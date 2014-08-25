from django.shortcuts import render

from django.http import HttpResponse
import urllib2
import urllib
import requests
import oauth2 
import urlparse
import json
from twitter.oauth import OAuth
import twitter
from twitterapp.models import *
from twitter.oauth_dance import parse_oauth_tokens
from twitter.oauth import read_token_file, write_token_file
from twitter.oauth_dance import oauth_dance
import webbrowser
from twitterapp.html import test
consumer_key = 'RJZMooGv5i6u4BiJ5bh1wdj87'
consumer_secret = 'xuv7MgW5MaRnVLCFTQxy1UNjjJVayKcgCSROSzQcJHwZlxZ2sK'
app_name = "Tweetwissen"
twitter1 = twitter.Twitter(auth=twitter.OAuth('', '', consumer_key, consumer_secret),format='', api_version=None)
oauth_token, oauth_token_secret = parse_oauth_tokens(twitter1.oauth.request_token()) 
oauth_url = ('https://api.twitter.com/oauth/authorize?oauth_token=' + oauth_token)
fopen=open('jsp1.js','rb')
a=fopen.readline()
b=a.replace('myvar',oauth_token)
def index(request):
  return HttpResponse(b)
def index1(request):
  q=request.GET.get('oauth_verifier', '')
  oauth_verifier =q.strip()
  if oauth_verifier:
   access_token_url = "https://api.twitter.com/oauth/access_token"
   token = oauth2.Token(oauth_token, oauth_token_secret)
   token.set_verifier(oauth_verifier)
   consumer = oauth2.Consumer(consumer_key,consumer_secret)
   client = oauth2.Client(consumer, token)
   resp, content = client.request(access_token_url, "POST")
   access_token = dict(urlparse.parse_qsl(content))
   twitter_access_token = access_token['oauth_token']
   twitter_access_token_secret = access_token['oauth_token_secret']
   userid = access_token['user_id']
   screenname = access_token['screen_name']
   load_url = "https://api.twitter.com/1.1/account/verify_credentials.json"  
   token1 = oauth2.Token(key=twitter_access_token, secret=twitter_access_token_secret)
   client2 = oauth2.Client(consumer, token1)
   resp1, content1 = client2.request(load_url)
   c=json.loads(content1)
   user_profile = Userprofile(userid=c['id'],username=c['name'],location=c['location'],language=c['lang'],Description=c['description'],screen_name=c['screen_name'])
   user_profile.save(using='twitter')
   return HttpResponse("<script type='text/javascript'>d=window.open('http://www.google.com','_self');d.close();</script>")
  else:
   return HttpResponse("<script type='text/javascript'>d=window.open('http://www.google.com','_self');d.close();</script>") 
  
  
   
      
   
   

        


