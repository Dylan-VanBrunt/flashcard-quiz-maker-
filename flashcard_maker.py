import re
import os
import random


#lists for questions answers and answer key
questionlist = []
answerlist = []
answerkey = []
#variable to count total correct answers and wrong answers
count_correct = int(0)
#open the file in read mode
###############################
##############################
#################################Make sure to have a user input for name of the file to quiz
with open("flashc_questions.txt", "r") as f:
    #read each line in the file
    #variable to decide question or answer based on line position start at 0 to get 0
    QorA = int(0)
    title = f.readline().strip()
    for line in f:
        
        if (QorA % 2 == 0):
            questionlist.append(line.rstrip("\n"))
        elif (QorA % 2 != 0):
            answerlist.append(line.rstrip("\n"))
        QorA += 1

#to get answer key 
with open("answerkey.txt", "r") as A:
    for line in A:
        answerkey.append(line.rstrip("\n"))


#create a list that will be for how many questions to use for the random question asker
# so that questions can be removed from the list when answered
questionindex = []
qnum = 1
for i in range (0,len(questionlist)):
    questionindex.append(qnum)
    qnum += 1




#to receive the answer from the user
answerchoice=str()
#chose which question
Qchoice = int()
#loop controller
stop = 1
questionsleft = len(questionindex)
totalright = int(0)
while (questionsleft > 0):
    #clear screen
    os.system('clear')

    #Qchoice = int(input("what question do you want to check: ")) (Testing each question)
    Current_question = random.choice(questionindex)

    #this removes used questions so that they dont get asked again
    while True:
        try:
            questionindex.remove(Current_question)
            break
        except ValueError:
            Current_question = random.choice(questionindex)
            
    

    Qchoice = Current_question
    Qchoice = Qchoice - 1   #to make sure you get the correct index value
    print(title , "\n")
    print(questionlist[Qchoice])
    #this adds a newline character to the output so its easier to read
    print(answerlist[Qchoice].replace('a.', '\na. ').replace('b.', '\nb. ').replace('c.', '\nc. ').replace('d.', '\nd. '))
    print("\n")
    #check for correct answer and output message
    answer = input("Enter answer: ")
    if (answer == answerkey[Qchoice]):
        print("you are correct ","\n" )
        #count hom many questions were answered correctly
        totalright += 1
        input("press enter to go to the next question")
    else:
        print("you are wrong","\n")
        print( "the correct answer is " , answerkey[Qchoice] )
        input("press enter to go to the next question")
    
    # change this to make the loop controller the length pf the list
   #stop = int(input("Press 1 to continue or 0 to stop: "))

    questionsleft -= 1

print("you got ", totalright , " correct out of ", len(questionlist), " questions")