w = input().upper()
w_list = list(set(w))

cnt =[]
for i in w_list:
    count = w.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(w_list[(cnt.index(max(cnt)))])