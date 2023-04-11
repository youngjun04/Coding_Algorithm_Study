s = input()
numbers = []
for number in s:
    numbers.append(int(number))

result = numbers[0]

for number in numbers[1:]:
    if number == 0 or number == 1 or result == 0:
        result += number
    else:
        result *= number

print(result)