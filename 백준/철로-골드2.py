import sys
import heapq

n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)
d = int(sys.stdin.readline())

roads = []
for road in road_info:
    a, b = road
    if abs(b - a) <= d:
        road.sort()
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
q = []
for road in roads:
    if not q:
        heapq.heappush(q, road)
    else:
        while q[0][0] < road[1] - d:
            heapq.heappop(q)
            if not q:
                break
        heapq.heappush(q, road)
    answer = max(answer, len(q))

print(answer)