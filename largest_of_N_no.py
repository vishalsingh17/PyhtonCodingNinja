lst = input("Enter n numbers splitted by space: ").split(" ")

largest = float(lst[0])

for i in range(len(lst)):
  if float(lst[i]) > largest:
    largest = float(lst[i])
  else:
    continue

print(f"{largest} is largest")