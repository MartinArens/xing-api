#!/usr/bin/python3

from rauth import OAuth1Service
import json
import requests
import urllib3

xing = OAuth1Service(
    consumer_key='',
    consumer_secret='',
    request_token_url='https://api.xing.com/v1/request_token',
    access_token_url='https://api.xing.com/v1/access_token',
    authorize_url='https://api.xing.com/v1/authorize',
    base_url='https://api.xing.com/v1/'
    )

request_token, request_token_secret = xing.get_request_token(params={'oauth_callback':'nil'})

authorize_url = xing.get_authorize_url(request_token)

print('Visit this URL in your browser: ' + authorize_url)
pin = input('Enter PIN from the oauth_verifier field (last 4 digits in the redirect URL): ')
session = xing.get_auth_session(request_token,
                                    request_token_secret,
                                    method='POST',
                                    data={'oauth_verifier': pin})


response = session.get('/v1/users/me', header_auth=True)
profile_data = response.json()
for item in profile_data['users']:
    user_id = item['id']
    print('user id:', user_id)


response = session.get('/v1/users/' + user_id + '/visits', header_auth=True)
visits_data = response.json()
for item in visits_data['visits']:
    print(item['display_name'])



