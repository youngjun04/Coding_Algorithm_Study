n = int(input())
bundles = []
for _ in range(n):
    bundles.append(int(input()))

bundles.sort()
total = bundles[0] + bundles[1]
for i in range(2, len(bundles)):
    total += total + bundles[i]
print(total)