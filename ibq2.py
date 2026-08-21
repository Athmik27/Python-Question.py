#armstrong number
# n=int(input("enter an number:"))
# num=0
# while (n>0):
#     digit=n%10
#     num=num+digit ** 3
#     n=n//10
# print("armstrong number is:",num)
# value=n #check whether the vakue is armstong or no.
# if num==value:
#     print("its armstrong")
# else:
#     print("not an armstrong")

#string reversing
# def Rev_str(text):
#     for i in range(len(text)-1,-1,-1):
#         yield text[i]
# for i in Rev_str("Manipal"):
#     print(i)

#or
# def Rev_str():
#     text=input("enter an string:")
#     for i in range(len(text)-1,-1,-1):
#         yield text[i]
# for i in Rev_str():
#     print(i)

#remove the duplicate value from the list
# list_1=[1,2,2,3,4,4,5]
# list_2=[]
# for i in list_1:
#     if i not in list_2:
#         list_2.append(i)
# print(list_2)

#second largest number in list
# numbers = [10, 25, 7, 45, 18]
# largest=numbers[0]
# second_largest=numbers[0]
# for i in numbers:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif(i>second_largest):
#         second_largest=i
# print("second largest number is :",second_largest)

#second smallest number in list
# numbers=[10,25,7,45,18]
# smallest=numbers[0]
# second_smallest=numbers[0]
# for i in numbers:
#     if i<smallest:
#         second_smallest=smallest
#         smallest=i
#     elif(i<second_smallest):
#         second_smallest=i
# print('second smallest number is:',second_smallest)

#count how many positive numbers, negative numbers, and zeros are present in a list.
# list_1=[10, -5, 0, 8, -2, 0, 7]
# positive_value=0
# negative_value=0
# null_value=0
# for i in list_1:
#     if i>0:
#         positive_value=positive_value+1
#         print("number of positive value:",positive_value)
#     elif i<0:
#             negative_value=negative_value+1
#             print("number of negative value:",negative_value)
#     else:
#             null_value=null_value+1    
#             print("number of null value:",null_value)

# sum of an list
# list_1=[10, 20, 30, 40]
# sum=0
# for i in list_1:
#     if i>0:
#       sum=sum+i
# print("sum:",sum)  

#average element in list
# list_1=[10, 20, 30, 40]
# count=0
# sum=0
# for i in list_1:
#     sum=sum+i
#     count=count+1
# average=sum/count
# print("sum:",sum)
# print('average number is:',average)

# #largest and smallest in list
# list_1=[10, 25, 7, 45, 18]
# largest=list_1[0]
# smallest=list_1[0]
# for i in list_1:
#     if i>largest:
#         largest=i
#     if i<smallest:
#             smallest=i

# print("largest value is:",largest)
# print("smallest value is:",smallest)

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