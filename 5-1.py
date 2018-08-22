# 텍스트 파일 쓰기
with open('somefile.txt', "wt") as f:
    f.write(text1)

# 파일 전체를 하나의 문자열로 읽음
with open('somefile.txt', 'rt') as f:
    data = f.read()
    
