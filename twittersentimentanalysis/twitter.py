from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)

# Twitter Keys
consumerKey = "vvQsPr1t3cXdhdztLlkr3W5Nl"
consumerSecret = "HRbGcTW8DBqDHiWAHRNwdxnxHcVQybalRYxCcDL6zoHXBlKdWR"
accessToken = "4020773291-dPNo5iiwEGfnWZHk7pqNUC0rtCZP1M8JRCh0oMc"
accessTokenSecret = "0PonLR4MyEHcczv3UXwMyQMX2CG2SXaT0IgLmvnmY6R6z"


# Establish a connection to Twitter
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# Get search term and number of tweets
searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

# Get the number of tweets related to search term
tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)
positive = 0
negative = 0
neutral = 0
polarity = 0

# Display each tweet

for tweet in tweets:
    #print(tweet.text)
    # get the text of the tweets
    analysis = TextBlob(tweet.text)
    #print(analysis)
    # Add up the polarity of each tweet
    polarity += analysis.sentiment.polarity

    # Add up if each tweet if positive, negative or neutral
    if analysis.sentiment.polarity == 0:
        neutral += 1
    elif analysis.sentiment.polarity < 0.00:
        negative += 1
    elif analysis.sentiment.polarity > 0.00:
        positive += 1

# Explanation of percentage function
# print(neutral)
# print(negative)
# print(positive)
#
# print(float(neutral))
# print(float(noOfSearchTerms))
# print(float(neutral)/float(noOfSearchTerms))
# print(100 * float(neutral)/float(noOfSearchTerms))

# Getting the percentages of each polarity
positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)
#print(neutral)

positive = format(positive, '.2f')
#print(positive)
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')
#print(neutral)

print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " Tweets.")

if polarity == 0:
    print("Neutral")
elif polarity > 0.00:
    print("Positive")
elif polarity < 0.00:
    print("Negative")

labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, text = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " Tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()