import pandas as pd 
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import nltk
import pickle
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
lemma = WordNetLemmatizer()
stop_words = stopwords.words('english')
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


def remove_emoji(string):
    """remove emojis from text"""
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F" # emoticons
                               u"\U0001F300-\U0001F5FF" # symbols & pictographs
                               u"\U0001F680-\U0001F6FF" # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

 
def preprocessing(x):
     corp = str(x).lower()  #lower
     corp = re.sub('[^a-zA-Z]+',' ', corp).strip() #keep text
     #corp = re.sub('[0-9]+', '', corp)
     corp=remove_emoji(corp) # remove emojis
     tokens = word_tokenize(corp) #tokenization
     words = [w for w in tokens if len(w) > 2 if not w in stop_words] # remove stop words and words with less than two caracters
     lemmatize = [lemma.lemmatize(w) for w in words] #lemmatization
     l=(' ').join(lemmatize)
     return l
 
def preprocess(self, X):
    preprocess_text = [preprocessing(i) for i in X['body']]
    X["preprocess_txt"] = preprocess_text
    return X

