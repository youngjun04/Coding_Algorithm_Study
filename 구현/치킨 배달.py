from itertools import combinations

n, m = map(int, input().split())
city = []
house = []
chickens = []
for _ in range(n):
    city.append(list(map(int, input().split())))
    
for i in range(len(city)):
    for j in range(len(city[0])):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

min_len = int(1e9)
for i in range(1, m + 1):
    remain = list(combinations(chickens, i))
    for methods in remain:
        length = 0
        for home in house:
            c, d = home
            chicken_len = int(1e9)
            for chicken in methods:
                a, b = chicken
                temp_len = abs(a - c) + abs(b - d)
                chicken_len = min(chicken_len, temp_len)
            length += chicken_len
        min_len = min(min_len, length)

    
print(min_len)