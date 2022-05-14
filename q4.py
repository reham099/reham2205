dict=dict()#define an empty dictionary to add values to him
print("d={",end="")
for i in range(0,10):#A loop counting from 0 to 10
    i=i+1#increase counter
    dict[i]=i*i#squaring the number and adding it to the dictionary
    print(i,":",dict[i],end="    ,")#printing the number and its square as a dictionary
print("}")
