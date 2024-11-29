import streamlit as st
from streamlit_option_menu import option_menu
# import Home,Check_Stock_Price,Account,About_Us,Contact_Us,Feedback
import firebase_admin
from firebase_admin import db,credentials
from firebase_admin import auth
import requests
import pycountry
from PIL import Image
import io
# from api import apiKEY
# cred = credentials.Certificate('stock-1167b-firebase-adminsdk-wtx7c-2cfe717115.json')
# firebase_admin.initialize_app(cred)
# apiKEY="d5878476a4cb42ccbae6443bab8620b7"
def app():
    # st.set_page_config(page_title="Stocker.com", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None,)
    # st.markdown(
    #     """
    #     <style>
    #         body {
    #             background-image: url('StockBackground.jpg');
    #             background-repeat: no-repeat;
    #             background-attachment: fixed;
    #             background-size: cover;
    #         }
    #     </style>
    #     """,unsafe_allow_html=True
    # )
    # st.title("Hello, "+st.session_state.username)
    # latest_news,Politics,Stock_market_news,Economic_news,Crypto_news=st.tabs(["latest_news","Politics"])
    # st.header("Learn all concepts of Stock Market:")
    # col1v,col2v,col3v=st.columns(3)
    # col1v.video("https://youtu.be/3UF0ymVdYLA?si=Zma0W5UoGwat3f8r", format="video/mp4", start_time=0)
    # col2v.video("https://youtu.be/8rIviI0ZKNA?si=PqhdQGs4E1XAbkhq",format="video/mp4",start_time=0)
    # col3v.video("https://youtu.be/PFN8dGDT0ZA?si=FO55a6lGlAYic48j",format="video/mp4",start_time=0)
    # # st.video("https://youtu.be/3UF0ymVdYLA?si=Zma0W5UoGwat3f8r", format="video/mp4", start_time=0)
    # #st.header("Learn Analysis of Various Stock Graphs:")
    # col1g,col2g,col3g=st.columns(3)
    # col1g.video("https://youtu.be/jOLX7nqRTqg?si=O4O8hGGK1l84addQ", format="video/mp4", start_time=0)
    # col2g.video("https://youtu.be/V47CdOCDo4s?si=9uTz0ZqrEUSyl3il",format="video/mp4",start_time=0)
    # col3g.video("https://youtu.be/mRfVY9Wbnrs?si=AgHST1tgLLK0rGLu",format="video/mp4",start_time=0)
    st.title("Stocker.com")
    st.write("Welcome to Stocker.com! Your one-stop destination to learn about the Stock Market, watch informative videos, and stay updated with the latest news.")
    
    # Introduction to video section
    st.header("Learn all concepts of Stock Market:")
    st.subheader("Watch these introductory videos to get started:")
    
    # Videos section
    col1v, col2v, col3v = st.columns(3)
    col1v.video("https://youtu.be/3UF0ymVdYLA?si=Zma0W5UoGwat3f8r", format="video/mp4", start_time=0)
    col2v.video("https://youtu.be/8rIviI0ZKNA?si=PqhdQGs4E1XAbkhq", format="video/mp4", start_time=0)
    col3v.video("https://youtu.be/PFN8dGDT0ZA?si=FO55a6lGlAYic48j", format="video/mp4", start_time=0)
    
    # Introduction to stock graphs section
    st.header("Learn Analysis of Various Stock Graphs:")
    st.subheader("Explore these videos to understand stock graph analysis:")
    
    # Stock graphs section
    col1g, col2g, col3g = st.columns(3)
    col1g.video("https://youtu.be/jOLX7nqRTqg?si=O4O8hGGK1l84addQ", format="video/mp4", start_time=0)
    col2g.video("https://youtu.be/V47CdOCDo4s?si=9uTz0ZqrEUSyl3il", format="video/mp4", start_time=0)
    col3g.video("https://youtu.be/mRfVY9Wbnrs?si=AgHST1tgLLK0rGLu", format="video/mp4", start_time=0)

    

# Create six columns for the videos
    # col1v, col2v, col3v, col4v, col5v, col6v = st.columns(6)

# Define the URLs of the videos
    # video_urls = [
    # "https://youtu.be/3UF0ymVdYLA?si=Zma0W5UoGwat3f8r",
    # "https://youtu.be/8rIviI0ZKNA?si=PqhdQGs4E1XAbkhq",
    # "https://youtu.be/PFN8dGDT0ZA?si=FO55a6lGlAYic48j",
    # "https://youtu.be/jOLX7nqRTqg?si=O4O8hGGK1l84addQ",
    # "https://youtu.be/V47CdOCDo4s?si=9uTz0ZqrEUSyl3il",
    # "https://youtu.be/mRfVY9Wbnrs?si=AgHST1tgLLK0rGLu"
    # ]

# Initialize video index
    # video_index = 0

# Display the first three videos
    # col1v.video(video_urls[video_index], format="video/mp4", start_time=0)
    # video_index += 1
    # col2v.video(video_urls[video_index], format="video/mp4", start_time=0)
    # video_index += 1
    # col3v.video(video_urls[video_index], format="video/mp4", start_time=0)
    # video_index += 1

