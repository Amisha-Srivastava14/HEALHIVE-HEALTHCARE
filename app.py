import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_excel("disease_dataset.xlsx")

# Separate features (symptoms) and target (chronic disease)
X = df.iloc[:, :-2]  # Features (excluding last 2 columns: Chronic Disease and Cure)
y = df.iloc[:, -2]   # Target (Chronic Disease)
cures = df.set_index("Chronic Disease")["Cure"].to_dict()  # Create a dictionary mapping diseases to cures

# Label encode the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Streamlit UI
st.title("Disease Prediction model")

# Get user input for symptoms
symptom_inputs = {}
for symptom in X.columns:
    symptom_inputs[symptom] = st.selectbox(f"Select {symptom}:", ["No", "Yes"])

# Function to make prediction
# Function to make prediction
def make_prediction(symptom_inputs):
    # Check if all symptoms are 'No'
    if all(value == "No" for value in symptom_inputs.values()):
        return "No disease detected"
    
    # Convert user input to numerical format
    for symptom, input_value in symptom_inputs.items():
        if input_value == "No":
            symptom_inputs[symptom] = 0
        else:
            symptom_inputs[symptom] = 1

    # Convert user input to DataFrame
    user_input_df = pd.DataFrame([symptom_inputs])

    # Make prediction
    prediction = model.predict(user_input_df)
    predicted_disease = label_encoder.inverse_transform(prediction)
    return predicted_disease[0]

# Prediction button
if st.button("Predict Disease"):
    predicted_disease = make_prediction(symptom_inputs)
    st.subheader("Predicted Disease:")
    st.write(predicted_disease)
    
    # Find cure for predicted disease
    if predicted_disease in cures:
        predicted_cure = cures[predicted_disease]
        st.subheader("Cure:")
        st.write(predicted_cure)
    else:
        st.write("Cure not found for the predicted disease.")
    
    # Message recommending to get doctor's advice
    st.write("WE RECOMMEND SEEKING DOCTOR'S ADVISE If CONDITION IS SERIOUS.")
