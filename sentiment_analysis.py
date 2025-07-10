import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("tweets.csv")

# Function to analyze sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df['Sentiment'] = df['tweet'].apply(get_sentiment)

# Save to new CSV
df.to_csv("tweets_with_sentiment.csv", index=False)

# Print result
print(df)

# Plot the results
df['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
