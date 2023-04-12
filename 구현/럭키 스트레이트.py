n = input()

l = len(n) // 2

sum_l = 0
sum_r = 0

for num in n[:l]:
    sum_l += int(num)
for num in n[l:]:
    sum_r += int(num)

if sum_l == sum_r:
    print("LUCKY")
else:
    print("READY")