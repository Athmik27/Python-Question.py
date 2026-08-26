#armstrong number
n=int(input("enter an number:"))
num=0
while (n>0):
    digit=n%10
    num=num+digit ** 3
    n=n//10
print("armstrong number is:",num)
value=n #check whether the value is armstong or no.
if num==value:
    print("its armstrong")
else:
    print("not an armstrong")

#string reversing
def Rev_str(text):
    for i in range(len(text)-1,-1,-1):
        yield text[i]
for i in Rev_str("Manipal"):
    print(i)

#or
def Rev_str():
    text=input("enter an string:")
    for i in range(len(text)-1,-1,-1):
        yield text[i]
for i in Rev_str():
    print(i)

#remove the duplicate value from the list
list_1=[1,2,2,3,4,4,5]
list_2=[]
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)

#second largest number in list
numbers = [10, 25, 7, 45, 18]
largest=numbers[0]
second_largest=numbers[0]
for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i
    elif(i>second_largest):
        second_largest=i
print("second largest number is :",second_largest)

#second smallest number in list
numbers=[10,25,7,45,18]
smallest=numbers[0]
second_smallest=numbers[0]
for i in numbers:
    if i<smallest:
        second_smallest=smallest
        smallest=i
    elif(i<second_smallest):
        second_smallest=i
print('second smallest number is:',second_smallest)

#count how many positive numbers, negative numbers, and zeros are present in a list.
list_1=[10, -5, 0, 8, -2, 0, 7]
positive_value=0
negative_value=0
null_value=0
for i in list_1:
    if i>0:
        positive_value=positive_value+1
       
    elif i<0:
            negative_value=negative_value+1
            
    else:
            null_value=null_value+1    
            
print("number of positive value:",positive_value)
print("number of negative value:",negative_value)
print("number of null value:",null_value)


#sum of an list
list_1=[10, 20, 30, 40]
sum=0
for i in list_1:
    if i>0:
      sum=sum+i
print("sum:",sum)  

#average element in list
list_1=[10, 20, 30, 40]
count=0
sum=0
for i in list_1:
    sum=sum+i
    count=count+1
average=sum/count
print("sum:",sum)
print('average number is:',average)

# #largest and smallest in list
list_1=[10, 25, 7, 45, 18]
largest=list_1[0]
smallest=list_1[0]
for i in list_1:
    if i>largest:
        largest=i
    if i<smallest:
            smallest=i

print("largest value is:",largest)
print("smallest value is:",smallest)

#seperate even and odd
list_1=[1, 2, 3, 4, 5, 6]
list_even=[]
list_odd=[]
for i in list_1:
    if i % 2==0:
        list_even.append(i)
    else:
        list_odd.append(i)
print("even numbers are:",list_even)
print("odd numbers are:",list_odd)

# #Reverse a list
numbers = [10, 20, 30, 40, 50]
rev_num=[]
for i in numbers:
    rev_num.insert(0,i)
print("reversed number is:",rev_num)

#sum of all the elements
numbers = [10, 20, 30, 40, 50]
total=0
for i in numbers:
    total=total+i
print('sum of the element:',total)

# count numbers of even in list
numbers = [10, 15, 20, 25, 30, 35, 40]
count=0
for i in numbers:
    if i%2==0:
        count=count+1
print("numbers of even are in:",count)


# # count numbers of odd in list
numbers = [10, 15, 20, 25, 30, 35, 40]
count=0
for i in numbers:
    if i%2!=0:
        count=count+1
print("numbers of odd are in:",count)

#count number of even and odd
numbers = [10, 15, 20, 25, 30, 35, 40]
odd=[]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else :
        odd.append(i)
print("even",even)
print("odd",odd)

#largest in list
numbers = [10, 25, 7, 45, 18]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print("largest number is :",largest)

#smallest in list
numbers = [10, 25, 7, 45, 18]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print("smallest number is :",smallest)

#number of positive number
numbers = [-5, 10, -2, 20, 0, 15, -8]
count=0
for i in numbers:
    if i>0:
        count=count+1
print("number of positive numbers:",count)

# #number of negative number
numbers = [-5, 10, -2, 20, 0, 15, -8]
count=0
for i in numbers:
    if i<0:
        count=count+1
print("number of negative numbers:",count)

#square of numbers
numbers = [1, 2, 3, 4, 5]
sq_num=[]
for i in numbers:
    i=i**2
    sq_num.append(i)
print('square of numbers:',sq_num)

# #number greater than 20
numbers = [10, 25, 15, 30, 8, 45]
num_list=[]
for i in numbers:
    if i>20:
        num_list.append(i)
print("number grater than 20 is :",num_list)

# #finding the num in list
numbers = [10, 20, 30, 40, 50]
num=int(input("enter the number you want to find:"))
for i in numbers:
    if i==num:
        print("number found in list",num)

#remove the duplicate from list
numbers = [10, 20, 10, 30, 20, 40, 30]
new_numbers=[]
for i in numbers:
    if i not in new_numbers: #not in operator is imp
        new_numbers.append(i)
print("new numbers from the original list is:",new_numbers)

#finding second largest numbers
numbers = [10, 25, 7, 45, 18]
largest=numbers[0]
second_largest=numbers[0]
for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest:
        second_largest=i
print("second largest number is:",second_largest)

#frequency checking
numbers = [5, 10, 15, 10, 20]
count = 0
for i in numbers:
    if i==10:
        count=count+1

 print("10 occurs:", count, "times")

#Sum of only even numbers
numbers = [10, 15, 20, 25, 30, 35]
sum=0
for i in numbers:
    if i%2==0:
        sum=sum+i
print("sum of even numbers is",sum)

# #Sum of only odd numbers
numbers = [10, 15, 20, 25, 30, 35]
sum=0
for i in numbers:
    if i%2!=0:
        sum=sum+i
print("sum of odd numbers is",sum)

#average of list
numbers = [10, 20, 30, 40, 50]
total=0
number=0
for i in numbers:
    total=total+i
    number=number+1
average=total/number
print("total ",total)
print("average ",average)


# #Find the number of elements without len()
numbers = [10, 20, 30, 40, 50, 60, 70]
number=0
for i in numbers:
    number=number+1
print("number of element:",number)

#Find the sum of elments at even indexes
numbers = [10, 20, 30, 40, 50, 60]
sum=0
 for i in range(len(numbers)):
    if i%2==0:
        sum=sum+numbers[i] #here we get the value that is associated to that index
print("sum of index:",sum)

#Find the sum of elements at odd indexes
numbers = [10, 20, 30, 40, 50, 60]
sum=0
for i in range(len(numbers)):
    if i%2!=0:
        sum=sum+numbers[i] #here we get the value that is associated to that index
print("sum of index:",sum)

