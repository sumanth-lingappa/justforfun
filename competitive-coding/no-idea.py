# Enter your code here. Read input from STDIN. Print output to STDOUT
lenn, lenm = map(int, input().split())

arr = [map(int, input().split())]
arrA = [map(int, input().split())]
arrB = [map(int, input().split())]


print(lenn, lenm, arr, arrA, arrB)

happiness = 0

for integer in arr:
    if integer in arrA:
        happiness += 1
    elif integer in arrB:
        happiness -= 1

print(happiness)

