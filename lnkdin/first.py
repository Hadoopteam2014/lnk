import json
from django.shortcuts import render
import django
import twitter
import tweetwissen
from django.db import models
from twitterapp.models import *
from django.http import HttpResponse


import linkedin
from twitter.oauth_dance import parse_oauth_tokens
from linkedin.oauth import read_token_file, write_token_file
import webbrowser
OAUTH_FILE = "/home/anil/Home/lnkdin/linkedin_oauth"
CONSUMER_KEY = 'CN02H77TD04UsW1ieIXPmJkOa'
CONSUMER_SECRET = 'WTnhm09FsSYMOPTFuif7URVI051EV3Rj8t9NfCPlSIkiQ1ldXK'
oauth_callback = 'http://127.0.0.1:8000/oauth/'
def pynb_oauth_dance(request):
_linkedin = twitter.Twitter(auth=twitter.OAuth('', '', CONSUMER_KEY, CONSUMER_SECRET),format='', api_version=None)
oauth_token, oauth_token_secret = parse_oauth_tokens(_twitter.oauth.request_token(oauth_callback=oauth_callback))
write_token_file(OAUTH_FILE, oauth_token, oauth_token_secret)
oauth_url = ('http://api.twitter.com/oauth/authorize?oauth_token=' + oauth_token)
#webbrowser.open(oauth_url,new=0, autoraise=True)
return  HttpResponse(webbrowser.open(oauth_url,new=0, autoraise=True))
