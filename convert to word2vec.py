from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import datapath, get_tmpfile

namaFileGlove = "glove_wiki_id.txt"
glove_file = datapath(namaFileGlove)
tmp_file = get_tmpfile("model")

glove2word2vec(glove_file, tmp_file)
