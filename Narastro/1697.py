# 2021.05.21. Baekjoon algorithm problem #1697
# 숨바꼭질

import sys, collections
input = sys.stdin.readline

N,K = map(int,input().split())

# BFS 함수
def bfs(N,K):
    visit = []      # 방문 표시를 위한 리스트
    Q = collections.deque()     # 큐를 데크자료형을 이용해 선언
    
    Q.append(N)
    visit.append(N)
    time = -1           # 0초부터 시작하기 위해 -1을 초기값으로 설정

    while Q:
        Q_l = len(Q)
        time += 1
        while Q_l!=0:
            Q_l -= 1
            v = Q.popleft()
            if v == K:
                return time
            for next_v in [v-1,v+1,v*2]:
                if next_v >= 0 and next_v not in visit and next_v<100001:
                    visit.append(next_v)
                    Q.append(next_v)

print(bfs(N,K))
# 테스트


