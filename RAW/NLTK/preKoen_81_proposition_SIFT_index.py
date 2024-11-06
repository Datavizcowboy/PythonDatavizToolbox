import gensim
from gensim.models import word2vec
import logging
import gzip
import pandas as pd
# pd.options.mode.chained_assignment = None
import numpy as np
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
import csv
import datetime

""" --------------------------------- SET UP ------------------------------------ """

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

""" ---------------------------------------------------------------- ADD NEYBER """

articles_data_path = '../datatest/SearchBOT/Neyber_Searchbot.json'

# articles_data_path = '../datatest/Database/sift_database_20181218.json'

articles_data = []
articles_file = open(articles_data_path, "r")

with open(articles_data_path) as f:
    data = json.load(f)

content = pd.DataFrame()

data = data['data']
content['body'] = list(map(lambda data: data['attributes']['body_text'], data))
content['date'] = list(map(lambda data: data['attributes']['published_date'], data))
content['pub'] = list(map(lambda data: data['attributes']['url'].split('//')[1].split('/')[0], data))

content = content.dropna()



""" ------------------------------------------------------------ ADD WAGESTREAM """

client_data_path = '../datatest/SearchBOT/Wagestream_Searchbot.json'
client_data = []
client_file = open(client_data_path, "r")

with open(client_data_path) as q:
    data_client = json.load(q)

partial = pd.DataFrame()

data_client = data_client['data']
partial['body'] = list(map(lambda data_client: data_client['attributes']['body_text'], data_client))
partial['date'] = list(map(lambda data_client: data_client['attributes']['published_date'], data_client))
partial['pub'] = list(map(lambda data_client: data_client['attributes']['url'].split('//')[1].split('/')[0], data_client))

# partial['pub'] =  partial['pub'].apply(lambda x: print(x))

""" ---------------------------------------------------------------- ADD HASTEE """

competitor_data_path = '../datatest/SearchBOT/Hastee_Searchbot.json'
competitor_data = []
competitor_file = open(competitor_data_path, "r")

with open(competitor_data_path) as q:
    data_competitor = json.load(q)

competitor = pd.DataFrame()

data_competitor = data_competitor['data']
competitor['body'] = list(map(lambda data_competitor: data_competitor['attributes']['body_text'], data_competitor))
competitor['date'] = list(map(lambda data_competitor: data_competitor['attributes']['published_date'], data_competitor))
competitor['pub'] = list(map(lambda data_competitor: data_competitor['attributes']['url'].split('//')[1].split('/')[0], data_competitor))

""" ------------------------------------------------------------- ADD TO CORPUS """

content=content.append(partial)
content=content.append(competitor)

content = content.reset_index()
contentpost = content.drop_duplicates()
precontent = contentpost.values

documents = []
for ll in range(0,len(precontent)):
    check = bool(precontent[ll][1])
    if (check == True):
        stripped = gensim.utils.simple_preprocess (precontent[ll][1])
        documents.append(stripped)

documents_short=documents[:]

logging.info ("Done reading data file")

""" Wagestream only """

""" TF-IFD Matrix """

from sklearn.feature_extraction import text

synopses = content['body']

synopses_comp = competitor['body']

eng_contractions = ["ain't", "amn't", "aren't", "can't", "could've", "couldn't",
                    "daresn't", "didn't", "doesn't", "don't", "gonna", "gotta",
                    "hadn't", "hasn't", "haven't", "he'd", "he'll", "he's", "how'd",
                    "how'll", "how's", "I'd", "I'll", "I'm", "I've", "isn't", "it'd",
                    "it'll", "it's", "let's", "mayn't", "may've", "mightn't",
                    "might've", "mustn't", "must've", "needn't", "o'clock", "ol'",
                    "oughtn't", "shan't", "she'd", "she'll", "she's", "should've",
                    "shouldn't", "somebody's", "someone's", "something's", "that'll",
                    "that're", "that's", "that'd", "there'd", "there're", "there's",
                    "these're", "they'd", "they'll", "they're", "they've", "this's",
                    "those're", "tis", "twas", "twasn't", "wasn't", "we'd", "we'd've",
                    "we'll", "we're", "we've", "weren't", "what'd", "what'll",
                    "what're", "what's", "what've", "when's", "where'd", "where're",
                    "where's", "where've", "which's", "who'd", "who'd've", "who'll",
                    "who're", "who's", "who've", "why'd", "why're", "why's", "won't",
                    "would've", "wouldn't", "y'all", "you'd", "you'll", "you're",
                    "you've", "'s", "s","'d", "'m", 'abov', 'afterward', 'ai', 'alon',
                    'alreadi', 'alway', 'ani', 'anoth', 'anyon', 'anyth', 'anywher',
                    'becam', 'becaus', 'becom', 'befor', 'besid', 'ca', 'cri', 'dare',
                    'describ', 'did', 'doe', 'dure', 'els', 'elsewher', 'empti', 'everi',
                     'everyon', 'everyth', 'everywher', 'fifti', 'forti', 'gon', 'got',
                     'henc', 'hereaft', 'herebi', 'howev', 'hundr', 'inde', 'let', 'll',
                      'mani', 'meanwhil', 'moreov', "n't", 'na', 'need', 'nobodi', 'noon',
                      'noth', 'nowher', 'ol', 'onc', 'onli', 'otherwis', 'ought', 'ourselv',
                      'perhap', 'pleas', 'sever', 'sha', 'sinc', 'sincer', 'sixti', 'somebodi',
                       'someon', 'someth', 'sometim', 'somewher', 'ta', 'themselv', 'thenc',
                       'thereaft', 'therebi', 'therefor', 'togeth', 'twelv', 'twenti', 've',
                       'veri', 'whatev', 'whenc', 'whenev', 'wherea', 'whereaft', 'wherebi',
                        'wherev', 'whi', 'wo', 'yourselv', 'said', 'new', 'using']

