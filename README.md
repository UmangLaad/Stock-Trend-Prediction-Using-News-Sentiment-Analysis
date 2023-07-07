# Stock-Trend-Prediction-Using-News-Sentiment-Analysis
This GitHub repository contains a Python project designed to automate the monitoring of financial markets and efficiently gather trading ideas. The project utilizes web scraping techniques, NLP-based summarization, and sentiment analysis to extract valuable insights from finance news articles and calculate sentiment for specific assets.

## ABSTRACT

The Efficient Market Hypothesis (EMH) is a widely recognized theory in finance that suggests 
that all available information about a stock is already reflected in its current market price. 
According to EMH, it is impossible for an investor to consistently outperform the market because 
stock prices already reflect all known information.
Despite the popularity of the EMH, there have been several instances where it has been 
challenged and even shown to be flawed. This has led to a surge in research efforts aimed at 
finding alternative methods for predicting stock trends. One such method involves using non-quantifiable data, such as financial news articles, to predict future stock trends.
The idea behind this approach is that news articles can have a significant impact on stock market 
performance. By analysing news sentiment and classifying it as positive, negative, or neutral, it 
is possible to gain insights into how a particular company is perceived by the public and how this 
perception might affect its stock performance.
This project aims to explore the relationship between news sentiment and stock trends by 
analysing financial news articles about a particular company and using this data to predict its 
future stock trend. By leveraging natural language processing and machine learning techniques, 
the project seeks to identify patterns in the news sentiment data that can be used to make accurate 
predictions about future stock trends.
The significance of this research lies in its potential to provide investors with a new tool for 
predicting stock trends. By incorporating news sentiment analysis into their decision-making 
processes, investors may be able to make more informed decisions and achieve better returns. 
Additionally, the project may shed light on the extent to which news sentiment influences stock 
market performance and contribute to a deeper understanding of the complex relationship 
between news and finance.

## Problem Statement

The stock market is a dynamic and complex environment where the value of securities fluctuates 
rapidly and unpredictably. Traders in this market face numerous challenges, including keeping track 
of all the information that could affect stock prices, predicting future trends accurately, and making 
profitable trades. Technical and fundamental analyses are widely used approaches to predict stock 
trends. However, their efficacy is debatable, and they may not always capture all the relevant factors 
that affect stock prices.
Active and Daily Traders often make rapid trades based on short-term trends in the market, which 
requires them to make quick decisions based on the latest information available. However, this 
information is often scattered across multiple news sources and can be difficult to keep track of in 
real-time. This can lead to missed opportunities and reduced profitability.
Another issue is the sheer volume of news articles that are produced every day. Traders and investors 
need to be able to quickly identify the most relevant news articles and evaluate their potential impact 
on stock prices. This can be a time-consuming process that may require them to filter through large amounts of irrelevant information. The sheer volume of news also poses a significant risk of 
information overload. Traders and investors who are overwhelmed by the amount of information 
available to them may struggle to make sense of it all, leading to analysis paralysis or decision 
fatigue.
In conclusion, the sheer volume of news articles produced every day is a significant challenge for 
traders and investors who rely on timely and relevant information to make informed decisions. This 
challenge requires the use of sophisticated news analysis tools and machine learning algorithms to 
filter through the noise and identify relevant insights. Failure to do so can result in missed 
opportunities and suboptimal investment decisions, which can have significant financial 
consequences in the dynamic and competitive world of the stock market.

## Proposed Solution

- Needed to automate monitoring of financial markets and gather trading ideas efficiently.
- Developed a Python project to scrape finance news, perform NLP-based summarization, and calculate sentiment for specific assets.
- Used Python and BeautifulSoup for web scraping from sites like Yahoo Finance.
- Implemented a fine-tuned Hugging Face Pegasus Transformers model for automated summarization.
- Employed a pre-trained Transformers deep learning pipeline for sentiment analysis.

- The pipeline generates article summaries, conducts sentiment analysis for assets like Bitcoin, Ethereum, Tesla, and Gamestop, allows easy updates for more stocks/cryptocurrencies, and exports results to a CSV file for further analysis.

## Input Screenshot
<h4>The screenshot below shows an example of the input being given to the project in the form of stock ticker symbols. The system processes this input to scrape relevant finance news articles, generate summaries, and perform sentiment analysis for each specified asset. 

<br>

![Screenshot (2432)](https://github.com/UmangLaad/Stock-Trend-Prediction-Using-News-Sentiment-Analysis/assets/81899965/658eccdd-001d-4504-813e-1f0bbfc7618c)



