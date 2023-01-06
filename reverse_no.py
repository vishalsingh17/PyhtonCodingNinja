n = int(input("Enter a no: "))
# 123 -> 321
temp = n
rev_n = 0

while temp > 0:
    last_digit = temp % 10
    temp = temp// 10
    rev_n = rev_n*10 + last_digit
print(rev_n)