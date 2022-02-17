import streamlit as st
from bike_demand import Bike_Demand
from card_default_pred import Card_Default_Pred
from trip_time_pre import Trip_Time_Pred
import pickle


def main ():

    activiteis = ["Home", "Bike sharing demand prediction",'Credit Card Default Prediction','Taxi Trip Time Prediction', "About","Contack Us","Error and Solutions"]
    choice = st.sidebar.selectbox("Select Activity", activiteis)

    if choice == "Home":
        st.title("Wellcome aliens")
        st.header('Select a ML project from the sidebar')       
        html_temp_home1 = """<div style="background-color:#6D7B8D;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Bike sharing demand prediction.</h4>
                                            </div>
                                            </br>"""

    if choice == "Bike sharing demand prediction":  
        Bike_Demand()

    if choice == "Credit Card Default Prediction":
        Card_Default_Pred()

    if choice == "Taxi Trip Time Prediction":
        Trip_Time_Pred()

    elif choice == "Contack Us":
        st.header("Contact Details")
        st.write(""" LinkedIn profile Link""")
        st.write(""" >* [Ali Asgar Lakadwala] (https://www.linkedin.com/in/ali-asgar-lakdawala/)""")
        st.write("""Email Id""")
        st.write(""">* Ali Asgar Lakadwala : aliasgarlakdawala0209@gmail.com""")

if __name__ == '__main__':
    main()