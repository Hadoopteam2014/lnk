from django.http import HttpResponse
import urllib2
import urllib
import requests
import oauth2 as oauth
import urlparse
from linkedin import linkedin
from viewer.models import project
import json
import webbrowser
consumer_key           = '75nanr9qwylt2d'
consumer_secret        = 'UpORpgoDH1iUl2kL'
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
request_token = dict(urlparse.parse_qsl(content))
oauth_token=request_token['oauth_token']
oauth_token_secret =request_token['oauth_token_secret']
def index(request):
   authorize_url ='https://api.linkedin.com/uas/oauth/authorize'
   a= "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
   b=webbrowser.open(a,new=0, autoraise=True)
   q=request.GET.get('oauth_verifier', '')
   oauth_verifier =q
   access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
   token = oauth.Token(request_token['oauth_token'],request_token['oauth_token_secret'])
   token.set_verifier(oauth_verifier)
   client = oauth.Client(consumer, token)
   resp, content = client.request(access_token_url, "POST")
   access_token = dict(urlparse.parse_qsl(content))
   oauth_token=access_token['oauth_token']
   oauth_secret=access_token['oauth_token_secret']
   #CONSUMER_KEY = '75wj4ollfp313d'
   #CONSUMER_SECRET = 'Z23HCUOiRwN1oJ4T'
   USER_TOKEN = oauth_token
   USER_SECRET = oauth_secret
   RETURN_URL = 'http://127.0.0.1:8000/lkdn/'
   auth = linkedin.LinkedInDeveloperAuthentication(consumer_key,
   consumer_secret,USER_TOKEN,USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())
   app = linkedin.LinkedInApplication(auth)
   x = app.get_profile(selectors=['id', 'firstName', 'lastName', 'location', 'numConnections',
'skills','educations','phoneNumbers','emailAddress'])
   '''y = project(firstname = x['firstName'], lastname = x['lastName'], ids = x['id'], location = x['location'], skills = x['skills'], 
        numconnections = x['numConnections'], educations = x['educations'], phoneNumbers = x['phoneNumbers'],emailAddress = x['emailAddress'])
   for n in y:
       if location == "":
           break
       if skills == "":
           break
       if education == "":
           break
       if emailAddress == "":
           break
       if phoneNumbers == "":
           break
             
   n.save()'''
   return HttpResponse(x.keys)
