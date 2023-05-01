import pickle
import streamlit as st

model_perokok = pickle.load(open('perokok-model.sav', 'rb'))
st.title('Prediksi Perokok Aktif Menggunakan Algoritma Logistic Regression')

gender = st.text_input("Jenis Kelamin (0=Perempuan 1=Laki Laki)")
age = st.text_input("Umur")
height = st.text_input("Tinggi Badan")
weight = st.text_input("Berat Badan")
waist = st.text_input("Ukuran Pinggang")
eyesight_left = st.text_input("Pandangan Mata Kiri")
eyesight_right = st.text_input("Pandangan Mata Kanan")
hearing_left = st.text_input("Pendengaran Kiri")
hearing_right = st.text_input("Pendengaran Kanan")
systolic = st.text_input("Tekanan Darah Jantung")
relaxation = st.text_input("Angka Relaksasi")
fasting_blood_sugar = st.text_input("Tekanan Gula darah")
cholesterol = st.text_input("Kolesterol")
triglyceride = st.text_input("Trigliserida")
hdl = st.text_input("HDL")
ldl = st.text_input("LDL")
hemoglobin = st.text_input("Hemoglobin")
urine_protein = st.text_input("Protein pada urin")
serum_creatinine = st.text_input("Serum Seratin")
ast = st.text_input("AST")
alt = st.text_input("ALT")
gtp = st.text_input("GTP")
oral = st.text_input("Kondisi Mulut (1=Y 0=N)")
dental_caries = st.text_input("Karies Pada Gigi")
tartar = st.text_input("Status Tartar (1=Y 0=N)")

perokok_hasil = ''

if st.button("PREDIKSI!"):
    perokok_pred = model_perokok.predict([[gender, age, height, weight, waist, eyesight_left, eyesight_right, hearing_left, hearing_right, systolic, relaxation,
                                         fasting_blood_sugar, cholesterol, triglyceride, hdl, ldl, hemoglobin, urine_protein, serum_creatinine, ast, alt, gtp, oral, dental_caries, tartar]])
    if(perokok_pred == 0):
        perokok_hasil = "Pasien BUKAN perokok"
        st.success(perokok_hasil)
    else:
        perokok_hasil = "Pasien PEROKOK"
        st.warning(perokok_hasil)
