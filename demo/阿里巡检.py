import requests
url = 'http://api3.zzx9.cn/api/send'

payload = {"id":"908493",
           "sequenceNumber":"30001541126680553",
           "sign":"369d7e237e42468835e95158484adade",
           "timestamp":"1541126680883",
           "userNumber":"13260276178",
           "username":"bufatest"}
headers = {'Content-Type': "application/json"}
response = requests.post(url,data=payload,headers=headers)
print(response.text)