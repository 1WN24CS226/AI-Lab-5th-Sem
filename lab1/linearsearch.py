arr = []
n = int(input("Enter length: "))
print("Enter Elements: \n")

for i in range(n):
    arr.append(int(input()))

key = int(input("Enter search element: "))

if key in arr:
    print("Element found")
else:
    print("Element not found")