import pickle
import streamlit as st 
import datetime
from geopy.distance import geodesic 
import numpy as np

bike= open('bike_demand_pred_model.pkl','rb')
regressor=pickle.load(bike)

card= open('card_default_pred_model.pkl','rb')
classifier=pickle.load(card)

#taxi= open('trip_time_pred_rfr.pkl','rb')
#taxi_regressor=pickle.load(taxi)

  

def main ():

    #activiteis = ["Home", "Bike sharing demand prediction",'Credit Card Default Prediction','Taxi Trip Time Prediction', "About","Contack Us","Error and Solutions"]
    activiteis = ["Home", "Bike sharing demand prediction",'Credit Card Default Prediction',"Contack Us"]
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

        if st.button("Predict count"):
            bike_count_result= regressor.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekend]])    
            st.success('{} number of bikes will be required '.format(round(int(bike_count_result))))

    if choice == "Credit Card Default Prediction":

        st.header('Credit Card Default Prediction')
        LIMIT_BAL = st.number_input("LIMIT_BAL",value =1000)

        sex=st.selectbox('sex',['Male','Female'])
        if sex=='Male':
            SEX_Male=1
            SEX_Female=0
        else:
            SEX_Male=0
            SEX_Female=1

        Education=st.selectbox('Education',['Graduate school','High School','University','Other'])
        if Education=='Graduate school':
            EDUCATION_graduate_school=1
            EDUCATION_high_school=0
            EDUCATION_university=0
            EDUCATION_other=0
        elif Education=="High School":
            EDUCATION_graduate_school=0
            EDUCATION_high_school=1
            EDUCATION_university=0
            EDUCATION_other=0  
        elif Education=="University":
            EDUCATION_graduate_school=0
            EDUCATION_high_school=0
            EDUCATION_university=1
            EDUCATION_other=0    
        else:
            EDUCATION_graduate_school=0
            EDUCATION_high_school=0
            EDUCATION_university=0
            EDUCATION_other=1

        Marital_status=st.selectbox('Marital status',['Married','Single','Others'])
        if Marital_status=="Married":
            MARRIAGE_married=1
            MARRIAGE_single=0
            MARRIAGE_others=0
        if Marital_status=="Single":
            MARRIAGE_married=0
            MARRIAGE_single=1
            MARRIAGE_others=0
        if Marital_status=="Others":
            MARRIAGE_married=0
            MARRIAGE_single=0
            MARRIAGE_others=1

        Age=st.number_input('Age',min_value=21,max_value=100)
        if Age<31:
            age_group_21_30=1
            age_group_31_40=0
            age_group_41_50=0
            age_group_51_60=0
            age_group_above_60=0
        if Age>=31 and Age<41:
            age_group_21_30=0
            age_group_31_40=1
            age_group_41_50=0
            age_group_51_60=0
            age_group_above_60=0
        if Age>=41 and Age<51:
            age_group_21_30=0
            age_group_31_40=0
            age_group_41_50=1
            age_group_51_60=0
            age_group_above_60=0
        if Age>=41 and Age<61:
            age_group_21_30=0
            age_group_31_40=0
            age_group_41_50=0
            age_group_51_60=1
            age_group_above_60=0
        else:
            age_group_21_30=0
            age_group_31_40=0
            age_group_41_50=0
            age_group_51_60=0
            age_group_above_60=1

        PAY_SEPT=st.number_input('PAY_SEPT',max_value=8,min_value=-2)
        PAY_AUG=st.number_input('PAY_AUG',max_value=8,min_value=-2)
        PAY_JUL=st.number_input('PAY_JUL',max_value=8,min_value=-2)
        PAY_JUN=st.number_input('PAY_JUN',max_value=8,min_value=-2)
        PAY_MAY=st.number_input('PAY_MAY',max_value=8,min_value=-2)
        PAY_APR=st.number_input('PAY_APR',max_value=8,min_value=-2)

        BILL_AMT_SEPT=st.number_input('BILL_AMT_SEPT', min_value=0)
        BILL_AMT_AUG=st.number_input('BILL_AMT_AUG', min_value=0)
        BILL_AMT_JUL=st.number_input('BILL_AMT_JUL', min_value=0)
        BILL_AMT_JUN=st.number_input('BILL_AMT_JUN', min_value=0)
        BILL_AMT_MAY=st.number_input('BILL_AMT_MAY', min_value=0)
        BILL_AMT_APR=st.number_input('BILL_AMT_APR', min_value=0)

        PAY_AMT_SEPT=st.number_input('PAY_AMT_SEPT', min_value=0)
        PAY_AMT_AUG=st.number_input('PAY_AMT_AUG', min_value=0)
        PAY_AMT_JUL=st.number_input('PAY_AMT_JUL', min_value=0)
        PAY_AMT_JUN=st.number_input('PAY_AMT_JUN', min_value=0)
        PAY_AMT_MAY=st.number_input('PAY_AMT_MAY', min_value=0)
        PAY_AMT_APR=st.number_input('PAY_AMT_APR', min_value=0)

        if st.button("Predict"):
            default_result= classifier.predict([[LIMIT_BAL, PAY_SEPT, PAY_AUG, PAY_JUL, PAY_JUN, PAY_MAY,
        PAY_APR, BILL_AMT_SEPT, BILL_AMT_AUG, BILL_AMT_JUL,
        BILL_AMT_JUN, BILL_AMT_MAY, BILL_AMT_APR, PAY_AMT_SEPT,
        PAY_AMT_AUG, PAY_AMT_JUL, PAY_AMT_JUN, PAY_AMT_MAY,
        PAY_AMT_APR, SEX_Female, SEX_Male, EDUCATION_graduate_school,
        EDUCATION_high_school, EDUCATION_other, EDUCATION_university,
        MARRIAGE_married, MARRIAGE_others, MARRIAGE_single,
        age_group_21_30, age_group_31_40, age_group_41_50,
        age_group_51_60, age_group_above_60]])

            if  int(default_result)==1:
                st.error('This person will default ')
            else:
                st.success('this person wil not default')

    if choice == "Taxi Trip Time Prediction":

        st.header('Taxi trip time prediction')

        pickup_longitude=st.number_input("pickup_longitude",value =-73.95104218,min_value=-122.0,max_value=-62.0)
        pickup_latitude=st.number_input("pickup_latitude",value =40.78575897,min_value=34.0,max_value=52.0)
        dropoff_longitude=st.number_input("dropoff_longitude",value =-73.96601868,min_value=-122.0,max_value=-62.0)
        dropoff_latitude=st.number_input("dropoff_latitude",value =40.75396729,min_value=34.0,max_value=44.0)
        distance=geodesic((pickup_latitude, pickup_longitude),(dropoff_latitude, dropoff_longitude)).km

        date = st.date_input("Date for demand prediction",datetime.date(2021, 4, 3))

        month=date.month
        pickup_months=['pickup_month_1', 'pickup_month_2','pickup_month_3', 'pickup_month_4', 'pickup_month_5', 'pickup_month_6']
        pickup_month_1= 0
        pickup_month_2= 0
        pickup_month_3= 0
        pickup_month_4= 0
        pickup_month_5= 0
        pickup_month_6= 0

        for month in pickup_months:
            if month[-1]==str(month):
                globals()[month] = 1
            else:
                globals()[month] = 0

        weekday=date.weekday()
        pickup_days=['pickup_day_0','pickup_day_1', 'pickup_day_2', 'pickup_day_3', 'pickup_day_4', 'pickup_day_5', 'pickup_day_6']
        pickup_day_0=0
        pickup_day_1=0
        pickup_day_2=0
        pickup_day_3=0
        pickup_day_4=0
        pickup_day_5=0
        pickup_day_6=0

        for day in pickup_days:
            if day[-1]==str(weekday):
                globals()[day] = 1
            else:
                globals()[day] = 0

        vendor_id=st.selectbox("vendor_id",[1,2],index=1)
        if vendor_id==1:
            vendor_id_1=1
            vendor_id_2=0
        else:
            vendor_id_1=0
            vendor_id_2=1 

        store_and_fwd_flag=st.selectbox("store_and_fwd_flag",['yes','no'],index=1)
        if store_and_fwd_flag=='yes':
            store_and_fwd_flag_Y=1
            store_and_fwd_flag_N=0
        else:
            store_and_fwd_flag_Y=0
            store_and_fwd_flag_N=1


        passenger_count=st.selectbox("passenger_count",[1,2,3,4,5,6],index=1)
        passengers_conts=['passenger_count_1', 'passenger_count_2', 'passenger_count_3',
       'passenger_count_4', 'passenger_count_5', 'passenger_count_6',]
        passenger_count_1=0
        passenger_count_2=0
        passenger_count_3=0
        passenger_count_4=0
        passenger_count_5=0
        passenger_count_6=0
        for num in passengers_conts:
            if num[-1]==str(passenger_count):
                globals()[num] = 1
            else:
                globals()[num] = 0

        pickup_period=st.slider("Hour",value =20,max_value=23,min_value=0)
        if pickup_period in range(6,12):
            pickup_period_Morning=1
            pickup_period_Afternoon=0
            pickup_period_Evening=0
            pickup_period_Night=0
        if pickup_period in range(12,17):
            pickup_period_Morning=0
            pickup_period_Afternoon=1
            pickup_period_Evening=0
            pickup_period_Night=0
        if pickup_period in range(17,24):
            pickup_period_Morning=0
            pickup_period_Afternoon=0
            pickup_period_Evening=1
            pickup_period_Night=0
        else:
            pickup_period_Morning=0
            pickup_period_Afternoon=0
            pickup_period_Evening=0
            pickup_period_Night=1

        #array=np.array([[-73.96896362,  40.76061249, -73.9793396 ,  40.76063538,
                                            #0.8761391 ,   0.        ,   1.        ,   1.        ,
                                            #0.        ,   0.        ,   0.        ,   0.        ,
                                            #0.        ,   0.        ,   0.        ,   0.        ,
                                            #0.        ,   0.        ,   1.        ,   0.        ,
                                           # 0.        ,   0.        ,   1.        ,   0.        ,
                                            #0.        ,   0.        ,   0.        ,   1.        ,
                                            #0.        ,   0.        ]])
        #result= taxi_regressor.predict(array)

        '''result= taxi_regressor.predict([[pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,distance,vendor_id_1,vendor_id_2,passenger_count_1,
                                    passenger_count_2,passenger_count_3,passenger_count_4,passenger_count_5,passenger_count_6,
                                    pickup_day_0,pickup_day_1,pickup_day_2,pickup_day_3,pickup_day_4,pickup_day_5,pickup_day_6,pickup_month_1,pickup_month_2,
                                    pickup_month_3,pickup_month_4,pickup_month_5,pickup_month_6,pickup_period_Afternoon,pickup_period_Evening,pickup_period_Morning,
                                    pickup_period_Night]])'''
        
        '''if st.button("Predict count"):
            st.success('The Trip will take {} minutes'.format(round(int(result/60)))) '''

    if choice == "About":
        pass




    elif choice == "Contack Us":
        st.header("Contact Details")
        st.write(""" LinkedIn profile Link""")
        st.write(""" >* [Ali Asgar Lakadwala] (https://www.linkedin.com/in/ali-asgar-lakdawala/)""")
        st.write("""Email Id""")
        st.write(""">* Ali Asgar Lakadwala : aliasgarlakdawala0209@gmail.com""")

if __name__ == '__main__':
    main()