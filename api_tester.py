import requests

# url = 'http://packagerat.pythonanywhere.com/packages/'
#
# package_data = [{
#
#     'recipient': 1,
#     'apartment_no': '309',
#     'package_type': 'small',
#     'status': 'pending'
# }]
#
# r = requests.post(url, json = package_data)
# print(r.text)

# url = 'http://parrotapp.pythonanywhere.com/maintenance/'
#
# data = {
#
#     'description': 'Bada Boom',
#     'apartment_no': 309
# }
#
# r = requests.post(url, json = data)
# print(r.text)

# url2 = 'http://parrotapp.pythonanywhere.com/maintenance/parse_text/'
#
# data2 = {
#
#     'query': "My toilet won't flush"
# }
#
# r = requests.post(url2, json = data2)
# print(r.text)

# url2 = 'http://parrotapp.pythonanywhere.com/login/'
#
# data2 = {
#
#     'username': 'kdenny',
#     'password': 'P@rr0t@pp'
# }
#
# r = requests.post(url2, json=data2)
# print(r.text)

url3 = 'http://parrotapp.pythonanywhere.com/get_username/'

headers = {'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImtkZW5ueSIsInVzZXJfaWQiOjUsImVtYWlsIjoiIiwiZXhwIjoxNTEzNjUzNjk5fQ.NAe7g16IOVAUImtu3Xc2vE1u097EdzfVv27_PO7nL6E'}

r = requests.get(url3, headers=headers)
print(r.text)