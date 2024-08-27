import numpy as np

import pickle

import streamlit as st



# Loading the saved model 

loaded_model = pickle.load(open('./trained_model.sav','rb'))



# Create a function for prediction

def heart_disease_prediction(input_data):

    

    # Convert the input data to a numpy array

    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    

    # Reshape the numpy array as we are predicting for only one instance

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    

    # Make the prediction

    prediction = loaded_model.predict(input_data_reshaped)

    

    if prediction[0] == 0:

        return 'The Person has a Healthy Heart'

    else:

        return 'The Person has Heart Disease'



def main():

    

    # Giving a title

    st.title('Heart Disease Prediction Web App')

    

    # Getting the input data from the user

    Age = st.text_input('Age')

    Sex = st.text_input('Sex (1 = Male, 0 = Female)')

    Chest_pain_type = st.text_input('Chest pain type (0-3)')

    BP = st.text_input('BP (Blood Pressure)')

    Cholesterol = st.text_input('Cholesterol')

    FBS_over_120 = st.text_input('FBS over 120 (1 = True, 0 = False)')

    EKG_results = st.text_input('EKG results (0-2)')

    Max_HR = st.text_input('Max HR (Maximum Heart Rate)')

    Exercise_angina = st.text_input('Exercise angina (1 = Yes, 0 = No)')

    ST_depression = st.text_input('ST depression')

    Slope_of_ST = st.text_input('Slope of ST (0-2)')

    Number_of_vessels_fluro = st.text_input('Number of vessels fluro (0-3)')

    Thallium = st.text_input('Thallium (3 = Normal, 6 = Fixed Defect, 7 = Reversible Defect)')

    

    # Convert inputs to appropriate types

    try:

        Age = int(Age)

        Sex = int(Sex)

        Chest_pain_type = int(Chest_pain_type)

        BP = int(BP)

        Cholesterol = int(Cholesterol)

        FBS_over_120 = int(FBS_over_120)

        EKG_results = int(EKG_results)

        Max_HR = int(Max_HR)

        Exercise_angina = int(Exercise_angina)

        ST_depression = float(ST_depression)

        Slope_of_ST = int(Slope_of_ST)

        Number_of_vessels_fluro = int(Number_of_vessels_fluro)

        Thallium = int(Thallium)

        

        # Code for prediction

        diagnosis = ''

        

        # Creating a button for prediction

        if st.button('Heart Test Result'):

            diagnosis = heart_disease_prediction([Age, Sex, Chest_pain_type, BP, Cholesterol, FBS_over_120, EKG_results, Max_HR, Exercise_angina, ST_depression, Slope_of_ST, Number_of_vessels_fluro, Thallium])

        

        st.success(diagnosis)

    

    except ValueError:

        st.error("Please enter valid numeric values for all fields.")



if __name__ == '__main__':

    main()
