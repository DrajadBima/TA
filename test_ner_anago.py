import anago.reader
import pprint
# weights = "model/ModelAnagoIndo/model_weights.h5"
# params = "model/ModelAnagoIndo/config.json"
# preprocessor = "model/ModelAnagoIndo/preprocessor.pkl"

model = anago.Sequence.load('model/ModelAnagoIndo')

words = 'Ahmad yani depan royal plaza padat merayap antrian hingga 2 km'.split()
pprint(model.analyze(words))
