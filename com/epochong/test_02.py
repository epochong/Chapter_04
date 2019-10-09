s = "I and si si"
arr = s.split()
for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        arr[i] = ""
res = " ".join(" ".join(arr).split())
print(res)