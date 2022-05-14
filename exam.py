l=["Reham","Nour","Rasha","Hasan","Mohammed","Ali"]
n=input("Enter your name if you are a graduate student: ")#Allow the user to enter his name

i=0#counter
for l[i] in l:#loop to search for user name
    #capitalize the first letter of the entered name because the list has the first letter of the names in upper 
    if n.capitalize()==l[i]:
      print("Yes",n,"is a graduate student")#print the name if equality is true
      break#get out of the loop
    else:
      print("no there in the list")
i=i+1#increase counter
