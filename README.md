# Stock-Prediction
The git is about Indian Stock market prediction.

[**REF. RESEARCH PAPERS**](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Research)

## Types of data available with us:
1. News data 

2. Quant Data of Company listed in NSE (National Stock Exchange India) 

The model is based on correlating the stock and news data.

## Series of steps must be followed for predicting the stock price based on news:

1. Collecting Data: Mainly company related news which are listed nse India
  * Using twitter API 
  * Webscraping
  * Crawling
  * Kaggle

2. Preprocessing the data
  * Cleaning the news.
  * Associating company name to news article.

3. Predicting Sentiment based on previous sentiments:
  * Using Classifiers present in scipy library of python: Naive bayes, Bernaulli etc.
  * the Amazon Web Services Comprehend API boto.
  * nltk's Sentiment Intensity Analyser
  * Using deeplearning model.

4. Preprocessing the data stage2:
  * Using regression to find out news effect on stock price and volume
  
5. Correlating news with the stock data present:
  * Deeplearning model for correlating news impact on stock price and volume.
  * Using LSTM for predicting stock price.
  

### Explanation

**DATA COLLECTION**

We start collecting the news from different sources. We have scraped news from Moneycontrol, IIFL, Economic Times, Business Standard, Reuters and LiveMint. Attributes such as Tags, Title, Subtitle, Categories and Content along with the time and date of the news was scraped. Data from twitter is also scraped for better real-time collection of data. For more details, click [here](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Scraping). We also scraped twitter for getting realtime 
data and we used crawler to get the annual reports.

**PREPROCESSING DATA (stage1)**

Cleaning the news : Stemming, chunking, chinking, stopwords removal etc. Click [here](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/TextPreprocessing) for more details.

Associating company names to the news article to know which news was related to which company. Click [here](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Company%20Name%20Extractor) for more details.

**SENTIMENT ANALYSIS OF NEWS**

It is important to find the sentiment of each news. The sentiment value gives us a better understanding whether the news was a positive, negative, mixed or neutral one. This also helps in sorting out the neutral news. News of announcements and political parties have little role to play in building the model for forecasting. Hence these can be ignored. 

* Sentiment analysis using classifiers present in scipy library of python. This classifiers should be trained on a dataset.
  Followed by testing the prediction. The prediction accuracy of the model was around 70% on an average.
  [click here](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Sentiment%20analysis%20of%20news/MovieReviewsSentimentAnalysis) for the code.

* Sentiment analysis using the Amazon Web Services Comprehend API can be found [here](https://github.com/vishalsingh9423/Stock-Prediction/blob/master/Sentiment%20analysis%20of%20news/Sentiment%20using%20AWS%20comprehend/Sentiment%20using%20aws%20comprehend.ipynb).

* Sentiment Analysis using nltk's SentimentIntensityAnalyser. The SentimentIntensity analyser predicts the sentiment in 4 parts positive, negative, neutral and compound. The result of this library was quite accurate and up to mark. This library is already trained library, so it helped us labeling the text with a sentiment value.[Code](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Sentiment%20analysis%20of%20news/tfidfSentimentAnalysis)

* Sentiment Analysis using deeplearning model. The deep learning model requires a well labeled dataset in csv format. So first we need to get a labeled dataset (text with a sentiment label) and then train the model using that dataset and after training we can enter text in model and we can get a sentiment value of the text.[Code](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Sentiment%20analysis%20of%20news/deeplearningModel)

The accuracy of the deeplearning model is a **state of art accuracy**. It has an **accuracy of 97%**.

**PREPROCESSING DATA (stage2)**

In stage2 we need to label the news with quant data regression line slope value.
So for that we first open the news file and checked its date-time, now that date-time is searched in quant data. If the time is present in market hours of stock market then the text is labeled with slope value of regression line.Else if news is not in market hours then closing value of previous day and opening value of current days' regression line acts as its label.
[Code](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Merging%20quant%20and%20news)


**Training model based on data prepared in stage 2 preprocessing**

Now we have two values the sentiment value of the text and slope value of quant when the news broke out in the market.
We made a deep learning model such that the input was the sentiment value and the target value will be the slope value.
So from this we can predict if a news about a company comes in market what will be the impact of it on the price and volume of the stocks of that company. We cannot disclose the code for this model.

[EXTRA]

**Predicting stock value using Quant Data only (LSTM model)**

We also created a LSTM model which will be predicting a future price of stocks and this model is trained on just the stock data. The input of the model is closing value of previous day and target value was set to opening value of current day.
This model was not as accurate but it can predict the possibility and flow. [Code](https://github.com/vishalsingh9423/Stock-Prediction/tree/master/Sentiment%20analysis%20of%20news/Model%20for%20Stock%20Prediction%20using%20quant%20only)









