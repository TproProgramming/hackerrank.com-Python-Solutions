set_a = set(map(int, input().split()))
n = int(input()) #number of other sets

is_strict_subset = True
for i in range(n):
    temp_set = set(map(int, input().split()))
    if (set_a.issuperset(temp_set) and len(set_a) > len(temp_set)): #a is strict superset
        continue
    else:
        is_strict_subset = False

print(is_strict_subset)