stopwords = text.ENGLISH_STOP_WORDS.union(eng_contractions)

def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []

""" Text to Synopses """

for i in synopses:
    allwords_stemmed = tokenize_and_stem(i)
    totalvocab_stemmed.extend(allwords_stemmed)

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)


for j in synopses_comp:
    allwords_stemmed = tokenize_and_stem(j)
    totalvocab_stemmed.extend(allwords_stemmed)

    allwords_tokenized = tokenize_only(j)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame_comp = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(max_df=0.7, max_features=200000,
                                 min_df=0.3, stop_words=stopwords,
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,2))

tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)
terms = tfidf_vectorizer.get_feature_names()

tfidf_matrix_comp = tfidf_vectorizer.fit_transform(synopses_comp)
terms_comp = tfidf_vectorizer.get_feature_names()

sums = tfidf_matrix.sum(axis=0)
sums_comp = tfidf_matrix_comp.sum(axis=0)

""" Ranking of each of the individual """

datum = []
for col, term in enumerate(terms):
    datum.append( (term, sums[0,col] ))

ranking = pd.DataFrame(datum, columns=['term','rank'])


""" Prioritize keyphrases over keywords: 10 points each """

indices_keyphrases=[]

for dd in range(0,len(ranking)):
    if len(ranking['term'][dd].split())>1:
        # print(ranking['term'][dd])
        indices_keyphrases.append(dd)

for nn in range(0,len(indices_keyphrases)):
    ranking['rank'].loc[indices_keyphrases[nn]] = ranking["rank"].apply(lambda x: x+10).loc[indices_keyphrases[nn]]

rankingpost = ranking.sort_values('rank',ascending=False)
rankingpost = rankingpost.reset_index()

datum_comp = []
for col, term in enumerate(terms_comp):
    datum_comp.append( (term, sums_comp[0,col] ))

ranking_comp = pd.DataFrame(datum_comp, columns=['term','rank'])
rankingpost_comp = ranking_comp.sort_values('rank',ascending=False)
rankingpost_comp = rankingpost_comp.reset_index()

""" Recover the whole word """

accukeys=[]
accurank=[]
combination = []

for ind in range(0,len(rankingpost),1):
        accurank.append(rankingpost['rank'][ind])
        elements = len(rankingpost['term'][ind].split(' '))
        if (elements == 1):
            accukeys.append(vocab_frame.loc[rankingpost['term'][ind].split(' ')].values.tolist()[0][0])
        else:
            for ele in range(0,len(rankingpost['term'][ind].split(' ')),1):
                combination.append(vocab_frame.loc[rankingpost['term'][ind].split(' ')[ele]].values.tolist()[0][0])
            accukeys.append(' '.join(combination))
            combination=[]

""" COMPETITORS Recover the whole word """

accukeys_comp=[]
accurank_comp=[]
combination_comp = []

for ind in range(0,len(rankingpost_comp),1):
        accurank_comp.append(rankingpost_comp['rank'][ind])
        elements = len(rankingpost_comp['term'][ind].split(' '))
        if (elements == 1):
            accukeys_comp.append(vocab_frame_comp.loc[rankingpost_comp['term'][ind].split(' ')].values.tolist()[0][0])
        else:
            for ele in range(0,len(rankingpost_comp['term'][ind].split(' ')),1):
                combination_comp.append(vocab_frame_comp.loc[rankingpost_comp['term'][ind].split(' ')[ele]].values.tolist()[0][0])
            accukeys_comp.append(' '.join(combination_comp))
            combination_comp=[]

