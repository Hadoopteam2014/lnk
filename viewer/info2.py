from linkedin import linkedin
from viewer.models import view
import json

CONSUMER_KEY = '75nanr9qwylt2d'
CONSUMER_SECRET = 'UpORpgoDH1iUl2kL'
USER_TOKEN = 'bacbf94e-ab93-4175-8b41-f3f904036419'
USER_SECRET = 'c815953e-1251-4299-8937-60802dc85fc8'

RETURN_URL = ' http://127.0.0.1:8000/''http://127.0.0.1:8000/lkdn/'
auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY,
CONSUMER_SECRET,USER_TOKEN,USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())
app = linkedin.LinkedInApplication(auth)

authentication = linkedin.LinkedInAuthentication(CONSUMER_KEY, CONSUMER_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)


__all__ = ['LinkedInAuthentication', 'LinkedInApplication', 'PERMISSIONS']

PERMISSIONS = enum('Permission',
                        BASIC_PROFILE='r_basicprofile',
                        FULL_PROFILE='r_fullprofile',
                        EMAIL_ADDRESS='r_emailaddress',
                        NETWORK='r_network',
                        CONTACT_INFO='r_contactinfo',
                        NETWORK_UPDATES='rw_nus',
                        GROUPS='rw_groups',
                        MESSAGES='w_messages')


ENDPOINTS = enum('LinkedInURL',
                      PEOPLE='https://api.linkedin.com/v1/people',
                      PEOPLE_SEARCH='https://api.linkedin.com/v1/people-search',
                      GROUPS='https://api.linkedin.com/v1/groups',
                      POSTS='https://api.linkedin.com/v1/posts',
                      COMPANIES='https://api.linkedin.com/v1/companies',
                      COMPANY_SEARCH='https://api.linkedin.com/v1/company-search',
                      JOBS='https://api.linkedin.com/v1/jobs',
                      JOB_SEARCH='https://api.linkedin.com/v1/job-search')


NETWORK_UPDATES = enum('NetworkUpdate',
                            APPLICATION='APPS',
                            COMPANY='CMPY',
                            CONNECTION='CONN',
                            JOB='JOBS',
                            GROUP='JGRP',
                            PICTURE='PICT',
                            EXTENDED_PROFILE='PRFX',
                            CHANGED_PROFILE='PRFU',
                            SHARED='SHAR',
                            VIRAL='VIRL')


#app.get_profile()
# data = app.get_profile()
# c= (data.get_profile())
#a = data['firstName']
#b = data['lastName']

x = app.get_profile()
application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
y = view(firstname = x['firstName'], lastname = x['lastName'], ids = x['id'], location = x['location'], skills = x['skills'])
y.save()
'''data = app.get_profile()
a = data['firstName']

y = linked(firstname=a)
y.save()'''

