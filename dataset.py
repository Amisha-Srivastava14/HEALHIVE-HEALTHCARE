import pandas as pd
import random

# Symptoms
symptoms = [
    "Fever",
    "Cough",
    "Shortness of breath",
    "Fatigue",
    "Headache",
    "Muscle or body aches",
    "Sore throat",
    "Loss of taste or smell",
    "Nausea or vomiting",
]

# Chronic Diseases and their corresponding cures
chronic_diseases = {
    "Hypertension": "Treatment of hypertension typically involves lifestyle changes (such as reducing salt intake, exercising regularly, and maintaining a healthy weight) and medications prescribed by a healthcare professional.",
    "High Cholesterol": "Management of high cholesterol involves lifestyle modifications such as following a healthy diet, regular exercise, and sometimes medication (such as statins) as prescribed by a healthcare professional.",
    "Arthritis": "Treatment for arthritis focuses on managing symptoms and improving quality of life. This may include medications, physical therapy, lifestyle changes, and in severe cases, surgery.",
    "Diabetes": "Management of diabetes involves lifestyle modifications such as regular exercise, a healthy diet, monitoring blood sugar levels, and sometimes medication or insulin therapy.",
    "Chronic Kidney Disease": "Treatment for chronic kidney disease focuses on managing symptoms, slowing disease progression, and preventing complications. This may include lifestyle changes, medications, and in severe cases, dialysis or kidney transplant.",
    "Heart Problem": "Management of heart problems often involves lifestyle changes (such as quitting smoking, eating a healthy diet, exercising regularly, and managing stress) and medications to control symptoms and reduce the risk of complications.",
    "Malaria": "Treatment for malaria involves antimalarial medications prescribed by a healthcare professional. The choice of medication depends on factors such as the type of malaria and the severity of the illness.",
    "Dengue": "There is no specific treatment for dengue fever. Management involves supportive care to relieve symptoms, such as rest, hydration, and pain relief medications. In severe cases, hospitalization may be necessary.",
    "Cancer": "Treatment for cancer varies depending on the type, stage, and other factors. It may include surgery, chemotherapy, radiation therapy, immunotherapy, targeted therapy, hormone therapy, or a combination of these treatments.",
}

# Generate synthetic dataset
data = []
for _ in range(500):
    symptoms_row = [random.choice([0, 1]) for _ in range(len(symptoms))]  # Randomly generate 0 or 1 for each symptom
    chronic_disease = random.choice(list(chronic_diseases.keys()))  # Randomly select a chronic disease
    cure = chronic_diseases[chronic_disease]  # Get the corresponding cure for the selected disease
    row = symptoms_row + [chronic_disease, cure]
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=symptoms + ["Chronic Disease", "Cure"])

# Save DataFrame to Excel
df.to_excel("disease_dataset.xlsx", index=False)
