import os

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from pprint import pprint
os.environ['CLASSPATH'] = 'Z:\TA\stanford-ner'

st = StanfordNERTagger('model/ner-model.ser.gz')

text = 'Mau punya tas canvas dgn hasil lukisan sendiri? Penasaran gimana serunya ngelukis di tas canvas? Yuk ikut Workshop Bersama @defirash_totebag & Beauty Class di WBH Surabaya, Minggu 31 Maret jam 12.30, HTM 75.000/orang. Info : 085730835779 - Anggie'
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

pprint(classified_text)
