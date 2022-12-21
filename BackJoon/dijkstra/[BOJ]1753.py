
"""
1. 아이디어
- 한점시작, 모든 거리 : dijkstra
- 간선을 인접리스트 저장
- 거리배열 무한대 초기화
- 시작점 : 거리배열 0, 힙에 넣어주기
- 힙에서 빼면서 다음 것들을 수행
    - 최신 값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신

2. 시간복잡도
- dijkstra : O(ElogV)
    - E : 3e5
    - V : 2e4, logV ~= 20
    - ElogV = 6e6 > 가능 (2억보다 작음)
3. 자료구조
- 힙 : (비용, 노드번호)
- 거리 배열 : 비용 : int[]
- 간선 저장, 인접리스트 : (비용, 노드번호)[]
"""
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
edge = [ [] for _ in range(V+1)]
dist = [INF] * (V+1)
for i in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([w, v])

# 시작점 초기화
dist[K] = 0
heap = [[0,K]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])