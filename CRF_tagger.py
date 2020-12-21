
import pycrfsuite
import re
import unicodedata
from underthesea import word_tokenize
# import tkinter as tk

_model_file = 'model.crf.tagger_ver2'

def sentence_tokenizer(str):
    # split = re.split('(?<=[.?!])\s+', str)
    split = re.split(r'(?<=(?:(?<!ThS(?=\.))(?<!TS(?=\.))(?<!PGS(?=\.))(?<!GS(?=\.))(?<!BS(?=\.)))[.?!])\s+', str)
    return split

# ------------------------------------------------------------------

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
        # Is End Of Sentences
        if idx < len(tokens)-1:
            if (tokens[idx+1]=='.' or tokens[idx+1]=="..." or tokens[idx+1]=="!" or tokens[idx+1]=="?") and idx==len(tokens)-2:
                feature_list.append("END_TRUE")
            else:
                feature_list.append("END_FALSE")
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
    trainer.set_params(({}))
    
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

# -------------------------------------------------------------------

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

# l = [['học_sinh','học','sinh_học'],['học_sinh', 'học', 'ăn', '.']]
# print(tag_sents(l))


# ---------------------------------------------------------------------

# sentence = 'Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò.'

# # print(word_tokenize(sentence))
# # ['Chàng trai', '9X', 'Quảng Trị', 'khởi nghiệp', 'từ', 'nấm', 'sò']
# print(tag_sents([word_tokenize(sentence)]))

# -------------------------------------------------------


# Function using by console.py
def sen_tagger(sen):
    w_list = word_tokenize(sen)
    for i in range(len(w_list)):
        w_list[i] =  w_list[i].replace(' ','_')
    result_list=tag_sents([w_list])
    result_str=''
    for i in range(len(result_list[0])):
        if i==0:
            result_str+=result_list[0][i][0]+'/'+result_list[0][i][1]
        else:
            result_str+=' '+result_list[0][i][0]+'/'+result_list[0][i][1]
    return result_str

