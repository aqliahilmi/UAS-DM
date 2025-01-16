import pickle
import streamlit as st

# Load model yang sudah dilatih
model = pickle.load(open('/mount/src/uas-dm/estimasi_tumbuhan.sav', 'rb'))

# Judul aplikasi
st.title('Estimasi Harga Tumbuhan')

# Input pengguna
jenis_tumbuhan = st.selectbox('Pilih Jenis Tumbuhan', ['Monstera', 'Kaktus', 'Anggrek', 'Lainnya'])
ukuran_pot = st.number_input('Input Ukuran Pot (cm)', min_value=5, max_value=100, step=1)
tinggi_tumbuhan = st.number_input('Input Tinggi Tumbuhan (cm)', min_value=10, max_value=300, step=1)
umur_tumbuhan = st.number_input('Input Umur Tumbuhan (bulan)', min_value=1, max_value=120, step=1)
kondisi_tumbuhan = st.selectbox('Kondisi Tumbuhan', ['Sehat', 'Kurang Sehat'])

# Konversi input ke bentuk yang dapat digunakan oleh model
jenis_mapping = {'Monstera': 1, 'Kaktus': 2, 'Anggrek': 3, 'Lainnya': 4}
kondisi_mapping = {'Sehat': 1, 'Kurang Sehat': 0}

jenis_tumbuhan_encoded = jenis_mapping[jenis_tumbuhan]
kondisi_tumbuhan_encoded = kondisi_mapping[kondisi_tumbuhan]

# Prediksi harga
tombol_prediksi = st.button('Estimasi Harga')

if tombol_prediksi:
    predict = model.predict(
        [[jenis_tumbuhan_encoded, ukuran_pot, tinggi_tumbuhan, umur_tumbuhan, kondisi_tumbuhan_encoded]]
    )
    st.write('Estimasi harga tumbuhan dalam IDR: Rp', predict[0])
