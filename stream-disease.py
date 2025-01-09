import pickle
import streamlit as st

# membaca model
disease_model = pickle.load(open('disease_model.sav', 'rb'))

# judul web
st.title('Disease Diagnosis')

#membagi kolom
col1, col2 = st.columns(2)

with col1:
    Age = st.text_input ('Umur')

with col2:
    Symptom_1 = st.text_input ('Gejala 1')

with col1:
    Symptom_1 = st.text_input ('Gejala 2')

with col2:
    Heart_Rate_bpm = st.text_input ('Denyut Jantung')

with col1:
    Body_Temperature_C = st.text_input ('Suhu Tubuh')

with col2:
    Blood_Pressure_mmHg = st.text_input ('Tekanan Darah')

with col1:
    Oxygen_Saturation = st.text_input ('Saturasi Oksigen')

with col2:
    Diagnosis = st.text_input ('Diagnosa')

with col1:
    Severity = st.text_input ('Tingkat Keparahan')

# code untuk prediksi
disease_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi disease'):
    disease_prediction = disease_model.predict([[Age, Symptom_1, Symptom_1, Heart_Rate_bpm, Body_Temperature_C, Blood_Pressure_mmHg, Oxygen_Saturation, Diagnosis, Severity]])

    if(disease_prediction[0] == 1):
        disease_diagnosis = 'Pasien Mengkonsumsi Obat dan Istirahat'
    else :
        disease_diagnosis = 'Pasien Memerlukan Perawatan Medis dan Obat-Obatan'

    st.success(disease_diagnosis)