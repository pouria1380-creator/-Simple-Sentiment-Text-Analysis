from newspaper import Article
import nltk
from textblob import TextBlob


nltk.download('punkt_tab')

url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

try:
    article.download()
    article.parse()
    article.nlp()  
    text = article.summary
    print(text)
except Exception as e:
    print(f"Error: {e}")


try: 
    blolb = TextBlob(text)
    sentiment = blolb.sentiment.polarity
    print(sentiment)
except Exception as e:
    print (f"Error: {e}")