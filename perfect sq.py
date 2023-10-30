a=int(input("Enter the lower limit"))
b=int(input("Enter the upper limit"))
result_list = [num for num in range(a,b+1)
               if all(int(digit) % 2 == 0 for digit in str(num))
               and int(num**0.5)**2 == num]
print(result_list)