from nltk.tag import CRFTagger

model_name = 'model.crf.tagger_2'
# Setting learned model file  

gold_sentences = [[('học_sinh', 'N'), ('học', 'V'), ('sinh_học', 'N')]]
ct = CRFTagger() 
ct.set_model_file(model_name)
print(ct.evaluate(gold_sentences))
# 1.0

l = [['học_sinh', 'học', 'sinh_học', '/'],]

print(ct.tag_sents(l))
# [[('học_sinh', 'N'), ('học', 'V'), ('sinh_học', 'N')]]