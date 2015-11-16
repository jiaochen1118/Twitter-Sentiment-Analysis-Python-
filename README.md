# Twitter-Sentiment-Analysis-in-Python
##Get Twitter Data##
1. Create a twitter account at [https://dev.twitter.com/apps]. Record "API Key", "API secret", "Access token" and "Access token secret" information to replace the missing information in twitterstream.py in the file.
2. python tweet_sentiment.py AFINN-111.txt output.txt to save data.

##Derive the sentiment of each tweet##
AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0.