""" ---------------------------------------------------------------- SIFT Score """

denominator = '{:.2e}'.format(sum(accurank))

keyword_score=[]

for oo in range(0,len(accukeys)):
    factor = float(accurank[oo])/float(denominator)
    keyword_score.append(factor)

indexclient=[]

for ii in range(0,len(accukeys)):
    for gg in range(0,len(partial['body'])):
        checkin = accukeys[ii] in partial['body'].values[gg]
        # print(checkin)
        if (checkin == True):
            indexclient.append(ii)

""" Track Keywords """

unique_index=[]

for i in indexclient:
    if i not in unique_index:
        unique_index.append(i)

accu_rank=[]
for jj in range(0,len(unique_index)):
    accu_rank.append(accurank[jj])

numerator_client = '{:.2e}'.format(sum(accu_rank))

indexcompetitor=[]

for ii in range(0,len(accukeys)):
    for gg in range(0,len(competitor['body'])):
        checkin = accukeys[ii] in competitor['body'].values[gg]
        # print(checkin)
        if (checkin == True):
            indexcompetitor.append(ii)

""" Track Keywords """

unique_index_comp=[]

for i in indexcompetitor:
    if i not in unique_index_comp:
        unique_index_comp.append(i)

accu_rank_comp=[]
for jj in range(0,len(unique_index_comp)):
    accu_rank_comp.append(accurank[jj])

numerator_competitor = '{:.2e}'.format(sum(accu_rank_comp))

""" ---------------------------------------------------------------- SIFT INDEX """

SIFT_index_keyword=float(numerator_client)/float(denominator)
SIFT_index_keyword_comp=float(numerator_competitor)/float(denominator)

""" ----------------------------------------------------- DATE INDEX on Content """

today = datetime.datetime.now()
content['date'] = pd.to_datetime(content['date'])
content['date_raw']= content['date'].apply(lambda x: (today-x).days * 24 * 60)

""" ------------------------------------------------------------ KOEN's FORMULA """



""" ---------------------------------------------- Filter Articles older than X """

for pp in range (0,len(content)):
    if content['date_raw'][pp]>300000:
        content = content.drop([pp],axis=0)

themax = np.max(content['date_raw'])
content['date_index']= content['date_raw'].apply(lambda x: (themax-x)/themax)


koen = pd.DataFrame()


koen['date']=content['date']
koen['date_raw']=content['date_raw']
koen['date_index']=content['date_index']








""" --------------------------------------------------- Complementary Proposals """

common=[]

for ii in range(0,len(accukeys)):
    checkin = accukeys[ii] in accukeys_comp
    if (checkin == True):
        common.append(accukeys[ii])

proposition = list(set(accukeys_comp) - set(common))

common_pub=[]

for ii in range(0,len(partial['pub'].values)):
    checkpub = partial['pub'].values[ii] in competitor['pub'].values
    checkslash = '/' in partial['pub'].values[ii]
    if (checkin == True & checkslash == False):
        common_pub.append(partial['pub'].values[ii])

proposition_pub = list(set(competitor['pub'].values) - set(common_pub))

""" --------------------------------------------------- SIFT Index Publications """

""" Plain audience """

import random

audience = []

for tt in range(0,len(proposition_pub)):
    therandom = random.randint(1,100)
    thedomain = random.randint(1,5)
    audience.append(therandom**5/thedomain)

content['pub_raw']= content['pub'].apply(lambda x: random.randint(1,100)**5)
content['domain_raw']= content['pub'].apply(lambda x: random.randint(1,10))
content['pub_all_raw'] = content['pub_raw']/content['domain_raw']

themaxpub = np.max(content['pub_all_raw'])

# content['pub_index']= np.log(content['pub_all_raw']/themaxpub)

""" SWITCH """
# content['pub_index']= (content['pub_all_raw']/themaxpub)**0.3
content['pub_index']= content['pub_all_raw']*0


""" ------------------------------------------------------- SIFT Index Keywords """

sum_keywords_article=[]
keywords_article=[]

for gg in range(0,len(content['body'])):
    for ii in range(0,len(accukeys)):
        checkin = accukeys[ii] in content['body'].values[gg]
        # print(checkin)
        if (checkin == True):
            keywords_article.append(accurank[ii])
    sum_keywords_article.append(sum(keywords_article))
    keywords_article=[]

""" Normalize """

