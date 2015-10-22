import praw
from pprint import pprint

from emailer import email

__author__ = 'Dan'

#r = praw.Reddit(user_agent='Testing reddit API for Dan B.')

#submissions = r.get_subreddit('starcraft').get_hot(limit=10)

#links = {}
#for submission in submissions:
    #links[str(submission)] = str(submission.url)

#pprint(links)

email()

##TODO: now build up email and send it out.




