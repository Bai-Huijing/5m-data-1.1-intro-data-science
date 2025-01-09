def Fizz_Buzz(x):
    if x%3==0 and x%5==0:
        return "Fizz_Buzz"
    elif x%3==0:
        return "Fizz"
    elif x%5==0:
        return "Buzz"
    else:
        print(x)
print (Fizz_Buzz(3))
print (Fizz_Buzz(5))
print (Fizz_Buzz(15))