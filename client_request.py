import requests

base_url = 'http://127.0.0.1:5000'

# response_get = requests.get(base_url)
# r = 1  # для постановки breakpoint

response_post = requests.post(
    'http://127.0.0.1:5000/users/',
    json={
        'name': 'Stepan',
        'user_pass': '12345dsad'
    }
)
print(response_post.status_code)
print(response_post.text)



