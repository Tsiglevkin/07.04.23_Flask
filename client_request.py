import requests

# base_url = 'http://127.0.0.1:5000'
#
# response_get = requests.get('http://127.0.0.1:5000/users/6')
#
#
# print(response_get.status_code)
# print(response_get.json())


response_post = requests.post(
    'http://127.0.0.1:5000/users/',
    json={
        'name': 'Ivan',
        'user_pass': '12345kiojoi'
    }
)


print(response_post.status_code)
print(response_post.json())

# response = requests.get(url=f'{base_url}/hello/')
# print(response.status_code)
# print(response.text)


