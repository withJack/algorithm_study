# 럭키 스트레이트
# acmicpc 18406 (baekjoon)
# LEE SEUNG JAE
# 2021.05.05
#################################

N = input()
N = list(N)
N_len = len(N)

sum1 = 0
sum2 = 0
for i in range(int(N_len/2)):
	sum1 += int(N[i])
	sum2 += int(N[N_len-i-1])
if sum1 == sum2:
	print("LUCKY")
else:
	print("READY")