# Add a "Next" button next to the videos
# if st.button("Next", key="next_button"):
#     if video_index < len(video_urls):
#         col1v.video(video_urls[video_index], format="video/mp4", start_time=0)
#         video_index += 1
#     if video_index < len(video_urls):
#         col2v.video(video_urls[video_index], format="video/mp4", start_time=0)
#         video_index += 1
#     if video_index < len(video_urls):
#         col3v.video(video_urls[video_index], format="video/mp4", start_time=0)
#         video_index += 1


    # st.header("Check Various News")
    user=st.text_input("Enter Country name",value="India")
    latest_news,Science,Business_news,Sports_news,Crypto_news,Health,Technology=st.tabs(["Latest News","Science News","Business News","Sports News","Crypto News","Healthcare Sector","Technology Sector"])
    # colln1,colln2,colln3=st.columns(3,gap="medium")
    # st.header("Latest News")
    with latest_news:
        # user=st.text_input("Enter Country name for Latest News", value="India")
        country = pycountry.countries.get(name=user).alpha_2
        url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=10cd10d5db4548eab10c43bf0b45f59e" 
        r=requests.get(url)
        r=r.json()
        articles = r['articles']
        for article in articles:
            st.header(article['title'])
            st.write(article['publishedAt']) 
            if article['author']:
                st.write(article['author'])
                st.write(article['source']['name'])
                st.write(article['description'])
                st.write(article['url'])
                # st.image(article['urlToImage'])
            # st.image(article['urlToImage'],output_format="auto")
            # aux_im = Image.open(io.BytesIO(r.content))
            # st.image(aux_im)
    
    with Science:
        # user1=st.text_input("Enter Country name for Science News")
        country = pycountry.countries.get(name=user).alpha_2
        url=f"https://newsapi.org/v2/top-headlines?country={country}&category=science&apiKey=10cd10d5db4548eab10c43bf0b45f59e"
        
        r1=requests.get(url)
        r1=r1.json()
        articles= r1['articles']
        for article in articles:
            st.header(article['title'])
            st.write(article['publishedAt'])
            if article['author']:
                st.write(article['author'])
                st.write(article['source']['name'])
                st.write(article['description'])
                st.write(article['url'])
                # st.image(article['urlToImage'])
        # st.write("Science data")
    
    with Business_news:
        # user2=st.text_input("Enter Country name for Business News")
        country = pycountry.countries.get(name=user).alpha_2
        url=f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey=10cd10d5db4548eab10c43bf0b45f59e"
        
        r2=requests.get(url)
        r2=r2.json()
        articles= r2['articles']
        for article in articles:
            st.header(article['title'])
            st.write(article['publishedAt'])
            if article['author']:
                st.write(article['author'])
                st.write(article['source']['name'])
                st.write(article['description'])
                st.write(article['url'])
                # st.image(article['urlToImage'])
        # st.write("Stocket Market news")
    with Sports_news:
        # user3=st.text_input("Enter Country name for Sports News")
        country = pycountry.countries.get(name=user).alpha_2
        url=f"https://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey=10cd10d5db4548eab10c43bf0b45f59e"
        
        r3=requests.get(url)
        r3=r3.json()
        articles= r3['articles']
        for article in articles:
            st.header(article['title'])
            st.write(article['publishedAt'])
            if article['author']:
                st.write(article['author'])
                st.write(article['source']['name'])
                st.write(article['description'])
                st.write(article['url'])
                # st.image(article['urlToImage'])
        # st.write("Economic news")
    with Crypto_news:
        url=f"https://newsapi.org/v2/everything?q=bitcoin&apiKey=10cd10d5db4548eab10c43bf0b45f59e"
        
        r4=requests.get(url)
        r4=r4.json()
        articles= r4['articles']
        for article in articles:
            st.header(article['title'])
            st.write(article['publishedAt'])
            if article['author']:
                st.write(article['author'])
                st.write(article['source']['name'])
                st.write(article['description'])
                st.write(article['url'])
                # st.image(article['urlToImage'])
        # st.write("Crypto news")
    
    with Health:
        # user5=st.text_input("Enter Country name for Healthcare News")
        country = pycountry.countries.get(name=user).alpha_2
        url=f"https://newsapi.org/v2/top-headlines?country={country}&category=health&apiKey=10cd10d5db4548eab10c43bf0b45f59e"
        
        r5=requests.get(url)
        r5=r5.json()
        articles= r5['articles']
        for article in articles:
            st.header(article['title'])
            st.write(article['publishedAt'])
            if article['author']:
                st.write(article['author'])
                st.write(article['source']['name'])
                st.write(article['description'])
                st.write(article['url'])
                # st.image(article['urlToImage'])
        # st.write("Energy Sector")
    
    with Technology:
        # user6=st.text_input("Enter Country name for Tech News")
        country = pycountry.countries.get(name=user).alpha_2
        url=f"https://newsapi.org/v2/top-headlines?country={country}&category=technology&apiKey=10cd10d5db4548eab10c43bf0b45f59e"
        
        r6=requests.get(url)
        r6=r6.json()
        articles= r6['articles']
        for article in articles:
            st.header(article['title'])
            st.write(article['publishedAt'])
            if article['author']:
                st.write(article['author'])
                st.write(article['source']['name'])
                st.write(article['description'])
                st.write(article['url'])
                # st.image(article['urlToImage'])
    #     # st.write("Technology Sector")
    
    # if app=='Home':
    #     Home.app()
    # if app=='About_Us':
    #     About_Us.app()
    # if app=='Check_Stock_Price':
    #     Check_Stock_Price.app()
    # if app=='Contact_Us':
    #     Contact_Us.app()
    # if app=='Feedback':
    #     Feedback.app()
    # if app=='Account':
    #     Account.app()