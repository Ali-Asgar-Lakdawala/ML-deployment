
class Bike_Demand():


    def __init__(self):

        import streamlit as st 
        import datetime
        import pickle

        pickle_in= open('bike_demand_pred_model.pkl','rb')
        regressor=pickle.load(pickle_in)

        st.header('Bike sharing demand prediction')                                   

        date = st.date_input("Date for demand prediction",datetime.date(2021, 3, 6))
        month=date.month
        weekday=date.weekday()

        if weekday > 4:
            weekend = 1
        else :
            weekend = 0

        Hour = st.slider("Hour",value =15,max_value=23,min_value=0)
        Holiday=st.checkbox('Holiday', value=True)
        if Holiday==0:
            Holiday_No_Holiday=0
        else :
            Holiday_No_Holiday=1

        Functioning_Day=st.checkbox('Functioning_Day', value=True)
        if Functioning_Day==0:
            Functioning_Day_Yes=0
        else :
            Functioning_Day_Yes=1

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
        Temperature_C = st.number_input("Temperature_C",value =16)
        Humidity_per = st.number_input("Humidity_per",value =14)
        Wind_speed_m_per_sec = st.number_input("Wind_speed_m_per_sec",value =2.2)
        Visibility_10m = st.number_input("Visibility_10m",value =1828)
        Dew_point_temp_c = st.number_input("Dew_point_temp_c",value =-15)
        Solar_Radiation = st.number_input("Solar_Radiation",value =2.33)
        Rainfall_mm = st.number_input("Rainfall_mm",value =0)
        Snowfall_cm = st.number_input("Snowfall_cm",value =0)

        result= regressor.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekend]])
        
        if st.button("Predict count"):
            st.success('The output is {}'.format(result)) 

        