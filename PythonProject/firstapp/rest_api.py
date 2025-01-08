import requests
url = 'http://127.0.0.1:8000/api/posts/'
# pas bon

headers = {'Authorization': 'Token c3ba7bf204ec287a296af02b7aadbdf32aaaf781'}
r = requests.get(url, headers=headers)
print (r.json())
