import json
import re
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

# stopword_factory = StopWordRemoverFactory()
# stopwords = stopword_factory.get_stop_words()

namaFileInput = "event.json"
namaFileOutput = "event-_bersih.json"

input = open(namaFileInput, encoding="utf8")

loadJson = json.loads(input.read())
# print(loadJson)
# for i in response:
#  print({'text': i['text'], 'tgl': i['created_at']})
clean_tweet = list()
for i in loadJson:
    text = i['full_text']
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+', '', text, flags=re.MULTILINE) #@ dihapus
    text = re.sub(r'#\w+', '', text, flags=re.MULTILINE) ## dihapus
    text = re.sub(r'[\W_]+', ' ', text, flags=re.MULTILINE) #belum bisa 
    text = text.replace('\n',' ')

    # text = text.replace('\u2026',' ')
    # text = text.replace('\u00a0',' ')
    text = text.replace('RT','')
    text = re.sub(r'^ ', '', text, flags=re.MULTILINE)
    text = re.sub(r' $', '', text, flags=re.MULTILINE)
    text = text.lower()
    
    
    text = re.sub('\|','')
    

    text = stemmer.stem(text)
    # text = ' '.join([t for t in text.split() if t not in stopwords])
    print(text)

    clean_tweet.append({
        'text': text,
         'label' : 0
         })

output = open(namaFileOutput, 'w')
output.write(json.dumps(clean_tweet, indent=4))
output.close()
