#this function will make the question and answer files
import os
def makefiles(Questionfile,Answerkeyfile):
    Cont = 0
    while(Cont != 1):
        os.system('cls')
        while(True):
            question = input("type in the question: ")
            choice = input("type in the choices using a.(question) b.(question) ... d.(question): ")
            answer = input("what is the answer for this question: ")
            validate_question = input("are you sure you want to add this question to the file (y or n)")
            if (validate_question == "Y" or validate_question == "y"):
                break 
            elif(validate_question == "N" or validate_question == "n"):
                os.system('cls')
            else:
                print("error please renter the question")

        #write to both files
        Questionfile.write(question)
        Questionfile.write("\n")
        Questionfile.write(choice)
        Questionfile.write("\n")
        Answerkeyfile.write(answer)
        Answerkeyfile.write("\n")
        Cont = int(input("press 1 to stop adding questions press any key to continue"))
# this program is used to make the questions and answers for the flashcard program

print("This program will help you make the answer key and the question list for the flashcard program")

question_file_name =str(input("what would you like to name the file for the questions: "))
answerkey_file_name = str(input("what would you like to name the file for the answer key: "))
questionfile = open(question_file_name + ".txt", "w")
answerfile = open(answerkey_file_name + ".txt", "w")



title = input("please enter the title of the questions: ")
questionfile.write(title)
questionfile.write("\n")
makefiles(questionfile, answerfile)







questionfile.close()
answerfile.close()