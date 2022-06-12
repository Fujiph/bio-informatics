num1 = 4718
num2 = 9662

ans = [total for total in range(num1,num2+1) if total%2 != 0 ]
print(sum(ans))