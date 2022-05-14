number=int(input("Please enter a decimal number:  "))#allow the user to enter a decimal number
binary=[]#empty list to add values to 
if number==0:
    print(number)#print the number 0 if the user enter it
else:
    while (number!=0):#aloop if the number entered is not zero
        remainder=number%2#remainder of divining the number by 2
        binary.append(remainder)#add the remainder of division to the list
        number=number//2#divide the number by 2 with the result rounded to the minimum
binary.reverse()#reverse the order of the list value until the highest ranked values apper first
for i in range(0,len(binary)):#a ring that prints the list in the form of a number
    binary[i]=int (binary[i])
    print(binary[i],end="")
            
