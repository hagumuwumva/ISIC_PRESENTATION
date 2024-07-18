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

Name=["National Bank of Rwanda"]
Username=["bnr"]
Password=["bnrisic"]
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


    st.title("International Standard Industrial Classification of All Economic Activities (ISIC)")
    #Navigation bar or side bar

    authenticator.logout("Logout", "sidebar") #Logout authentication
    st.sidebar.title("welcome to this page")
#####################################################################################
    Rad= st.sidebar.radio("OUTLINE",["Introduction","Long term customer satisfaction","Discovery surveys","Moisture interventions","Purchasing power test","About us"])
    if Rad=="Introduction":
        st.write("Data-driven decisions are crucial in research and development. Through data analysis, institutions are able to learn more about their clients and test hypotheses. By using a streamlit dashboard, we present the most important insights on various ongoing projects on this page. ")
    if Rad=="Long term customer satisfaction":
        Rad12=st.sidebar.radio("Customer satisfaction and Repair done",["Customer satisfaction","Repair done"])
        if Rad12=="Customer satisfaction":

            st.title("Long term customer satisfaction")





            Long= pd.read_excel('Long_term_c.xlsx')
            Long=pd.DataFrame(Long)

            Long.replace(" ", np.nan)
            # Calculations
            Having_floor = pd.DataFrame(Long['Do you still have Tube Heza Floor?'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%').reset_index()
            Having_floor_Yes = Having_floor.at[0, 'Do you still have Tube Heza Floor?']
            Having_floor_No = Having_floor.at[1, 'Do you still have Tube Heza Floor?']

            Maintenance = pd.DataFrame(Long['Remembers Floor Maintainance'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%').reset_index()

            Maintenance_Yes = Maintenance.at[0, 'Remembers Floor Maintainance']
            Maintenance_No = Maintenance.at[1, 'Remembers Floor Maintainance']
            # Maintenance_NA = Maintenance.at[2, 'Remembers Floor Maintainance']
            #
            Issue = pd.DataFrame(Long['Does Your floor/Plaster have issues?'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%').reset_index()
            Issue_Yes = Issue.at[0, 'Does Your floor/Plaster have issues?']
            Issue_No = Issue.at[1, 'Does Your floor/Plaster have issues?']

            Satisfaction_mean = Long['Customer Satisfaction Score'].mean().round(1)
            Satisfaction_median = Long['Customer Satisfaction Score'].median().round(1)


            Statistics_F, Having_F, F_maintenance, F_issues = st.columns(4)
            Statistics_F.metric(label="Average customer satisfaction score",value= Satisfaction_mean)
            Statistics_F.metric(label="Median customer satisfaction score", value= Satisfaction_median)

            Having_F.metric(label="Still have our floor",
                            value=Having_floor_Yes)
            Having_F.metric(label="Do not still have our floor",
                            value=Having_floor_No)

            F_maintenance.metric(label="Remember floor maintenance",
                                 value=Maintenance_Yes)
            F_maintenance.metric(label="Do not remember floor maintenance",
                                 value=Maintenance_No)
            F_issues.metric(label="Floors have an issues",
                            value=Issue_Yes)
            F_issues.metric(label="Floors have no issues",
                            value=Issue_No)

            Long.sort_values(by='Converted Dates', ascending=True, inplace=True)

            Nine_month = Long.loc[Long['Record Type'] == '9 month Follow Up survey']
            One_year = Long.loc[Long['Record Type'] == '1 Year Follow Up survey']
            Two_year = Long.loc[Long['Record Type'] == '2 Years Follow Up survey']
            Three_year = Long.loc[Long['Record Type'] == '3 Years Follow Up survey']
            Four_year = Long.loc[Long['Record Type'] == '4 Years Follow Up survey']
            Five_year = Long.loc[Long['Record Type'] == '5 Years Follow Up survey']

            Long.set_index('Converted Dates', inplace=True)

            Nine_month1 = Nine_month.resample("M", on='Converted Dates').mean()
            One_year1 = One_year.resample("M", on='Converted Dates').mean()
            Two_year1 = Two_year.resample("M", on='Converted Dates').mean()
            Three_year1 = Three_year.resample("M", on='Converted Dates').mean()
            Four_year1 = Four_year.resample("M", on='Converted Dates').mean()
            Five_year1 = Five_year.resample("M", on='Converted Dates').mean()

            Nine_month2 = Nine_month1[['Customer Satisfaction Score']].dropna()
            One_year2 = One_year1[['Customer Satisfaction Score']].dropna()
            Two_year2 = Two_year1[['Customer Satisfaction Score']].dropna()
            Three_year2 = Three_year1[['Customer Satisfaction Score']].dropna()
            Four_year2 = Four_year1[['Customer Satisfaction Score']].dropna()
            Five_year2 = Five_year1[['Customer Satisfaction Score']].dropna()


            Column_time = ['Nine months', 'One year', 'Two years', 'Three years', 'Four years', 'Five years']
            Concatinated_data = pd.concat([Nine_month2, One_year2, Two_year2, Three_year2, Four_year2, Five_year2], axis=1)
            Concatinated_data.columns = Column_time
            Concatinated_data=Concatinated_data.reset_index()
            Concatinated_data = Concatinated_data.set_index('Converted Dates')

            st.header("Customer satisfaction score against time")
            st.line_chart(Concatinated_data)
            st.write("Generally, trend shows that customer satisfaction score decreases as time increases. Specifically, we have rapid decreases in customer satisfaction scores of 5 years Record Type")

            Nine_month = Long.loc[Long['Record Type'] == '9 month Follow Up survey']
            One_year = Long.loc[Long['Record Type'] == '1 Year Follow Up survey']
            Two_year = Long.loc[Long['Record Type'] == '2 Years Follow Up survey']
            Three_year = Long.loc[Long['Record Type'] == '3 Years Follow Up survey']
            Four_year = Long.loc[Long['Record Type'] == '4 Years Follow Up survey']
            Five_year = Long.loc[Long['Record Type'] == '5 Years Follow Up survey']

            Nine_months_Satisfaction_by_district = pd.DataFrame(
            Nine_month.groupby('Customer Opportunity: District')['Customer Satisfaction Score'].mean().round(2))
            One_year_Satisfaction_by_district = pd.DataFrame(
            One_year.groupby('Customer Opportunity: District')['Customer Satisfaction Score'].mean().round(2))
            Two_year_Satisfaction_by_district = pd.DataFrame(
            Two_year.groupby('Customer Opportunity: District')['Customer Satisfaction Score'].mean().round(2))
            Three_year_Satisfaction_by_district = pd.DataFrame(
            Three_year.groupby('Customer Opportunity: District')['Customer Satisfaction Score'].mean().round(2))
            Four_year_Satisfaction_by_district = pd.DataFrame(
            Four_year.groupby('Customer Opportunity: District')['Customer Satisfaction Score'].mean().round(2))
            Five_year_months_Satisfaction_by_district = pd.DataFrame(
            Five_year.groupby('Customer Opportunity: District')['Customer Satisfaction Score'].mean().round(2))

            Column_time = ['Nine months', 'One year', 'Two years', 'Three years', 'Four years', 'Five years']

            District_Customer_Scores = pd.concat([Nine_months_Satisfaction_by_district, One_year_Satisfaction_by_district, Two_year_Satisfaction_by_district,Three_year_Satisfaction_by_district, Four_year_Satisfaction_by_district,Five_year_months_Satisfaction_by_district], axis=1)
            District_Customer_Scores.columns = Column_time
            District_Customer_Scores_Concatinated_data = District_Customer_Scores.reset_index()

            H = District_Customer_Scores_Concatinated_data.reset_index(drop=True).transpose().reset_index()
            C = ['Opp type', 'Gatsibo', 'Kamonyi', 'Kayonza', 'Ngoma', 'Nyagatare', 'Rwamagana', 'Bugesera', 'Gasabo', 'Nyanza',
                 'Ruhango']
            H.columns = C
            H.drop(index=H.index[0], axis=0, inplace=True)
            L = H.set_index('Opp type').pct_change()
            L.drop(index=L.index[0], axis=0, inplace=True)
            st.header("Percentage change in customer satisfaction score")
            st.write(L)
        if Rad12=="Repair done":
            Repair = pd.read_excel('Repair_done_long_term_customer_satisfaction.xlsx')
            Repair= pd.DataFrame(Repair)
            Repair.replace(" ",np.nan)


            #Total area damaged
            Total_repaired_area_district = pd.DataFrame(Repair.groupby('Opportunity: District')['Size of damage in Sqm'].sum())
            Total_repaired_area_district.rename(columns={'Size of damage in Sqm': 'Total size of damage'}, inplace=True)
            st.header('The total area damaged in each district' )
            st.bar_chart(Total_repaired_area_district, width=1000, height=400, use_container_width=True)
            Total_area_repaired = Total_repaired_area_district['Total size of damage'].sum()

            st.write(f'The total damaged area that has been repaired in this program is {Total_area_repaired} sqm. The main damage types that are found on the field are cracks, roughness, and dents. The top district with the highest number of square meters damaged and repaired is Kamonyi.')
            #Damage types
            C = ['Types of damage', 'Counts']
            Types_Damage = pd.DataFrame(Repair['Types of damage'].value_counts()).reset_index()
            Types_Damage.columns = C

            Total_cracks = Types_Damage[Types_Damage['Types of damage'].str.contains('Cracks')]['Counts'].sum()  # extract in dataset where there is a ward cracks and sum their counts
            Total_Dents = Types_Damage[Types_Damage['Types of damage'].str.contains('Dents')]['Counts'].sum()
            Total_Roughness = Types_Damage[Types_Damage['Types of damage'].str.contains('Roughness')]['Counts'].sum()
            Total_wetness = Types_Damage[Types_Damage['Types of damage'].str.contains('Wet Floor')]['Counts'].sum()
            Damage_total_values = pd.DataFrame({'Damage types': ['Cracks', 'Dents', 'Roughness', 'Wetness'],'Total_counts': [Total_cracks, Total_Dents, Total_Roughness,Total_wetness]})


            # The plot
            fig_damage = go.Figure(
                go.Pie(
                    labels=Damage_total_values['Damage types'],
                    values=Damage_total_values['Total_counts'],
                    hoverinfo="label+percent",
                    textinfo="value"
                ))

            st.header("Types of damage")
            st.plotly_chart(fig_damage)
            st.write("44.8% of damage types in the forementioned districts are cracks, followed by dents and roughness. As a recommendation to R & D, we should focus on finding a sustainable solution to such damage types.")

            #TYPES OF REPAIR DONE
            st.header('Damage types and corresponding  repair approaches')
            Q = Repair.groupby('Types of Repair')['Types of damage']
            df3 = pd.concat([Q.value_counts(), Q.value_counts(normalize=True).mul(100)], axis=1,keys=('counts', 'percentage')).reset_index()
            st.write(df3)
            st.write("Some repair approaches do not correspond with damage types. For instance, we have four roughness damage, repaired with crack repair.")













    if Rad=="Moisture interventions":
        st.header("Moisture interventions")
        st.write(" In this section we will analyse moisture intervention pilot")
    if Rad=="Purchasing power test":
        st.header("Purchasing power test")
        st.write("In this section we will see trends clients purchasing power on different products under test. ")

    if Rad=="Discovery surveys":
        st.header("Discovery surveys")
        st.write("In this section we find and compare results from discovery surveys")






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


