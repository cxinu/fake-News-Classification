import pickle
from newspaper import Article


def link(url):
    url_i = Article(url="%s" % (url), language='en')
    url_i.download()
    url_i.parse()
    return url_i.text


def classify(var):
    load_model = pickle.load(open('data/model.pickle', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])
    dictx = {"prediction": prediction[0], "probability": prob[0][1]}
    return dictx
