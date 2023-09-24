import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
img= Image.open('favicon.ico')
st.set_page_config(page_title='Chikitsha', page_icon=img,initial_sidebar_state="expanded",layout="wide")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# loading the saved models
diabetes_model = pickle.load(open('A:\PROJECT\major\saved models\diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('A:\PROJECT\major\saved models\heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('A:\PROJECT\major\saved models\parkinsons_model.sav', 'rb'))

with st.sidebar:    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Home','Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          icons=['house','activity','heart','person'],menu_icon="cast",default_index=0)
    selected

if (selected == 'Home'):
    st.header(" Chikitsha: A Medical Web Application")
    img = Image.open("background2.jpg")
    st.image(img)
    
    
    
    with st.container():
        st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://static.streamlit.io/examples/cat.jpg")
        }
        </style>
        """,unsafe_allow_html=True)
        tab1, tab2, tab3 = st.tabs(["Heart", "Diabetes", "Parkinson's"])

        with tab1:
            st.header("Heart Diseases")
            st.write("Studies show that there are several sources that are responsible for any kind of heart disease and data is collected from such sources. This results in constructing the structure of the database. To resolve the heart disease prediction-related issues, the NB (Naive Bayesian) classification and KNN algorithm are considered for the prediction of disease. Dataset of this study includes fields like age, types of chest pain, blood pressure, cholesterol level, blood sugar level, etc.")
        with tab2:
            st.header("Diabetes")
            st.write("From many studies, it is found that the factors which play role in the detection of diabetes are pregnancies, glucose level, blood pressure, skin thickness values, insulin level and others")
        with tab3:
            st.header("Parkinson's")
            st.write("Diagnosis of Parkinson's disease (PD) is commonly based on medical observations and assessment of clinical signs, including the characterization of a variety of motor symptoms. However, traditional diagnostic approaches may suffer from subjectivity as they rely on the evaluation of movements that are sometimes subtle to human eyes and therefore difficult to 7 classify, leading to possible misclassification. In the meantime, early non-motor symptoms of PD may be mild and can be caused by many other conditions. Therefore, these symptoms are often overlooked, making diagnosis of PD at an early stage challenging. To address these difficulties and to refine the diagnosis and assessment procedures of PD, machine learning methods have been implemented for the classification of PD and healthy controls or patients with similar clinical presentations (e.g., movement disorders or other Parkinsonian syndromes).")

        

    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        img = Image.open("dia.jpg")
        st.image(img)

    # page title
    st.title('Diabetes Test')
    
    
    # getting the input data from the user
    col1, col2, col3, col4= st.columns(4)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col4:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col1:
        Insulin = st.text_input('Insulin Level')
    
    with col2:
        BMI = st.text_input('BMI')
    
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col4:
        Age = st.text_input('Age')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Check Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Diabetic please prefer to doctor'
        else:
          diab_diagnosis = 'NOT Diabetic! Precations should be taken'
        
    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        img = Image.open("heart.jpg")
        st.image(img)
    
    # page title
    st.title('Heart Disease Prediction')
    
    col1, col2, col3,col4 = st.columns(4)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col4:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col3:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col4:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col1:
        exang = st.text_input('Exercise Induced Angina')
        
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col4:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal;\n 1 = fixed defect;\n 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        img = Image.open("park5.png")
        st.image(img)
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
