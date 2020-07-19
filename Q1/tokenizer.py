import pandas as pd
import os
import re
import string
import jieba
import pickle
jieba.set_dictionary('./dict.txt.big')
import sys

# def remove_punctuation(text:str):
    
#     text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",text)
#     text = re.sub("[【】╮╯▽╰╭★→「」]+","",text)
#     text = re.sub("！，❤。～《》：（）【】「」？”“；：、","",text)
#     noPunct = "".join([c for c in text if c not in string.punctuation and c])
#     return noPunct

stopWord = [x for x in open('./zh_stopword.txt','r').read().split('\n')]

def tokenization(text:str):
 
    tokens = set(jieba.cut(text))

    return ([t for t in tokens if t and t not in stopWord])





if __name__ == "__main__":
    fileName = "description.txt"

    df = pd.read_csv(fileName,names=["description"])

    df["token"]  = df.description.apply(tokenization)

    with open("./output.txt","w") as f:
        for _,i in df.iterrows():
            f.write(str(i["token"])+"\n")


    with open("./output.pickle","wb") as f:
        pickle.dump(df.token.tolist(), f)

    
    