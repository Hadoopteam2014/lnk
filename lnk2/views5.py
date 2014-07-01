from linkedin_json_client.api import LinkedInJsonAPI
from urllib import urlencode
from linkedin_json_client.constants import LinkedInScope
from linkedin_json_client.constants import BasicProfileFields, BasicProfileSelectors
from lnkdin2 import UserProfile2


CONSUMER_KEY = '75nanr9qwylt2d'
CONSUMER_SECRET = 'UpORpgoDH1iUl2kL'
li_client = LinkedInJsonAPI(CONSUMER_KEY, CONSUMER_SECRET)

try:
    request_token_dict = li_client.get_request_token(scope=[LinkedInScope.BASIC_PROFILE, LinkedInScope.EMAIL_ADDRESS])
    url = '%s?%s' % (li_client.authorize_path, urlencode(request_token_dict))
    # store your request token in the user session for use in callback
    request.session['li_request_token'] = request_token_dict
    # REDIRECT USER TO url
except (HTTPError, socket.error):
    # failed to connect to LinkedIn, handle this in your application
oauth_verifier = request.GET.get('oauth_verifier')
request_token = request.session.get('li_request_token')
 
oauth_problem = request.GET.get('oauth_problem')
if oauth_problem or request_token is None:
    if oauth_problem == 'user_refused':
        # user refused auth, handle in your application
    # some other problem, handle in your application
else:
    access_token = li_client.get_access_token(request_token, oauth_verifier)
    # user successfully authorized, store this access_token and associate with the user for use with API

try:
    json_object = linkdin2.UserProfile(access_token, [UserProfile2.firstname, UserProfile2.lastname, UserProfile2.cid])
 
    json_object[UserProfile2.cid]
    json_object[UserProfile2.firstname]
    json_object[UserProfile2.lastname]
except LinkedInApiJsonClientError, e:
    print e
