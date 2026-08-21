# odd or even number
n=int(input("enter an number:"))
if n % 2==0:
    print("Even")
else:
   print("odd")

#largest of three num
n_1=int(input("enter an number for n_1:"))
n_2=int(input("enter an number for n_2:"))
n_3=int(input("enter an number for n_3:"))
if (n_1>n_2 and n_1>n_3):
   print("n_1 value is larger")
elif(n_2>n_3):
   print("n_2 value is larger")
else:
  print("n_3 value is larger")
 
#sum of digit
n=int(input("Enter a number: "))
sum = 0
while n > 0:
    #gives the last digit
    digit = n % 10
    sum=sum+digit
    #removes the last digit
    n = n // 10
print("Sum of digits:", sum)


#reverse an value
n=int(input("Enter a number: "))
reverse_number= 0
while n > 0:
     
    digit = n % 10
    reverse_number=(reverse_number*10)+digit
    n = n // 10
print("Reversed number:", reverse_number)

#factorial of number
n=int(input("enter the number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("factorial of an number is:",factorial)

#count the digits
n=int(input("enter the number:"))
digit= 0
while n > 0:
    num = n % 10
    digit=digit+1
    n = n // 10
print("the digits are:",digit)

#check palindrome or not
n=int(input("enter the value:"))
num=n
reverse_number=0
while n>0:
    digit=n%10
    reverse_number=(reverse_number*10)+digit
    n=n//10
if num==reverse_number:
    print("palinrdrome")
else:
    print("not an palindrome")

#largest element in list
numbers = [10, 25, 7, 45, 18]
max(numbers)
print(max(numbers))
#or
numbers = [10, 25, 7, 45, 18]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print("largest number is :",largest)
        
#smallest element in list
numbers = [10, 25, 7, 45, 18]
min(numbers)
print(min(numbers))
#or
numbers = [10, 25, 7, 45, 18]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print("smallest number is :",smallest)

#counting vowels in string
string=input("enter an string:")
count = 0 # count the vowels in the string
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count = count + 1
    else:
        print(i, "is not a vowel")
print("Number of vowels:", count)
