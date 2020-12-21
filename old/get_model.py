from nltk.tag import CRFTagger

_model_file = 'model.crf.tagger_2'

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

data = get_data()

# with open('vtb3.txt','w',encoding='utf-8') as vtb3:
#     vtb3.write(str(data))


ct = CRFTagger()
ct.train(data,_model_file)

