# 안테나
# 2019 SW 마에스트로 입학 테스트
# 2021.05.15. 
# LEE SEUNG JAE
#################################

N = int(input())

houses = list(map(int, input().split()))
houses.sort()

print(houses[int((N-1)/2)])
