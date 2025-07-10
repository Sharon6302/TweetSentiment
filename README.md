# 🐦 TweetSentiment – Twitter Sentiment Analysis using NLP

This project performs **sentiment analysis** on a set of sample tweets using Python's NLP library TextBlob. Each tweet is classified as **Positive**, **Negative**, or **Neutral**, and results are visualized in a bar chart.

---

## 📁 Project Files

| File Name              | Description                                  |
|------------------------|----------------------------------------------|
| `tweets.csv`           | Input dataset with example tweets            |
| `sentiment_analysis.py`| Python code for analyzing sentiment          |
| `tweets_with_sentiment.csv` | Output file with sentiment predictions |
| `README.md`            | Project overview and instructions            |

---

## 🚀 How It Works

1. Loads tweets from a CSV file
2. Analyzes each tweet using TextBlob
3. Labels sentiment: **Positive**, **Negative**, or **Neutral**
4. Saves results and plots a sentiment distribution chart

---

## 🖥 How to Run

```bash
pip install pandas matplotlib textblob
python -m textblob.download_corpora
python sentiment_analysis.py
