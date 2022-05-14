#json file definition for questions and answers
import json
def json_writer_quiz():
    data = [{ 'Question1': { "Ques": "How many days are in a week?", "a": "8", "b": "6", "c": "7", "d": "9","correct_answer": "c" }
             ,'Question2': { "Ques": "How many letters are in the english alphabet?", "a": "28", "b": "26", "c": "27", "d": "29","correct_answer": "b" }
             ,'Question3': { "Ques": "How many colors are in the rainbow?", "a": "8", "b": "6", "c": "7", "d": "9", "correct_answer":"c" }
             ,'Question4': { "Ques": "How many days are in a year?", "a":"365", "b": "368", "c": "367", "d": "379", "correct_answer": "a" }
             ,'Question5': { "Ques": "How many hours are in a day?", "a":"28", "b":"26", "c": "29", "d": "24", "correct_answer": "d" }
             ,'Question6': { "Ques": "What is the capital of India?", "a": "Nagpur","b": "Mumbai", "c": "Delhi", "d": "Bangalore", "correct_answer": "c" }
             ,'Question7': { "Ques": "How many continents are in the world?", "a":"8", "b": "7", "c": "6", "d": "9", "correct_answer": "b" }
             ,'Question8': { "Ques": "Which direction does the sun set in?", "a": "north", "b":"east", "c": "west", "d": "south", "correct_answer": "b" }
             ,'Question9': { "Ques": "How many years are there in a millenium?", "a": "1000", "b": "100", "c": "10000", "d": "500", "correct_answer": "a" }
             ,'Question10': { "Ques": "Which is the smallest continent?", "a":"North America", "b":"Asia", "c": "Africa", "d": "Australia", "correct_answer": "d" }
             ,'Question11': { "Ques": "Who created Python?","a":"Guido van Rossum","b":"Elon Musk","c":"Bill Gates","d":"Mark Zuckerburg","correct_answer": "a"}
             ,'Question12': { "Ques": "What year was Python created?","a":"1989","b":"1991","c":"2000","d":"2016","correct_answer": "b"}
             ,'Question13': { "Ques": "Python is tributed to which comedy groub?:","a":"Lonely Island","b":"smosh","c":"Monty Python","d":"SNL","correct_answer": "c"}
             ,'Question14': { "Ques": "Is the Earth round?","a":"True","b":"False","c":"sometimes","d":"What's Earth?","correct_answer": "a"}
             ,'Question15': { "Ques": "What is the result of mixing blue and yellow?:","a":"purple","b":"red","c":"green","d":"white","correct_answer": "c"}
             ,'Question16': { "Ques": "What is the result of mixing blue and red?:","a":"purple","b":"yellow","c":"green","d":"white","correct_answer": "a"}
             ,'Question17': { "Ques": "What is the result of the following arthmetic operation (6*5-2(3*2)+2)","a":"16","b":"170","c":"20","d":"0","correct_answer": "c"}
             ,'Question18': { "Ques": "Which bear lives at the North Pole","a":"polar bear","b":"brown bear","c":"asiatic black bear","d":"sloth bear","correct_answer": "a"}
             ,'Question19': { "Ques": "Which is the largest animal?:","a":"elephant","b":"blue whale","c":"hippopotamus","d":"rhino","correct_answer": "b"}
             ,'Question20': { "Ques": "Which is the fastest land animal?:","a":"ostrich","b":"tiger","c":"cheetah","d":"zebra","correct_answer": "c"}} ]
    with open("ques.json", "w") as fileobj:json.dump(data, fileobj, indent=4)
if __name__ =='__main__': # creating json file for quiz questions
        json_writer_quiz()


import json
import random
qnum = 1
total_points = 0
lifeline_used =False
e_read = []
#Definition of a definition of one_time help deletes two answers
def eliminate_option(ques):
    possible_options = ['a', 'b', 'c', 'd']
    possible_options.remove(e_read[0]['Question' +str(ques)]['correct_answer'])
    any_two_to_remove =random.sample(possible_options, 2)
    two_to_keep = list(set(['a', 'b','c', 'd']) - set(any_two_to_remove)) + list(set(any_two_to_remove) -set(['a', 'b', 'c', 'd']))
    two_to_keep.sort()
    print("Options afterelimination are : ")
    print("{}: ".format(two_to_keep[0]) + e_read[0]['Question' +str(ques)][two_to_keep[0]])
    print("{}: ".format(two_to_keep[1]) + e_read[0]['Question' +str(ques)][two_to_keep[1]])
    return two_to_keep
