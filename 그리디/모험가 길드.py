n = int(input())
people = list(map(int, input().split()))

people.sort()

count = 0
group = []

for person in people:
    group.append(person)
    if max(group) <= len(group):
        count += 1
        group = []

print(count)