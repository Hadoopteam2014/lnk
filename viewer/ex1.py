import oauth2 as oauth
import httplib2
import time, os, simplejson
 
# Fill the keys and secrets you retrieved after registering your app

consumer_key  = '75wj4ollfp313d'
consumer_secret = 'Z23HCUOiRwN1oJ4T'
user_token  = '75--b97ba2e6-920b-4fbf-ae92-95097511c9a2'
user_secret = 'f96e3a63-5de4-445d-927e-76bef8fa31b6'
 
# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)
 
# Use the consumer object to initialize the client object
client = oauth.Client(consumer)
 
# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
            key=user_token,
            secret=user_secret)
 
client = oauth.Client(consumer, access_token)
 
# Make call to LinkedIn to retrieve your own profile
resp,content = client.request("http://api.linkedin.com/v1/people/~", "GET", "")
 
# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
# resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")


from linkedin import linkedin
from viewer.models import view
import json
import oauth2 as oauth
import time

url = "http://api.linkedin.com/v1/people/~"

consumer = oauth.Consumer(
     key="75wj4ollfp313d",
     secret="Z23HCUOiRwN1oJ4T")
     
token = oauth.Token(
     key="f02dba89-516c-43eb-9d95-78f9b713b729", 
     secret="600b205a-c58c-4610-ba2d-f81901b3098e")


client = oauth.Client(consumer, token)

resp, content = client.request(url)
print resp
print content
