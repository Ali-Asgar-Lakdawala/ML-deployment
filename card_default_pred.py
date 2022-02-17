class Card_Default_Pred():
    def __init__(self):

        import streamlit as st 
        import pickle


        pickle_in= open('card_default_pred_model.pkl','rb')
        classifier=pickle.load(pickle_in)

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