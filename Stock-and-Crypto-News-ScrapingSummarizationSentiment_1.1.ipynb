{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "59e9ecc6",
   "metadata": {},
   "source": [
    "## 1. Install and Import Baseline Dependencies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "35fb751d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import PegasusTokenizer, PegasusForConditionalGeneration\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import re\n",
    "from transformers import pipeline\n",
    "import csv"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fbf2e57e",
   "metadata": {},
   "source": [
    "## 2. Setup Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9184ef60",
   "metadata": {},
   "outputs": [],
   "source": [
    "model_name = \"human-centered-summarization/financial-summarization-pegasus\"\n",
    "tokenizer = PegasusTokenizer.from_pretrained(model_name)\n",
    "model = PegasusForConditionalGeneration.from_pretrained(model_name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17c5219d",
   "metadata": {},
   "source": [
    " ## 3. Setup Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e7da38f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# monitored_tickers = ['ETH']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "404cb2f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter A List Of Tickers To Monitor (separated by spaces): JPM BAC NKE\n"
     ]
    }
   ],
   "source": [
    "# Take input from the user for the monitored tickers\n",
    "monitored_tickers = input(\"Enter A List Of Tickers To Monitor (separated by spaces): \").split()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "94d3bde3",
   "metadata": {},
   "source": [
    "## 4.1. Search for Stock News using Google and Yahoo Finance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "58802155",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searching For Stock News For ['JPM', 'BAC', 'NKE']\n"
     ]
    }
   ],
   "source": [
    "print('Searching For Stock News For', monitored_tickers)\n",
    "def search_for_stock_news_links(ticker):\n",
    "    search_url = 'https://www.google.com/search?q=yahoo+finance+{}&tbm=nws'.format(ticker)\n",
    "    r = requests.get(search_url)\n",
    "    soup = BeautifulSoup(r.text, 'html.parser')\n",
    "    atags = soup.find_all('a')\n",
    "    hrefs = [link['href'] for link in atags]\n",
    "    return hrefs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "891a211c",
   "metadata": {},
   "outputs": [],
   "source": [
    "raw_urls = {ticker:search_for_stock_news_links(ticker) for ticker in monitored_tickers}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffc82ae7",
   "metadata": {},
   "source": [
    "## 4.2. Strip - Out Unwanted URLs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "11de43aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cleaning URLs...\n"
     ]
    }
   ],
   "source": [
    "print('Cleaning URLs...')\n",
    "exclude_list = ['maps', 'policies', 'preferences', 'accounts', 'support']\n",
    "def strip_unwanted_urls(urls, exclude_list):\n",
    "    val = []\n",
    "    for url in urls:\n",
    "        if 'https://' in url and not any(exc in url for exc in exclude_list):\n",
    "            res = re.findall(r'(https?://\\S+)', url)[0].split('&')[0]\n",
    "            val.append(res)\n",
    "    return list(set(val))\n",
    "\n",
    "cleaned_urls = {ticker:strip_unwanted_urls(raw_urls[ticker] , exclude_list) for ticker in monitored_tickers} "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "053cc65e",
   "metadata": {},
   "source": [
    "## 4.3. Search and Scrape Cleaned URLs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "249cd785",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Scraping News Links...\n"
     ]
    }
   ],
   "source": [
    "print('Scraping News Links...')\n",
    "def scrape_and_process(URLs):\n",
    "    ARTICLES = []\n",
    "    for url in URLs:\n",
    "        r = requests.get(url)\n",
    "        soup = BeautifulSoup(r.text, 'html.parser')\n",
    "        results = soup.find_all('p')\n",
    "        text = [res.text for res in results]\n",
    "        words = ' '.join(text).split(' ')[:350]\n",
    "        ARTICLE = ' '.join(words)\n",
    "        ARTICLES.append(ARTICLE)\n",
    "    return ARTICLES\n",
    "articles = {ticker:scrape_and_process(cleaned_urls[ticker]) for ticker in monitored_tickers}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "595cac55",
   "metadata": {},
   "source": [
    "## 4.4. Summarise all Articles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bb132571",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Summarizing Articles...\n"
     ]
    }
   ],
   "source": [
    "print('Summarizing Articles...')\n",
    "def summarize(articles):\n",
    "    summaries = []\n",
    "    for article in articles:\n",
    "        input_ids = tokenizer.encode(article, return_tensors=\"pt\")\n",
    "        output = model.generate(input_ids, max_length=55, num_beams=5, early_stopping=True)\n",
    "        summary = tokenizer.decode(output[0], skip_special_tokens=True)\n",
    "        summaries.append(summary)\n",
    "    return summaries\n",
    "\n",
    "summaries = {ticker:summarize(articles[ticker]) for ticker in monitored_tickers}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb72c737",
   "metadata": {},
   "source": [
    "## 5. Adding Sentiment Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7027d4a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer\n",
    "\n",
    "model_name = \"distilbert-base-uncased-finetuned-sst-2-english\"\n",
    "model = AutoModelForSequenceClassification.from_pretrained(model_name)\n",
    "tokenizer = AutoTokenizer.from_pretrained(model_name)\n",
    "sentiment = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)\n",
    "scores = {ticker:sentiment(summaries[ticker]) for ticker in monitored_tickers}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d1792f7",
   "metadata": {},
   "source": [
    "## 6. Exporting Results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a70657bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exporting Results...\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "print('Exporting Results...')\n",
    "\n",
    "def create_output_array(summaries, scores, urls):\n",
    "    output = []\n",
    "    for ticker in monitored_tickers:\n",
    "        for counter in range(len(summaries[ticker])):\n",
    "            output_this = [\n",
    "                            ticker, \n",
    "                            summaries[ticker][counter], \n",
    "                            scores[ticker][counter]['label'], \n",
    "                            scores[ticker][counter]['score'], \n",
    "                            urls[ticker][counter]\n",
    "                          ]\n",
    "            output.append(output_this)\n",
    "    return output\n",
    "\n",
    "final_output = create_output_array(summaries, scores, cleaned_urls)\n",
    "final_output.insert(0, ['Ticker','Summary', 'Sentiment', 'Sentiment Score', 'URL'])\n",
    "\n",
    "# Get the current date and time in the format DD_MM_YYYY_HH_MM_SS\n",
    "current_date_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')\n",
    "\n",
    "# Construct the file name using the current date and time\n",
    "file_name = f'summaries_{current_date_time}.csv'\n",
    "\n",
    "# Open the file for writing\n",
    "with open(file_name, mode='w', newline='') as f:\n",
    "    csv_writer = csv.writer(f, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)\n",
    "    csv_writer.writerows(final_output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5d750802",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done!\n"
     ]
    }
   ],
   "source": [
    "print('Done!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4779592c",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Umang Laad\n",
    "## 20100BTCSDSI07300"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0366e1bc",
   "metadata": {},
   "source": [
    "## Anaconda3 Prompt Commands"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63b936de",
   "metadata": {},
   "outputs": [],
   "source": [
    "## cd \"C:\\Users\\laad_\"\n",
    "## python Stock-and-Crypto-News-ScrapingSummarizationSentiment_1.1.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
