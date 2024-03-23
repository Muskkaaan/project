import streamlit as st
import csv
import os
import re
from difflib import SequenceMatcher

# Set background color and font
st.markdown(
    """
    <style>
    .stApp {
        background-color: #d0b783; 
        font-family: Arial, sans-serif; 
    },
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to validate password strength
def validate_password(password):
    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if len(password) < 6:
        return False

    return True

# Function to get the next available serial number
def get_next_serial_number():
    try:
        with open("Login_portal.csv", 'r') as file:
            file.seek(0)
            reader = csv.reader(file)
            rows = list(reader)
            last_index = len(rows)
            return last_index 
    except FileNotFoundError:
        return 1
    
    
# Function for user signup
def signup():
    name = st.text_input("Enter your name:")
    prof = st.radio("Are you a student or a teacher?", ("Student", "Teacher"))
    password = st.text_input("Enter a strong password:", type="password")
    
    if st.button("Sign Up", key = "signup"):
        if validate_password(password):
            next_serial_number = get_next_serial_number()
            with open("Login_portal.csv", 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([next_serial_number, name, password, prof, 0, 0, 0])  # Initial paper creation flags set to 0
            st.success("Signup Successful!")
            return True
        else:
            st.error("Password is weak. Please try again.")
            return False

# Function to load login credentials from CSV
def load_login_credentials():
    credentials = {}
    with open("Login_portal.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            credentials[row[1]] = (row[2], row[3])  # Username: (password, role)
    return credentials

# Function to authenticate login
def login(username, password, role):
    credentials = load_login_credentials()
    if username in credentials:
        if credentials[username][0] == password and credentials[username][1] == role:
            return True
    return False


# Function for user login
def login(username, password, role):
    #name = st.text_input("Enter your name:")
    #password = st.text_input("Enter your password:", type="password")
    
    #if st.button("Login"):
        try:
            with open("Login_portal.csv", 'r') as file:
                file.seek(0)
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    if row[1] == username:
                        if row[2] == password:
                            st.success("Login Successful!")
                            return True, row[3]  # Return user role
                st.error("Invalid Username or Password")
                return False, None
        except FileNotFoundError:
            st.error("CSV file not found.")
            return False, None

# Function to create a question paper
def create_paper(subject, name):
    questions_answers = []
    if subject == "Maths":
        count = int(st.number_input("Enter the number of questions that you want to create", min_value=1, step=1))
        for i in range(count):
            question = st.text_input(f"Enter question number {i+1}:")
            answer = st.text_input(f"Enter answer for question {i+1}:", key=f"answer_{i+1}_{subject.lower()}")
            questions_answers.append((question, answer))
    
    elif subject == 'DBMS':
        count = int(st.number_input("Enter the number of questions that you want to create", min_value=1, step=1))
        for i in range(count):
            question = st.text_input(f"Enter question number {i+1}:")
            answer = st.text_input(f"Enter answer for question {i+1}:", key=f"answer_{i+1}_{subject.lower()}")
            questions_answers.append((question, answer))
                
    elif subject == 'OS':
        count = int(st.number_input("Enter the number of questions that you want to create", min_value=1, step=1))
        for i in range(count):
            question = st.text_input(f"Enter question number {i+1}:")
            answer = st.text_input(f"Enter answer for question {i+1}:", key=f"answer_{i+1}_{subject.lower()}")
            questions_answers.append((question, answer))
    
    return questions_answers

# Function to store questions and answers in CSV
def store_questions_answers(subject, name, questions_answers):
    filename = f"{subject.lower()}.csv"
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if os.stat(filename).st_size == 0:
            writer.writerow(['Serial_no', 'Subject', 'Name', 'Question', 'Answer'])
        for i, (question, answer) in enumerate(questions_answers, start=1):
            writer.writerow([i, subject, name, question, answer])

# Function to display similarity analysis results
def display_similarity_analysis(similarity_scores):
    st.write("Similarity Analysis:")
    for i, similarity in enumerate(similarity_scores, start=1):
        st.write(f"Question {i} Similarity: {similarity}%")
        
# Function to sign up a new user
#def signup(name, password, role):
 #   next_serial_number = get_next_serial_number()
  #  try:
   #     # Check if username already exists
    #    credentials = load_login_credentials()
     #   if name in credentials:
      #      return False  # Username already exists, return False
       #     
        # Write new entry to CSV
        #with open("Login_portal.csv", 'a', newline='') as file:
         #   writer = csv.writer(file)
          #  writer.writerow([next_serial_number, name, password, role])
        #st.success("Sign up successful! You can now log in.")
        #return True  # Signup successful
    #except (FileNotFoundError, PermissionError) as e:
     #   st.error(f"Error occurred while signing up: {e}")
      #  return False  # Signup failed

# Function to get the next available serial number
#def get_next_serial_number():
 #   try:
  #      with open("Login_portal.csv", 'r', newline="") as file:  # Open in 'r' mode for reading
   #         reader = csv.reader(file)
    #        next(reader)  # Skip header
     #       serial_numbers = [int(row[0]) for row in reader if row[0].isdigit()]  # Only consider rows with valid integers
      #      if serial_numbers:
       #         return max(serial_numbers) + 1
        #    else:
         #       return 1
    #except FileNotFoundError:
     #   return 1  # Start from 1 if file doesn't exist

        
# Main function
def main():
    st.title("ANONYMOUS EXAM PORTAL")

if __name__ == "_main_":
    main()