content['key_raw']=sum_keywords_article
themaxkey = np.max(content['key_raw'])
content['key_index']= (content['key_raw']/themaxkey)

""" --------------------------------------------------------- SWITCH OF ALL/NONE """

Name = 'Wagestream'
Name_comp = 'Neyber'
Name_comp2 = 'Hastee'

accunames=['Wagestream','Neyber','Hastee']

accu_name=[]
accu_comp=[]
accu_comp2=[]

for ii in range(0,len(accunames)):
    for gg in range(0,len(content['body'])):
        checkin = accunames[ii] in content['body'].values[gg]
        # print(checkin)
        if (checkin == True):
            accu_name.append(accunames[ii])
        else:
            accu_name.append(0)

    accu_comp.append(accu_name)
    accu_name=[]

# accu_comp2 = [sum(x) for x in zip(accu_comp[0], accu_comp[1], accu_comp[2])]
alles=[]
concon=[]

for jj in range(0,len(accu_comp[0])):
    for uu in range(0,len(accu_comp)):
        if accu_comp[uu][jj] != 0:
            concon.append(str(accu_comp[uu][jj]))
    alles.append(concon)
    concon=[]

zusammen=[]
for hh in range(0,len(alles)):
    zusammen.append(' '.join(alles[hh]))

content['mention'] = zusammen


"""----------------------------------------------------------- SIFT Index Total """

""" Coefficients """

date_coeff=0.5
pub_coeff=0.3
key_coeff=0.2

content['SIFT_index']=date_coeff*content['date_index']+pub_coeff*content['pub_index']+key_coeff*content['key_index']

content = content.sort_values('SIFT_index',ascending=False)
content = content.reset_index()

content = np.round(content, decimals=2)

""" --------------------------------------------- Let's propose some journalists """

folder='/Users/jmartinez/Sites/MGClimDeX/Dev_7c/'
path = '../datatest/Journalists/'

company=[]
journalist=[]
publication=[]

fp=open(path+'Manual_scrapping_comma.csv','r')

for t in fp.readlines(0):

        model_name=t.strip()
        data=model_name.split(',')

        company.append(data[0])
        journalist.append(data[2])
        publication.append(data[1].split('//')[1].split('/')[0])

fp.close()

unique_companies=[]

for i in company:
    if i not in unique_companies:
        unique_companies.append(i)

unique_publications=[]

for i in publication:
    if i not in unique_publications:
        unique_publications.append(i)

""" Sort by publications """

pub_indices=[]
pub_journalists=[]
pub_half_journalists=[]

for oo in range(0,len(unique_publications)):
    indices_pub = [i for i, x in enumerate(publication) if x == unique_publications[oo]]
    pub_indices.append(indices_pub)

for jj in range(0,len(pub_indices)):
    for kk in range(0,len(pub_indices[jj])):
        pub_half_journalists.append(journalist[pub_indices[jj][kk]])
    pub_journalists.append(pub_half_journalists)
    pub_half_journalists=[]

""" Sort by companies """

# indices=[]
all_indices=[]
all_journalists=[]
all_publications=[]
half_journalists=[]
half_publications=[]

for ii in range(0,len(unique_companies)):
    indices = [i for i, x in enumerate(company) if x == unique_companies[ii]]
    all_indices.append(indices)

for jj in range(0,len(all_indices)):
    for kk in range(0,len(all_indices[jj])):
        half_journalists.append(journalist[all_indices[jj][kk]])
        half_publications.append(publication[all_indices[jj][kk]])
    all_journalists.append(half_journalists)
    all_publications.append(half_publications)
    half_journalists=[]
    half_publications=[]

""" Scan the pub database """

scan_indices=[]

for ii in range(0,len(proposition_pub)):
    indices = [i for i, x in enumerate(unique_publications) if x == proposition_pub[ii]]
    if indices:
        scan_indices.append(indices)

for ll in range(0,len(scan_indices)):
    the_pub=unique_publications[scan_indices[ll][0]]
    the_writers=pub_journalists[scan_indices[ll][0]]
    the_writers_string=','.join(the_writers)
    # print('Publication: '+ the_pub + ' // Journalist: ' + the_writers_string)

""" ----------------------------------------------------------- PLOT THE OUTPUT """

# plt.scatter(content.date_index,content.key_index, s=content.SIFT_index*100)
# plt.show()

""" --------------------------------------------------  FILTER AND EXCEL OUTPUT """
#
# content_output = content.drop(['level_0','body','index'],axis=1)
# content_output.to_csv('/Users/jorge/Documents/GitHub/starter-flask-react-app/container/backend/datatest/SIFT_Index/SIFT_Index.csv', sep='\t', encoding='utf-8')
