# re: 정규식
import re

# 매칭

p = re.compile(("ca.e"))
# . (ca.e)  : 하나의 문자를 의미 > care,cafe(o) | caffe (x)
# ^ (^de)   : 문자열의 시작 > desk, destina(o)  | fade  (x)
# $ (se$)   : 문자열의 끝 > case, base(o)       | face  (x)


def print_match(m):
    if m:
        print("m.group", m.group())    # 일치하는 문자열 반환
        print("m.string", m.string)   # 입력받은 문자열
        print("m.start", m.start())    # 일치하는 문자열의 시작 index
        print("m.end", m.end())      # 일치하는 문자열의 끝 index
        print("m.span", m.span())     # 일치하는 문자열의 시작 index

    else:
        print("매칭되지 않음")


print("# match: 매치 되면 값 반환,매치 되지않으면 에러 발생")
m = p.match("cafe")
print_match(m)

print("# search: 주어진 문자열 중에 일치하는게 있는지 확인")
m = p.search("careless")
print_match(m)

print("# findall: 일치하는 모든 것을 리스트 형태로 표시")
lst = p.findall("good care cafe")
print(lst)


# 정리:
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열"): 일치하는 모든것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e)  : 하나의 문자를 의미 > care,cafe(o) | caffe (x)
# ^ (^de)   : 문자열의 시작 > desk, destina(o)  | fade  (x)
# $ (se$)   : 문자열의 끝 > case, base(o)       | face  (x)


# .startswith(): xx로 시작하는 element 찾기
# https://search4.kakaochd.net/argon/130x130 으로 url 완성하기
images_url = "//search4.kakaochd.net/argon/130x130"
for image in images_url:
    if image_url.startswith("//"):  # 시작 문단에 "//"가 잇는문단 만찾느다
        image_url = "https:" + image_url
