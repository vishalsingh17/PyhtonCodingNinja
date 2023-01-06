# from math import sqrt

# n = int(input("Enter a no: "))

# if n == 1:
#     print("1 is neither prime not composite")
# elif n == 2:
#     print("2 is the only prime no")
# elif n % 2 == 0:
#     print(f"{n} is not prime")
# else:
#     for i in range(2, int(sqrt(n))+1):
#         if n%i == 0:
#             print(f"{n} is not prime")
#             break
#     else:
#         print(f"{n} is prime")


n = int(input("Enter a no: "))

m = 2
while m <= n:
    d = 2
    flag = False
    while d < m:
        if m % d == 0:
            flag = True
        d = d + 1
    
    if flag == False:
        print(f"{m} is prime")

    m = m+1