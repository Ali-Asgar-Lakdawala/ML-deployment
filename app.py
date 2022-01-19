import numpy as np
import pickle
import pandas as pd
import streamlit as st 

pickle_in= open('finalized_model.pkl','rb')
regressor=pickle.load(pickle_in)


def predict_bike_number(Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend):

    prediction = regressor.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend]])

    return {'prediction': prediction}

    

def main ():
    # Face Analysis Application #
    st.title("Real Time Face Emotion Detection Application")
    activiteis = ["Home", "Bike sharing demand prediction", "About","Contack Us","Error and Solutions"]
    choice = st.sidebar.selectbox("Select Activity", activiteis)

    if choice == "Home":
        html_temp_home1 = """<div style="background-color:#6D7B8D;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Bike sharing demand prediction.</h4>
                                            </div>
                                            </br>"""

    if choice == "Bike sharing demand prediction":                                       
        Seasons = st.selectbox("Seasons",['Spring','Summer','Winter','Autumn'])
        if Seasons=='Spring':
            Seasons_Spring = 1
            Seasons_Summer = 0
            Seasons_Winter = 0
        elif Seasons=='Summer':
            Seasons_Spring = 0
            Seasons_Summer = 1
            Seasons_Winter = 0
        elif Seasons=='Autumn':
            Seasons_Spring = 0
            Seasons_Summer = 0
            Seasons_Winter = 0  
        else:
            Seasons_Spring = 0
            Seasons_Summer = 0
            Seasons_Winter = 1

        Holiday=st.checkbox('Holiday', value=False)
        if Holiday==0:
            Holiday_No_Holiday=0
        else :
            Holiday_No_Holiday=1

        Functioning_Day=st.checkbox('Functioning_Day', value=False)
        if Functioning_Day==0:
            Functioning_Day_Yes=0
        else :
            Functioning_Day_Yes=1
        Hour = st.number_input("Hour",value =15,max_value=23,min_value=1)
        Temperature_C = st.number_input("Temperature_C",value =16)
        Humidity_per = st.number_input("Humidity_per",value =14)
        Wind_speed_m_per_sec = st.number_input("Wind_speed_m_per_sec",value =2.2)
        Visibility_10m = st.number_input("Visibility_10m",value =1828)
        Dew_point_temp_c = st.number_input("Dew_point_temp_c",value =15)
        Solar_Radiation = st.number_input("Solar_Radiation",value =2.33)
        Rainfall_mm = st.number_input("Rainfall_mm",value =0)
        Snowfall_cm = st.number_input("Snowfall_cm",value =0)
        month = st.number_input("month",value =3,max_value=12,min_value=1)
        weekend = st.selectbox("weekend",['yes','no'])
        if weekend=='yes':
            weekdays_weekend = 1
        else :
            weekdays_weekend = 0

        if st.button("Predict"):
            result=predict_bike_number(Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                        ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend)    
            st.success('The output is {}'.format(result))

    elif choice == "Contack Us":
        st.header("Contact Details")
        st.write(""" LinkedIn profile Link""")
        st.write(""" >* [Ali Asgar Lakadwala] (https://www.linkedin.com/in/ali-asgar-lakdawala/)""")
        st.write("""Email Id""")
        st.write(""">* Ali Asgar Lakadwala : aliasgarlakdawala0209@gmail.com""")



if __name__ == '__main__':
    main()