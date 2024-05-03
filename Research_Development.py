import authenticator
import pandas as pd
import numpy as np
import plotly as px
import plotly.graph_objects as go
import streamlit as st
import matplotlib.pyplot as plt
import time
import pickle
from pathlib import Path
import streamlit_authenticator as sauth
import openpyxl
##############################################Background##########
# Check if 'key' already exists in session_state
#

##Auth##

Name=["Earth Enable"]
Username=["david"]
Password=["123"]
file_path=Path(__file__).parent /"hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_pass=pickle.load(file)

authenticator= sauth.Authenticate(Name,Username,hashed_pass,"EE_Dash","ABCDE", cookie_expiry_days=1)
name, authentication_status, username= authenticator.login("Login","main")
##########################################################################################

if authentication_status == False:
    st.error("Username or password is incorrect")
if authentication_status== None:
    st.warning("Please enter username and password")
if authentication_status:


    st.title("International Standard Industrial Classification of All Economic Activities Revision 4")
    #Navigation bar or side bar

    authenticator.logout("Logout", "sidebar") #Logout authentication
    st.sidebar.title("ISIC REVISION 4")
############################################################################
    with open("style.css") as css:
        st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
#####################################################################################
    Rad= st.sidebar.radio("CONTENTS",["Title page","Introduction","Detailed Structure","About us"])
    if Rad== "Title page":
        st.write(" Author: David Hagumuwumva",layout="wide")
        st.write(" Institution: BNR")
        st.write(" Department: Financial Stability Monitoring")

    if Rad=="Introduction":
        import streamlit as st

        col1, col2 = st.columns(2)
        with col1:
            st.header("Introduction")
            st.write("ISIC is the international reference classification of productive activities. It has been adopted in 1948 with purpose of providing set of categories of activities that can be used in data collection, analysis and reporting of statistics based on that activities. Since several nations have adopted ISIC, it has been a vital tool for comparing economic statistics of a country with the rest of the world. In this presentation we summarize all ISIC sections.")
        with col2:
            st.header("Why ISIC, Rev.4?")
            st.write("In comparison with previous version of ISIC, the ISCI revision 4 is more detailed than the previous version, responding to the need to identify many new industries separately. This is especially applicable in the case of services. Moreover, the relevance of the Classification has been enhanced with the introduction of new high-level categories to better reflect current economic phenomena. A new section entitled “Information and communication” has been introduced.")
    if Rad=="Detailed Structure":
        option = st.selectbox(
            'LEVEL 1:',
            ( " ",  "A. Agriculture, forestry and fishing", "B. Mining and quarrying ", "C. Manufacturing ",
             "D. Electricity, gas, steam and air conditioning supply",
             "E. Water supply; sewerage, waste management and remediation activities ", "F. Construction ",
             "G. Wholesale and retail trade; repair of motor vehicles and motorcycles ",
             "H. Transportation and storage ", "I. Accommodation and food service activities ",
             "J. Information and communication ", "K. Financial and insurance activities ",
             "L. Real estate activities ", "M. Professional, scientific and technical activities ",
             "N. Administrative and support service activities ",
             "O. Public administration and defence; compulsory social security ", "P. Education ",
             "Q. Human health and social work activities", "R. Arts, entertainment and recreation ",
             "S. Other service activities ",
             "T. Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use ",
             "U. Activities of extraterritorial organizations and bodies "))
        st.write('You selected:', option)
        if option=="A. Agriculture, forestry and fishing":
            st.write(
                "This section includes the exploitation of vegetal and animal natural resources, comprising the activities of growing of crops, raising and breeding of animals, harvesting of timber and other plants, animals or animal products from a farm or their natural habitats.")
            optionAg2 = st.selectbox('LEVEL 2:',
                (" ",'Crop and animal production, hunting and related service activities', 'Forestry and logging', 'Fishing and aquaculture'))
            st.write('You selected:', optionAg2)
            if optionAg2=="Crop and animal production, hunting and related service activities":
                st.write('This division includes two basic activities, namely the production of crop products and production of animal products, covering also the forms of organic agriculture, the growing of genetically modified crops and the raising of genetically modified animals. This division also includes service activities incidental to agriculture, as well as hunting, trapping and related activities.')
                st.write("Note: It exclude any subsequent processing of the agricultural products((Manufacture of food products and beverages) and division 12 (Manufacture of tobacco products)), and field construction (e.g. agricultural land terracing, drainage, preparing rice pddis etc.)")
                optionAg3 = st.selectbox('LEVEL 3:',
                (' ','Growing of non-perennial crops','Growing of perennial crops','Plant propagation','Animal production','Mixed farming','Support activities to agriculture and post-harvest crop activities','Hunting, trapping and related service activities'))
                st.write('You selected:', optionAg3)
                if optionAg3=="Growing of non-perennial crops":
                    st.write(
                        "This group includes the growing of plants that do not last for more than two growing seasons. Included is the growing of these plants for the purpose of seed production.")

                    optionAg4= st.selectbox('LEVEL 4:',
                    ('','Growing of cereals (except rice) leguminous crops and oil seeds' ,  'Growing of rice' ,  'Growing of vegetables and melons', 'roots and tubers', 'Growing of sugar cane', 'Growing of tobacco', 'Growing of fibre crops', 'Growing of other non-perennial crops'))
                    st.write('You selected:', optionAg4)
                    if optionAg4=='Growing of cereals (except rice) leguminous crops and oil seeds':
                        st.write('This class includes all forms of growing of cereals, leguminous crops and oil seeds in open fields, including those considered organic farming and the growing of genetically modified crops. The growing of these crops is often combined within agricultural units.')
                        if optionAg4 == "Growing of cereals (except rice) leguminous crops and oil seeds":
                            optionAg5 = st.selectbox('LEVEL 5:',
                            (' ','Growing of cereals', 'Growing of leguminous crops', 'Growing of oil seeds'))
                            st.write('You selected:', optionAg5)
                            if optionAg5 == "Growing of cereals":
                                optionAg6 = st.selectbox('LEVEL 6:',
                                ('','Wheat', 'grain maize', 'sorghum', 'barley', 'rye', 'oats',  'millets',  'other cereals n.e.c.'))
                                st.write('Congratulations you are now on level 6, you selected: ', optionAg6)
                            if optionAg5 == "Growing of leguminous crops":
                                optionAg6 = st.selectbox('LEVEL 6:',
                                ('','Beans','broad beans','chick peas', 'cow peas', 'lentils', 'lupins','peas','pigeon peas', 'other leguminous crops'))
                                st.write('Congratulations you are now on level 6, you selected: ', optionAg6)
                            if optionAg5 == 'Growing of oil seeds':
                                optionAg6 = st.selectbox('LEVEL 6:',
                                ('','soya beans', 'groundnuts', 'castor bean', 'linseed', 'mustard seed', 'niger seed', 'rapeseed', 'safflower seed', 'sesame seed', 'sunfower seed','other oil seeds'))
                                st.write('Congratulations you are now on level 6, you selected: ', optionAg6)







    if Rad=="About us":
        st.header("About us")
        progress= st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
        st.balloons()#Ballon after annimations
        st.error("Error message")
        st.success("Success")
        st.info("information")
        st.warning("Warning")


