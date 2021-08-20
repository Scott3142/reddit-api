import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('<CLIENT_ID>', '<SECRET_TOKEN>')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': '<USERNAME>',
        'password': '<PASSWORD>'}