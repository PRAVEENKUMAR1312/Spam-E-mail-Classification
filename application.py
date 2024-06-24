import streamlit as st
import pickle
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer


#Loading the model
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

#Transform text function
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

nltk.download('stopwords')
ps = PorterStemmer()

def transform_text(text):
    text = text.lower() #Conversion to lowercase
    text = nltk.word_tokenize(text) #Tokenizing

    text = [word for word in text if word.isalnum()] #Removing spl char and acquirng the alphanumeric words

    text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation] #Removing Stopwords and punctuations
    
    text = [ps.stem(word) for word in text] #Stemming

    return " ".join(text)

#Streamlit code
st.title("E-Mail Spam Classifier")
input_sms = st.text_area("Enter Message")

if st.button('Predict'):
    #Preprocess
    transformed_sms = transform_text(input_sms)
    #vectorize
    vector_input =tfidf.transform([transformed_sms])
    #prediction
    result = model.predict(vector_input)[0]
    #To display
    if result == 1:
        st.header(" SPAM.IGNORE IT! ")
    else:
        st.header(" NOT A SPAM")    
 