# Stock-Prediction
The git is about Indian Stock market prediction.

## Types of data available with us:
1.News data 

2.Quant Data of Company listed in NSE (National Stock Exchange India) 

The model is based on correlating the stock and news data.

## Series of steps must be followed for predicting the stock price based on news:

1. Collecting Data: Mainly company related news which are listed nse India
  * Using twitter API 
  * Webscraping
  * Crawling
  * Kaggle

2. Preprocessing the data
  * Cleaning the news: Stemming, chunking, chinking, stopwords removal etc.
  * Labeling the news with a sentiment value

3. Predicting Sentiment based on previous sentiment:
  * Using Classifiers present in scipy library of python: Naive bayes, Bernaulli etc.
  * Using deeplearning model.
  
4. Correlating news with the stock data present:
  * Deeplearning model.
  * Using regression to find out news effect on stock price and volume
  

### Explanation

We start collecting the news from different sources. We have scraped news from Moneycontrol, IIFL, Economic Times, Business Standard, Reuters and LiveMint. Attributes such as Tags, Title, Subtitle, Categories and Content along with the time and date of the news was scraped. For more details, click [Here](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Scraping).
