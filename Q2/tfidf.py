from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
import pickle
import pandas as pd
import numpy as np



def dummy_fun(doc):
    return doc

if __name__ == "__main__":

    
    with open('../Q1/output.pickle', 'rb') as f:
        docs = pickle.load(f)


    tfidf = TfidfVectorizer(
        tokenizer=dummy_fun,
        preprocessor=dummy_fun,
        token_pattern=None)
    X = tfidf.fit_transform(docs)

    np.savetxt('./output.txt', X.A)
    
    # # print(X.shape)
    # array = np.loadtxt("output.txt")
    # print(len(array[0]))

    
