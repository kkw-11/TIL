import requests
res = requests.get("https://google.com")
res.raise_for_status() #응답여부 체크 코드

# print("status code: ",res.status_code)

# if res.status_code == requests.codes.ok:
#     print("success")
# else:
#     print("fail")

print(len(res.text))

with open("mygoogole.html","w",encoding="utf8") as f:
    f.write(res.text)