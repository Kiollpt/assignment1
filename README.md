
Installation:
==========
`pipenv install`

Question1:
==========
1. Use [Scrapy](https://docs.scrapy.org/en/latest/) to extract the descriptions in RSS. 
   Go to path `cd RSScrawler/RSScrawler` and run `scrapy crawl rss`  will generate two files
   `news.rss` and `description.txt` in the directory Q1.

2. Select [Jieba](https://github.com/fxsjy/jieba) to tokenize with the zh-TW dictionary and also remove the Chinese stopwords.

    run `python tokenizer.py`


Question2:
==========
    
run ```python tfidf.py```

1. Use [sklearn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to transform the vectors.
2. Save the vectors to .txt by [Numpy](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html).
