from gensim.models import KeyedVectors

namaFileModel = "model/w2vec_glove_wiki_id.txt"
model = KeyedVectors.load_word2vec_format(namaFileModel)
hasil = model.most_similar("Bandung")
print("Bandung:{}".format(hasil))
hasil = model.most_similar("tempo")
print("tempo:{}".format(hasil))
hasil = model.most_similar("Tempo")
print("Tempo:{}".format(hasil))
hasil = model.most_similar("Soekarno")
print("Soekarno:{}".format(hasil))

sim = model.similarity("bakso", "nasi")
print("Kedekatan bakso-nasi: {}".format(sim))
sim = model.similarity("bakso", "pecel")
print("Kedekatan bakso-pecel: {}".format(sim))
sim = model.similarity("bakso", "mobil")
print("Kedekatan bakso-mobil: {}".format(sim))

hasil = model.most_similar_cosmul(positive=['perempuan', 'raja'], negative=['pria'])
print("pria-raja, perempuan-?: {}".format(hasil))

hasil = model.most_similar_cosmul(positive=['perempuan', 'raja'], negative=['lelaki'])
print("lelaki-raja, perempuan-?:{}".format(hasil))

hasil = model.most_similar_cosmul(positive=['minuman', 'mangga'], negative=['buah'])
print("buah-mangga, minuman-?:{}".format(hasil))