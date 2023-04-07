import requests

base_url = 'http://127.0.0.1:5000/'

response_get = requests.get(base_url)

response_post = requests.post(
    base_url,
    json={
        'name': 'Stepan',
        'user_pass': '12345dsad'
    }
)
r = 1


