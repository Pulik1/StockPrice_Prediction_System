import streamlit as st

from streamlit_option_menu import option_menu

import Home,Stock,Account,About_Us,Contact_Us,Feedback
st.set_page_config( 
    page_title="Welcome to Stocker",
    layout="centered",
    # background_image='StockBackground.jpg'
)
class MultiApp:
    def __init__(self) :
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function": function
        })
    def run():
        with st.sidebar:
            app= option_menu (
                menu_title=None,
                options=['Home','Account','Stock','About_Us','Contact_Us','Feedback'],
                icons=['house-fill','person-circle','cash-coin','info-circle-fill','person-lines-fill','ui-checks'],
                menu_icon="chat-text-fill",
                default_index=0,
                # orientation="horizontal",
                styles={
                    "container":{"padding": "5!important","background-color":"black"},
                    "icon": {"color":"White","Font-size":"23px"},
                    "nav-link":{"color":"White","font-size":"20px","text-align":"left","margin":"0px"},
                    "nav-link-selected": {"background-color":"#02ab21"},
                }
                )
        if app=='Home':
            # st.set_page_config( 
            # page_title="Welcome to Stocker",
            # layout="wide",)
            Home.app()
        if app=='Account':
            # Account.app()
            Account.app()
        if app=='About_Us':
            About_Us.app()
        if app=='Stock':
            Stock.app()
        if app=='Contact_Us':
            Contact_Us.app()
        if app=='Feedback':
            Feedback.app()
        
    run()        