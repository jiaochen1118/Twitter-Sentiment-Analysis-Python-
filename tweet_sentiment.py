import json
import sys

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
   # lines(sent_file)
   # lines(tweet_file)
    
    scores = {}
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.
    
    for line in tweet_file:
	tweet = json.loads(line)
        sum = 0	
        if 'lang' in tweet.keys() and tweet["lang"]=='en':
	   if 'text' in tweet.keys():
		words = tweet['text'].split()
		for word in words:
		    if word in scores:
			sum += scores[word]     
	print str(sum)

if __name__ == '__main__':
    main()
