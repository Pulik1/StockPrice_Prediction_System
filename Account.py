import streamlit as st
# import pyrebase
# from datetime import datetime
import random
import smtplib
import firebase_admin
from firebase_admin import db,credentials
from firebase_admin import auth
import random
import time
import re
# import Home,Check_Stock_Price,About_Us,Contact_Us,Feedback

cred = credentials.Certificate('stock-1167b-firebase-adminsdk-wtx7c-2cfe717115.json')

def app():
    # st.set_page_config(page_title="Stocker.com", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None,)
    
    st.title("Welcome to User Login-Page") 

    def t():
        st.session_state.signout=False
        st.session_state.signedout=False
        st.session_state.username=''
    
    if 'username' not in st.session_state:
        st.session_state.username=''
        
    if 'useremail' not in st.session_state:
        st.session_state.useremail=''
    
    def f():
        try:
            user=auth.get_user_by_email(email)
            # print(user.uid)
            st.success("Login Successfully")
            # Home.app()
            st.session_state.username= user.uid
            st.session_state.useremail= user.email
            st.session_state.signedout=True
            st.session_state.signout=True
            
            
            # if app=='About_Us':
            #  About_Us.app()
            # if app=='Check_Stock_Price':
            #  Check_Stock_Price.app()
            # if app=='Contact_Us':
            #  Contact_Us.app()
            # if app=='Feedback':
            #  Feedback.app()
            
        except Exception as e:
            st.error(e)
    def is_valid_email(email):
    # Use a regular expression for basic email format validation
     email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
     return re.match(email_regex, email)
    def is_valid_password(password):
    # Password constraints: 8 characters, one uppercase, one lowercase, one special character, one digit
     return (
        len(password) >= 8
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in '!@#$%^&*()_-+=[]{}|;:,.<>?/' for char in password)
     )        
    if 'signedout' not in st.session_state:
        st.session_state.signedout=False
    if 'signout' not in st.session_state:
        st.session_state.signout=False 
    if not st.session_state['signedout']:
        choice=st.selectbox('Login/Signup',['Login','SignUp'])
    
        if choice=='Login':
          email = st.text_input("Enter your email:")
          if not is_valid_email(email):
           st.warning("Please enter a valid email address.")
          password=st.text_input('Password',type='password')
          st.button('Login',on_click=f)
          st.warning("Don't have an Account ?  Signup")
        #   Home.app()
        else:
          email = st.text_input("Enter your email:")
          if not is_valid_email(email):
           st.warning("Please enter a valid email address.")
          password = st.text_input("Create a password:", type="password")
          if not is_valid_password(password):
           st.warning("Password must be at least 8 characters long and include atleast one uppercase, one lowercase, one digit, and one special character.") 
          if is_valid_email(email) and is_valid_password(password):
           st.success("Email and Password formate are valid.")
          username=st.text_input("Enter unique username")
          def send_email(recipient_email, otp):
            sender_email = "pulikrpatel@gmail.com"
            app_password = "ynuu lbgs edtq olhh"

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, app_password)

            subject = "Your OTP (One Time Password)"
            body = f"Your OTP is {otp}"
            message = f"Subject: {subject}\n\n{body}"

            server.sendmail(sender_email, recipient_email, message)
            server.quit()
          def run():
    # Use session state to persist data across app reruns
           if "otp" not in st.session_state:
            st.session_state.otp = random.randint(1000, 9999)
            st.session_state.email_sent = False

    # Display UI components
           if not st.session_state.email_sent:
            # recipient_email = st.text_input("Enter your email:")
            recipient_email=email
            if st.button("Send OTP"):
              try:
               if recipient_email:
                send_email(recipient_email, st.session_state.otp)
                st.session_state.email_sent = True
                st.success("OTP sent successfully!")
                st.info("Press enter to Continue")
               else:
                st.warning("Please enter a valid email address.")
              except Exception as e:
                 st.error(e)
           else:
             entered_otp = st.text_input("Enter the OTP:")
             if 'button_clicked' not in st.session_state:
                st.session_state.button_clicked=False
             if not st.session_state.button_clicked:
              if st.button("Verify OTP"):
               if entered_otp.isdigit() and int(entered_otp) == st.session_state.otp:
                st.success("OTP verification successful!")
                st.info("Press Enter to Continue.")
                st.session_state.button_clicked=True
               else:
                st.error("Incorrect OTP. Please try again.")
             else:
                # st.warning("Email Verification is Completed. Click on Create Account Button to Create your Account.")
                if 'create_button_else' not in st.session_state:
                   st.session_state.create_button_else=False
                if not st.session_state.create_button_else:
                   if st.button("Create Account"):
                      try:
                        user=auth.create_user(email=email,password=password,uid=username)
                        st.success("Account Created Successfully!")
                        st.warning("Please Login with the same credentials to access our services")
                        st.balloons()
                      except Exception as e:
                         st.error(e)
                      st.session_state.create_button_else=True
                else:
                   st.success("Your Account is Already Created. Now Select Login to Access Our Services.")
          run()
    # if st.button('Create My Account'):
    #         # user=auth.create_user(email=email,password=password,uid=str(temp_otp))
    #         st.success("Account Created Successfully!")
    #         st.warning("Please Login with the same credentials to access our services")
    #         st.balloons()
                 
    if st.session_state.signout:
        st.text('Name : '+st.session_state.username)
        st.text('Email-id : '+st.session_state.useremail)
        st.button('Sign out',on_click=t)
#         # Home.app() 
           