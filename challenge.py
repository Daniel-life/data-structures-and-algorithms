# Daniel Cheong Jun Jie, 200157E, Group 1
from time import perf_counter

start_time = perf_counter()


def factor(factors, Z):
    for i in range(2, Z + 1):
        if Z % i == 0:
            f = int(Z / i)
            factors.append(f)

    factors.reverse()


def binary_search(SEQ, f):
    low = 0
    high = len(SEQ) - 1

    while low <= high:
        mid = (high + low) // 2

        if SEQ[mid] == f:
            return mid

        elif f < SEQ[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


SEQ = [2, 3, 4, 5, 12, 15, 20, 24, 25, 30, 40, 60]
factors = []
status = " "
Z = int(input("What's your target value? "))
factor(factors, Z)
compare = []

for i in factors:
    if binary_search(SEQ, i) == -1:
        pass
    else:
        compare.append(i)
        status = "found"
count = 0
if status == "found":
    for count, i in enumerate(compare):
        count += 1
        print("X={}, Y={}, Z={}".format(i, Z, Z))
    print("Total match is {}".format(count))
else:
    print("X=not found, Y=not found, Z={}".format(Z))
    print("Total match is {}".format(count))
end_time = perf_counter()
print(end_time, start_time)
print("Elapsed time during the whole program in seconds:",
      end_time - start_time)
