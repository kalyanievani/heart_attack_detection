import gradio as gr
import joblib
import numpy as np
xgb_clf = joblib.load('app/trained_model/xgboost-model.pkl')
def predict_death_event(age, anaemia, high_blood_pressure, creatinine_phosphokinase, diabetes, ejection_fraction, platelets, sex, serum_creatinine, serum_sodium, smoking, time):
  death = xgb_clf.predict(np.array([age, anaemia, high_blood_pressure, creatinine_phosphokinase, diabetes, ejection_fraction, platelets, sex, serum_creatinine, serum_sodium, smoking, time]).reshape(1, -1)) 
  return death[0]
  
inputs = [
    gr.Slider(20, 100, label="Age"),
    gr.Radio([0, 1], label="Anaemia (0=No, 1=Yes)"),
    gr.Radio([0, 1], label="High Blood Pressure (0=No, 1=Yes)"),
    gr.Slider(0, 8000, label="Creatinine Phosphokinase (mcg/L)"),
    gr.Radio([0, 1], label="Diabetes (0=No, 1=Yes)"),
    gr.Slider(10, 80, label="Ejection Fraction (%)"),
    gr.Slider(20000, 850000, label="Platelets (kiloplatelets/mL)"),
    gr.Radio([0, 1], label="Sex (0=Female, 1=Male)"),
    gr.Slider(0.5, 10.0, label="Serum Creatinine (mg/dL)"),
    gr.Slider(100, 150, label="Serum Sodium (mEq/L)"),
    gr.Radio([0, 1], label="Smoking (0=No, 1=Yes)"),
    gr.Slider(0, 300, label="Follow-up Time (days)")
]
# Output response
# YOUR CODE HERE
output = gr.Textbox(label="Prediction Result")

title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

iface = gr.Interface(fn = predict_death_event,
                         inputs = inputs,
                         outputs = output,
                         title = title,
                         description = description,
                         allow_flagging='never')

iface.launch(server_name="0.0.0.0", server_port=7860)