import sys
import json
import numpy as np

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiment_term = {}
    for line in sent_file:
	term, score = line.split("\t")
	sentiment_term[term] = int(score)

    new_sentiment = {}
    for line in tweet_file:
	sum = 0
	tweet = json.loads(line)
	if 'lang' in tweet.keys() and tweet["lang"]=='en':
	    if 'text' in tweet.keys():
		words = tweet['text'].split()
		for word in words:
		    if word in sentiment_term:
			sum += sentiment_term[word]
		    elif len(word) > 1 and word.isalnum() and word.lower() not in new_sentiment:
			new_sentiment[word.lower()] = []
		for word in words:
		    if word.lower() in new_sentiment:
			new_sentiment[word.lower()].append(sum)	
     
    for key, item in new_sentiment.items():
	print key + " " + str(np.mean(item))	

if __name__ == '__main__':
    main()
