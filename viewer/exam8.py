import oauth2 as oauth
import urlparse 
import time

 
consumer_key           = "75nanr9qwylt2d"
consumer_secret        = "UpORpgoDH1iUl2kL"
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)
request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])
 
request_token = dict(urlparse.parse_qsl(content))

print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']

authorize_url =      'https://api.linkedin.com/uas/oauth/authorize'
print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print

access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret']

client = oauth.Client(consumer, token)
 
resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))
 
print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']


url = "http://api.linkedin.com/v1/people/~"

consumer = oauth.Consumer(
     key="CONSUMER_KEY",
     secret="CONSUMER_SECRET")
     
token = oauth.Token(
     key="OAUTH_TOKEN", 
     secret="OAUTH_TOKEN_SECRET")


client = oauth.Client(consumer, token)

resp, content = client.request(url)
print resp
print content

