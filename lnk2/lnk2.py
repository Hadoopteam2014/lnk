import time

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from models import *

import json
import threading
import oauth2 as oauth
from linkedin import lnk2

import logging

# Get an instance of a logger
logger = logging.getLogger("sbutler")


SITE_URL = settings.SITE_URL

LINKEDIN_CONSUMER_KEY = settings.LINKEDIN_CONSUMER_KEY
LINKEDIN_CONSUMER_SECRET = settings.LINKEDIN_CONSUMER_SECRET
LINKEDIN_OAUTH_STEP1_URL = SITE_URL+"linkedin_oauth_step1/"
LINKEDIN_OAUTH_STEP2_URL = SITE_URL+"linkedin_oauth_step2/"
LINKEDIN_SEARCH_STRING = "http://api.linkedin.com/v1/people-search:(people:(id,headline,first-name,last-name,location:(name),num-connections,specialties,interests,positions,skills,educations,twitter-accounts,phone-numbers,main-address,picture-url,public-profile-url,date-of-birth,last-modified-timestamp,relation-to-viewer,num-recommenders,recommendations-received,following,job-bookmarks,group-memberships,related-profile-views,languages),num-results)?start=1&count="+str(settings.LINKEDIN_SEARCH_COUNT)+"&network=S&format=json"
LINKEDIN_CONNECTION_STRING = "http://api.linkedin.com/v1/people/~/connections:(id,headline,first-name,last-name,location:(name),num-connections,specialties,interests,positions,skills,educations,twitter-accounts,phone-numbers,main-address,picture-url,public-profile-url,date-of-birth,last-modified-timestamp,relation-to-viewer,num-recommenders,recommendations-received,following,job-bookmarks,group-memberships,related-profile-views,languages)?format=json&count=" + str(settings.LINKEDIN_CONN_COUNT)

li_thread_lock = threading.Lock()

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

content = get_linkedin_data_old(request, dos, access_token, access_token_secret)

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
