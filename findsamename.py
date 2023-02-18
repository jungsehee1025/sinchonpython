def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))


def 짝(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(f'{a[i]} - {a[j]}')

name2 = ["Tom", "Jerry", "Mike"]
print(짝(name2))