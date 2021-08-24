# 국영수
# acmicpc 10825 (baekjoon)
# LEE SEUNG JAE
# 2021.05.05
#################################
import sys

N = sys.stdin.readline()

students = []
for _ in range(int(N)):
	name, guk, young, soo = sys.stdin.readline().split()
#	name2int = sum([ord(n) for n in name])
#	students.append([name, name2int/1221 - int(guk)*101*101 + int(young)*101 - int(soo)])
	students.append((name, int(guk), int(young), int(soo)))

sort_1 = sorted(students, key=lambda x:(-x[1],x[2],-x[3],x[0]))
for student in sort_1:
	print(student[0])
