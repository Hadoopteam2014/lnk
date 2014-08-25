from django.http import HttpResponse
import urllib2
import urllib
import time
import requests
from urlparse import urlparse
import oauth2 as oauth
import urlparse
from linkedin import linkedin
from lnkdin.models import project
import json
import webbrowser
consumer_key = "75nanr9qwylt2d"
consumer_secret = "UpORpgoDH1iUl2kL"
authorize=True
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
request_token = dict(urlparse.parse_qsl(content))
oauth_token=request_token['oauth_token']
oauth_token_secret =request_token['oauth_token_secret']
fopen=open('jsp.js','rb')
a=fopen.readline()
b=a.replace('myvar',oauth_token)
def index1(request):
 return HttpResponse(b)
def index(request): 
  q=request.GET.get('oauth_verifier', 'refused')
  oauth_verifier =q
  if oauth_verifier:
   access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
   token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
   token.set_verifier(oauth_verifier)
   client = oauth.Client(consumer, token)
   resp, content = client.request(access_token_url, "POST") 
   q1=content.replace('&',',')
   q2=q1.split('=')
   q3=q2[1].split(',')
   q4=q2[2].split(',')
   USER_TOKEN=q3[0]
   USER_SECRET=q4[0]
   RETURN_URL = 'http://119.82.102.117:8000/lkdn/'
   auth = linkedin.LinkedInDeveloperAuthentication(consumer_key,
   consumer_secret,USER_TOKEN,USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())
   app = linkedin.LinkedInApplication(auth)
   x = app.get_profile(selectors=['id', 'firstName', 'lastName', 'location', 'distance', 'numConnections',  'skills', 'educations'])
   ky=x.keys()
   count=0
   for i in range(len(ky)):
     if ky[i]=="skills":
         count=1
         break
   if count!=1:
     updat_dict={'skills':"null"}
     x.update(updat_dict)
   for i in range(len(ky)):
     if ky[i]=="educations":
         count=1
         break
   if count!=1:
     updat_dict={'educations':"null"}
     x.update(updat_dict)
   for i in range(len(ky)):
     if ky[i]=="location":
         count=1
         break
   if count!=1:
     updat_dict={'location':"null"}
     x.update(updat_dict)
   for i in range(len(ky)):
     if ky[i]=="distance":
         count=1
         break
   if count!=1:
      updat_dict={'distance':"null"}
      x.update(updat_dict)
   y = project(firstname = x['firstName'], lastname = x['lastName'], ids = x['id'], location = x['location'], skills = x['skills'], 
   distance =x['distance'], numconnections = x['numConnections'], educations = x['educations'])
   y.save(using='linkedin')
   return HttpResponse("<script type='text/javascript'>d=window.open('http://www.google.com','_self');d.close();</script>")


