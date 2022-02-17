import pickle
import streamlit as st 

pickle_in= open('bike_demand_pred_model.pkl','rb')
regressor=pickle.load(pickle_in)

pickle_in= open('card_default_pred_model.pkl','rb')
classifier=pickle.load(pickle_in)
  

def main ():

    activiteis = ["Home", "Bike sharing demand prediction",'Credit Card Default Prediction', "About","Contack Us","Error and Solutions"]
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

        if st.button("Predict count"):
            result= regressor.predict([[Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_No_Holiday,Functioning_Day_Yes,Hour,Temperature_C,Humidity_per
                                    ,Wind_speed_m_per_sec,Visibility_10m,Dew_point_temp_c,Solar_Radiation,Rainfall_mm,Snowfall_cm,month,weekdays_weekend]])    
            st.success('The output is {}'.format(result))

    elif choice == "Contack Us":
        st.header("Contact Details")
        st.write(""" LinkedIn profile Link""")
        st.write(""" >* [Ali Asgar Lakadwala] (https://www.linkedin.com/in/ali-asgar-lakdawala/)""")
        st.write("""Email Id""")
        st.write(""">* Ali Asgar Lakadwala : aliasgarlakdawala0209@gmail.com""")


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
            st.success('The output is {}'.format(default_result))

if __name__ == '__main__':
    main()