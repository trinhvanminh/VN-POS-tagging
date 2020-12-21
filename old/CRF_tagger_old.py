
import pycrfsuite
import re
import unicodedata

_model_file = 'model.crf.tagger'

def _get_features(tokens, idx):
        """
        Extract basic features about this word including
             - Current Word
             - Is Capitalized ?
             - Has Punctuation ?
             - Has Number ?
             - Suffixes up to length 3
        Note that : we might include feature over previous word, next word ect.
        :return : a list which contains the features
        :rtype : list(str)
        """
        token = tokens[idx]

        feature_list = []

        if not token:
            return feature_list

        # Capitalization
        if token[0].isupper():
            feature_list.append("CAPITALIZATION")

        # Number
        if re.search(re.compile(r"\d"), token) is not None:
            feature_list.append("HAS_NUM")

        # Punctuation
        punc_cat = set(["Pc", "Pd", "Ps", "Pe", "Pi", "Pf", "Po"])
        if all(unicodedata.category(x) in punc_cat for x in token):
            feature_list.append("PUNCTUATION")

        # Suffix up to length 3
        if len(token) > 1:
            feature_list.append("SUF_" + token[-1:])
        if len(token) > 2:
            feature_list.append("SUF_" + token[-2:])
        if len(token) > 3:
            feature_list.append("SUF_" + token[-3:])

        feature_list.append("WORD_" + token)

        return feature_list

def train(train_data, model_file):
    '''
    Train the CRF tagger using CRFSuite  
    :params train_data : is the list of annotated sentences.        
    :type train_data : list (list(tuple(str,str)))
    :params model_file : the model will be saved to this file.     
        
    '''
    trainer = pycrfsuite.Trainer(verbose=False)
    trainer.set_params(({
            # 'c1': 1.0,                            # coefficient for L1 penalty
            # 'c2': 1e-3,                           # coefficient for L2 penalty
            # 'max_iterations': 50,                 # stop earlier
            # 'feature.possible_transitions': True  # include transitions that are possible, but not observed
        }))
    
    for sent in train_data:
        tokens,labels = zip(*sent)
        features = [ _get_features(tokens,i) for i in range(len(tokens))]
        trainer.append(features,labels)
                    
    # Now train the model, the output should be model_file
    trainer.train(model_file)
    # Save the model file
    pycrfsuite.Tagger().open(model_file)

def get_data(ifile='vtb.txt'):
    data = []
    with open(ifile, encoding='utf-8') as vtb:
        for _ in range(10383):
            temp = []
            a = vtb.readline().split()
            for i in a:
                if i == '/':
                    i = ['/','/']
                    temp.append(tuple(i))
                else:
                    temp.append(tuple(i.split('/')))
            data.append(temp)
    return data

# data = get_data()
# train(train_data=data, model_file=_model_file)


def tag_sents(sents):
    '''
    Tag a list of sentences. NB before using this function, user should specify the mode_file either by 
                    - Train a new model using ``train'' function 
                    - Use the pre-trained model which is set via ``set_model_file'' function  
    :params sentences : list of sentences needed to tag. 
    :type sentences : list(list(str))
    :return : list of tagged sentences. 
    :rtype : list (list (tuple(str,str))) 
    '''
    if _model_file == '':
        raise Exception(' No model file is found !! Please use train or set_model_file function')
    

    tagger = pycrfsuite.Tagger()
    tagger.open(_model_file) 
    # We need the list of sentences instead of the list generator for matching the input and output
    result = []  
    for tokens in sents:
        features = [_get_features(tokens,i) for i in range(len(tokens))]
        labels = tagger.tag(features)
            
        if len(labels) != len(tokens):
            raise Exception(' Predicted Length Not Matched, Expect Errors !')
        
        tagged_sent = list(zip(tokens,labels))
        result.append(tagged_sent)
        
    return result 

l = [['học_sinh', 'học', 'sinh_học','/'],['học_sinh', 'học', 'ăn', '.']]
print(tag_sents(l))