#Defination of a function that prints the rules of the quiz
def rule_print():
    print("Welcome to 20 question quiz!")
    print("Rule 1 : Lifeline can be used only once")
    print("Rule 2 : You will only get one lifeline that is 50/50 which will eliminate two wrong answers")
    print("Rule 3 : The points are counted as follows : ")
    print("5 points are given for each correct answer")
    print("Rule 5 : After using a lifeline you get 10 seconds to give your answer")  
    print("Okay, so let's get started")
#Defination of a function that displays the value of the final score
def point_display(total):
    print("Your total points are ",total)
    if total <= 25:
        print("You can do better!")
    elif total <= 50:
        print("Good job! Keep improving")
    elif total <= 75:
        print("Nice! You seem smart")
    elif total <= 100:
        print("Great job! That was a nice ")
    else:
        print("You cracked the quiz! Brilliant!")
#Defining afunction that displays the questions and saves the answer chosen by the user in the file name.json
def ask_ques(): 
    global name
    name=input("Enter your name:  ")#Enter user name
    global qnum
    global total_points
    global lifeline_used
    data_list=[] #Define an empty list to add user answwer to
    ques =random.sample (range(1, 21),20)#definition of a function that displays questions in random order
    #An episode displaying questions and options for answers
    for i in ques:
        print("Question{}".format(qnum))
        print(e_read[0]["Question" + str(i)]['Ques'])
        print("a: " + e_read[0]['Question' + str(i)]['a'])
        print("b: " + e_read[0]['Question' + str(i)]['b'])
        print("c: " + e_read[0]['Question' + str(i)]['c'])
        print("d: " + e_read[0]['Question' + str(i)]['d'])
        c3 =input("Answer : (press l for lifeline) ")#add user answer to empty list
        while c3.lower() not in ['a','b', 'c','d', 'l']:
            print("Choose correctly")
            c3 = input("Answer :(press l for lifeline) ")
        #if you press the letter (l),it goes to the help tool   
        if c3.lower() == 'l':
            if not lifeline_used:
                possible_options = eliminate_option(i)
                lifeline_used = True
                pass
            else:
                possible_options = ['a', 'b', 'c','d']
                print("Sorry, lifeline already used!")
            while c3.lower() not in possible_options:
                print("Choose correctly")
                c3 = input("Answer : ")#Enter the answer by the user
        if c3.lower() ==e_read[0]['Question' + str(i)]['correct_answer'].lower():
            print("Your answer is correct! Let's go to the next question!")
            data_list.append(c3)#add user answer to empty list
            total_points=total_points+ 5
            #Enter the answer by the user       
            d=("correct answer: ",data_list)
            with open("name.json","w")as f:
                print(d)
            
        else:
            print("Sorry, wrong answer",e_read[0]['Question' + str(i)]['correct_answer'].lower())
            data_list.append(c3)
            #open file name.json to write user results
            d=("wrong answer: ",data_list)
            with open("name.json","w")as f:
                print(d)
        #increase the number of questions
        qnum=qnum+1
#write the user name and its final degree in the file name.json
    with open("name.json","w")as f:
        f.write("user name  : "+name+"\n")
    with open("name.json","a")as f:
        f.write("your score{} points\n".format(total_points))
    print(open("name.json","r").read())
    f.close()
    return "name.json"
#defination a function reading the previous chapter        
def read_all_ques():
    global e_read
    global reham
    #Downnload the question and answer file
    with open("ques.json") as fileobj:
        e_read =json.load(fileobj) 
if __name__ == '__main__':
    read_all_ques()#call Definition of the rules
    
    print("Welcome to the 20 question quiz!")
    c2 = input("Do you need me to tell you the rules? (Enter Y/y)")
    if c2.lower() == 'y':
        rule_print()
    else: print("Okay, so let's get started")
    choice = input("Are you ready to start? (Enter Y/y)")
    if choice.lower() == 'y':
        ask_ques()#call Definition of the question and the answer
        point_display(total_points)
        print("Thank you for playingthe quiz!")
    else:
        print("Okay! Do come back when you are ready! Bye :)")
   

  

