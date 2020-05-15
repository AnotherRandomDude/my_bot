import tweepy
from datetime import datetime
import time
import os
from os import environ

interval = 60 * 30      #interval
consumer_key = environ['CONSUMER_KEY']
consumer_secret_key = environ['CONSUMER_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

currentMonth = datetime.now().strftime('%h')
currentYear = datetime.now().year

api = tweepy.API(auth)

while (True):

    if (datetime.now().hour >= 7 and datetime.now().hour <= 23):

        tbody = f'------------------------ CANADA ---------------------------- \n{currentMonth} {currentYear} \nEnjoy $5.00 Off Your First Order With Skip The Dishes! \nClick my referral Link: http://skipthedishes.com/r/PZ01zaXhrU \n#skipthedishes \n#skipthedishescoupon \n#helpauniversitystudentgetfood \nThanks'
        api.update_with_media("skip.jpg", tbody)
        
    time.sleep(interval)
    
    if (datetime.now().hour < 7 and datetime.now().hour > 23):

        tbody = f'------------------------ CANADA ---------------------------- \n{currentMonth} {currentYear} \nEnjoy $5.00 Off Your First Order With Skip The Dishes! \nClick my referral Link: http://skipthedishes.com/r/PZ01zaXhrU \n#skipthedishes \n#skipthedishescoupon \n#helpauniversitystudentgetfood \nThanks'
        api.update_with_media("skip.jpg", tbody)
        
    time.sleep(interval * 4)