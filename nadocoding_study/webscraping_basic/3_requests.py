import requests
res = requests.get("https://kimpga.com/")
res.raise_for_status()
# print("응답코드:", res.status_code)  # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다.[에러 코드", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mykimp.html", "w", encoding="utf8") as f:
    f.write(res.text)
