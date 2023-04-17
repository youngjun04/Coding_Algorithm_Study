import sys
string = sys.stdin.readline().rstrip()

string = string.upper()
string_list = list(set(string))

cnt = []
for i in range(len(string_list)):
    cnt.append(list(string).count(string_list[i]))
Max = max(cnt)
if cnt.count(Max) != 1:
    print("?")
else:
    print(string_list[cnt.index(Max)])