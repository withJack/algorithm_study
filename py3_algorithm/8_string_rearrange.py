# 문자열 재정렬
# Facebook Interview
# 2021.05.15. 
# LEE SEUNG JAE
#################################

input_ = input()

string = []
num = 0
for char in input_:
    if 'A' <= char <= 'Z':
        string.append(char)
    else:
        num += int(char)

print("".join(sorted(string)+[str(num)]))
