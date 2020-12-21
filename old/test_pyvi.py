'https://github.com/trungtv/pyvi'



from pyvi import ViTokenizer, ViPosTagger, ViUtils

str = u'Trường Đại học Bách Khoa hà nội'
a = ViTokenizer.tokenize(str)
print((a))

print(ViPosTagger.postagging(ViTokenizer.tokenize(str)))

print(ViUtils.remove_accents(str))

print(ViUtils.add_accents(u'truong dai hoc bach khoa ha noi'))




'''POS TAGS:

A - Adjective
C - Coordinating conjunction
E - Preposition
I - Interjection
L - Determiner
M - Numeral
N - Common noun
Nc - Noun Classifier
Ny - Noun abbreviation
Np - Proper noun
Nu - Unit noun
P - Pronoun
R - Adverb
S - Subordinating conjunction
T - Auxiliary, modal words
V - Verb
X - Unknown
F - Filtered out (punctuation)'''