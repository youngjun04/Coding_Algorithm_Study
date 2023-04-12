s = input()
alphas = []
total = 0

for word in s:
    if word.isalpha():
        alphas.append(word)
    else:
        total += int(word)

alphas.sort(key = lambda x: ord(x))

answer = ""
for alpha in alphas:
    answer += alpha
answer += str(total)
print(answer)