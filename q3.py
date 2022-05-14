l=["Network","Math","Programming","Physics","Music"]#list
i=0#counter
for i in range (len(l)):#loop to search for name that begins with the letter P
    if l[i][0].find("P")==0:
     print(l[i])#print the name when the condition is met
i=i+1#increase counter
