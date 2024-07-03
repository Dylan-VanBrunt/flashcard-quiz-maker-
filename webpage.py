import streamlit as st
import os

## enter this command to run it
## streamlit run webpage.py


#pagetitle and icon
st.set_page_config(page_title="FlashStudy", page_icon="🤓" , layout="wide")

#header section
#st.subheader("This is a great way to practice multiple choice tests")
#st.title("A quiz generator")
#st.write("i hope this helps you alot ")


# streamlit_app.py

def makefiles(Questionfile, Answerkeyfile):
    Cont = 0
    key = 0
    while Cont != 1:
        st.text("Enter the flashcard details:")
        question = st.text_input("Type in the question:")
        choice = st.text_input("Type in the choices using a.(question) b.(question) ... d.(question):")
        answer = st.text_input("What is the answer for this question:")
        validate_question = st.text_input("Are you sure you want to add this question to the file? (Type Y or N)")
        
        if validate_question.lower() == "y":
            # Write to both files
            Questionfile.write(question + "\n")
            Questionfile.write(choice + "\n")
            Answerkeyfile.write(answer + "\n")
            Cont = int(st.text_input("Press 1 to stop adding questions, press any key to continue"))

# Streamlit UI
st.title("Flashcard Maker App")

# Create file names input widgets
question_file_name = st.text_input("Enter the name for the question file:")
answerkey_file_name = st.text_input("Enter the name for the answer key file:")

# Create file objects
question_file = open(question_file_name + ".txt", "w")
answer_file = open(answerkey_file_name + ".txt", "w")

# Get flashcard details
title = st.text_input("Enter the title of the flashcards:")
question_file.write(title + "\n")

# Button to start making flashcards
if st.button("Start Making Flashcards",key="unique"):
    makefiles(question_file, answer_file)

# Close files
question_file.close()
answer_file.close()