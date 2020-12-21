'''https://www.programcreek.com/python/?code=rafasashi%2Frazzy-spinner%2Frazzy-spinner-master%2Fcore%2Fbin%2Fpython%2Fnltk%2Ftag%2Fcrf.py'''

'''
    A module for POS tagging using CRFSuite https://pypi.python.org/pypi/python-crfsuite
    
    >>> from nltk.tag import CRFTagger
    >>> ct = CRFTagger()
 
    >>> train_data = [[('University','Noun'), ('is','Verb'), ('a','Det'), ('good','Adj'), ('place','Noun')],
    ... [('dog','Noun'),('eat','Verb'),('meat','Noun')]]
    
    >>> ct.train(train_data,'model.crf.tagger')
    >>> ct.tag_sents([['dog','is','good'], ['Cat','eat','meat']])
    [[('dog', 'Noun'), ('is', 'Verb'), ('good', 'Adj')], [('Cat', 'Noun'), ('eat', 'Verb'), ('meat', 'Noun')]]
    
    >>> gold_sentences = [[('dog','Noun'),('is','Verb'),('good','Adj')] , [('Cat','Noun'),('eat','Verb'), ('meat','Noun')]] 
    >>> ct.evaluate(gold_sentences) 
    1.0
    
    Setting learned model file  
    >>> ct = CRFTagger() 
    >>> ct.set_model_file('model.crf.tagger')
    >>> ct.evaluate(gold_sentences)
    1.0
'''


