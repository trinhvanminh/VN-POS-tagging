import pycrfsuite
from itertools import chain
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report

def eval(test_x, test_y, crf_model):
        tagger = pycrfsuite.Tagger()
        tagger.open(crf_model)

        y_pred = []
        for feat_list in test_x:
            preds = tagger.tag(feat_list)
            y_pred.append(preds)

        lb = LabelBinarizer()
        y_true_all = lb.fit_transform(list(chain.from_iterable(test_y)))
        y_pred_all = lb.transform(list(chain.from_iterable(y_pred)))

        tagset = sorted(set(lb.classes_))
        class_indices = {cls: idx for idx, cls in enumerate(lb.classes_)}

        print(classification_report(
            y_true_all,
            y_pred_all,
            labels=[class_indices[cls] for cls in tagset],
            target_names=tagset,
            digits=5
        )) 

# test_x = 
# test_y = 
# eval(test_x, test_y, 'model.crf.tagger_new')

