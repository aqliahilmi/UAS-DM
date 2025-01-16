# UAS-DATA MINING

## Deskripsi Proyek
Proyek ini berfokus pada estimasi tumbuhan menggunakan model machine learning. Dataset yang digunakan mencakup data berbagai jenis tumbuhan dan karakteristiknya. Model yang telah dilatih disimpan dalam format `.sav` untuk digunakan kembali.

## Struktur File
- **estimasiTumbuhan.ipynb**: Notebook Jupyter yang berisi kode untuk eksplorasi data, pelatihan model, dan evaluasi.
- **estimasi_tumbuhan.csv**: Dataset utama yang digunakan untuk melatih model.
- **estimasi_tumbuhan.py**: Skrip Python yang dapat dijalankan untuk melakukan estimasi.
- **estimasi_tumbuhan.sav**: Model machine learning yang telah dilatih dan disimpan.
- **Iris.csv**: Dataset tambahan yang digunakan dalam analisis.

## Cara Menggunakan
1. **Jalankan Notebook**: Buka `estimasiTumbuhan.ipynb` di Jupyter Notebook dan jalankan sel secara berurutan.
2. **Gunakan Skrip Python**: Jalankan `estimasi_tumbuhan.py` untuk melakukan estimasi menggunakan model yang sudah dilatih.
3. **Model yang Disimpan**: Gunakan file `estimasi_tumbuhan.sav` untuk memuat model dan melakukan prediksi pada data baru.

## Persyaratan
- Python 3.x
- Pandas
- Scikit-learn
- Jupyter Notebook (opsional)
- NumPy
- Matplotlib
- Seaborn

## Instalasi dan Setup
1. Pastikan Python 3.x telah terinstal.
2. Instal pustaka yang diperlukan dengan menjalankan perintah berikut:
   ```sh
   pip install pandas scikit-learn numpy matplotlib seaborn
   ```
3. Buka Jupyter Notebook jika ingin menjalankan `estimasiTumbuhan.ipynb`:
   ```sh
   jupyter notebook
   ```

## Penjelasan Model
Model yang digunakan dalam proyek ini merupakan model supervised learning yang dilatih menggunakan algoritma regresi dan klasifikasi. Model ini mampu melakukan estimasi berdasarkan dataset yang tersedia dan memberikan prediksi terhadap data baru. 

Teknik yang digunakan meliputi:
- **Preprocessing Data**: Normalisasi dan pembersihan dataset.
- **Feature Engineering**: Pemilihan fitur yang relevan untuk meningkatkan akurasi model.
- **Training dan Evaluasi**: Melatih model dengan dataset dan mengevaluasi performanya menggunakan metrik seperti akurasi, precision, recall, dan F1-score.

## Kontribusi
Jika Anda ingin berkontribusi dalam proyek ini:
1. Fork repositori ini.
2. Buat branch baru (`feature-branch`).
3. Lakukan perubahan yang diperlukan.
4. Kirim pull request untuk direview.

## Lisensi
Proyek ini bebas digunakan untuk keperluan akademik dan penelitian. Jika menggunakan proyek ini dalam publikasi, harap cantumkan sumbernya.

