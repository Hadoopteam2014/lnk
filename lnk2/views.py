# Python
import oauth2 as oauth
import cgi
import simplejson as json
import datetime
import re

# Django
#from django.http import HttpResponse
#from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
#from django.conf import settings
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

# Project
from lnk2.models import UserProfile

# from settings.py
consumer = oauth.Consumer(settings.LINKEDIN_TOKEN, settings.LINKEDIN_SECRET)
client = oauth.Client(consumer)
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
authenticate_url = 'https://www.linkedin.com/uas/oauth/authenticate'

SITE_URL = settings.SITE_URL

LINKEDIN_CONSUMER_KEY = settings.LINKEDIN_CONSUMER_KEY
LINKEDIN_CONSUMER_SECRET = settings.LINKEDIN_CONSUMER_SECRET
LINKEDIN_OAUTH_STEP1_URL = SITE_URL+"linkedin_oauth_step1/"
LINKEDIN_OAUTH_STEP2_URL = SITE_URL+"linkedin_oauth_step2/"


def load_linkedin(request, dos):
# print "DOS", dos
    if request.user.is_authenticated():
        print "User is logged into SB"
    else:
        return HttpResponse("You are not logged in! <a href='/accounts/login/'>Login</a>")

#check if the authentication tokens are in session, if not call oath handshake
    if is_linkedin_authorized(request) is False:
      #store this url in session
      # print "Storing RedirectURL after OAuth: ", request.path
        request.session["session_linkedin_oauth_callingurl"] = "http://" + request.get_host() + request.path

       #redirect to HTTP oath step1
    return HttpResponseRedirect(LINKEDIN_OAUTH_STEP1_URL)

access_token = request.session.get("session_linkedin_access_token")
access_token_secret = request.session.get("session_linkedin_access_token_secret")
# print "Access Token", access_token, "DOS ", dos
# print "Access Token Secret", access_token_secret, "DOS ", dos

def is_linkedin_authorized(request):
    oauth_acccess_token = request.session.get("session_linkedin_access_token")
    oauth_acccess_token_secret = request.session.get("session_linkedin_access_token_secret")

    if (oauth_acccess_token is not None) and (oauth_acccess_token_secret is not None):
	return True
    else:
	return False

def linkedin_oauth_step1(request):
    api = linkedin.LinkedIn(LINKEDIN_CONSUMER_KEY, LINKEDIN_CONSUMER_SECRET, LINKEDIN_OAUTH_STEP2_URL)
    result = api.request_token()
    request.session["session_linkedin_request_token_secret"] = api._request_token_secret
    redirectURL = api.get_authorize_url(request_token = api._request_token)
 
    return HttpResponseRedirect(redirectURL)


def linkedin_oauth_step2(request):
    oauth_token_1 = request.GET['oauth_token']
    oauth_verifier_1 = request.GET['oauth_verifier']

    request.session["session_linkedin_oauth_token"] = oauth_token_1
    request.session["session_linkedin_oauth_verifier"] = oauth_verifier_1

    rts_session = request.session.get("session_linkedin_request_token_secret")
    DUMMY_CALLBACK_URL = SITE_URL

    api = linkedin.LinkedIn(LINKEDIN_CONSUMER_KEY, LINKEDIN_CONSUMER_SECRET, DUMMY_CALLBACK_URL)

    result = api.access_token(request_token = oauth_token_1, request_token_secret = rts_session, verifier = oauth_verifier_1)

    request.session["session_linkedin_access_token"] = api._access_token
    request.session["session_linkedin_access_token_secret"] = api._access_token_secret
    redirectURL = request.session.get("session_linkedin_oauth_callingurl")
    return HttpResponseRedirect(redirectURL)
