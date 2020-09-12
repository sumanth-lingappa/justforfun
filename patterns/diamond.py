n = int(input("Enter an odd number: "))

if n % 2 != 1:
    print("Entered number is not ODD number. Exiting..")
    exit()

pattern = "*"

for i in range(1, n + 1, 2):
    print(f"{pattern*i:^{n}}")

for i in range(n - 2, 0, -2):
    print(f"{pattern*i:^{n}}")
