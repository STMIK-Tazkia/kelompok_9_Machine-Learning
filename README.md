# Proposal Penelitian  
## Prediksi Jumlah Penjualan Minuman Berdasarkan Suhu Harian  
### Menggunakan Deep Learning (Neural Network)

---

### Disusun Oleh
- **Denvi Sekartazi Iskandar** (241552010020)  
- **Muhammad Ma’rufil Kurhi** (241552010002)

### Dosen Pengampu  
Hendri Karisma, S.Kom., M.T.

### Institusi  
Fakultas Ilmu Komputer  
Jurusan Teknik Informatika  
Sekolah Tinggi Manajemen Ilmu Komputer Tazkia (STMIK Tazkia)

---

## BAB I – PENDAHULUAN

### 1.1 Latar Belakang
Perkembangan teknologi komputasi dan kecerdasan buatan telah mendorong pemanfaatan data secara intensif dalam berbagai bidang, termasuk analisis dan prediksi penjualan. Prediksi penjualan yang akurat memiliki peran penting dalam perencanaan stok, strategi pemasaran, serta pengambilan keputusan bisnis.

Salah satu faktor eksternal yang memengaruhi tingkat penjualan minuman adalah **suhu udara harian**, di mana peningkatan suhu umumnya diikuti oleh meningkatnya konsumsi minuman. Metode prediksi konvensional seperti **Linear Regression** memiliki keterbatasan dalam menangani hubungan data yang bersifat non-linear.

**Deep Learning**, khususnya **Neural Network**, mampu mempelajari pola kompleks dan hubungan non-linear melalui banyak lapisan tersembunyi (*hidden layers*). Oleh karena itu, penelitian ini menerapkan metode Deep Learning untuk meningkatkan akurasi prediksi penjualan minuman berdasarkan suhu harian.

---

### 1.2 Rumusan Masalah
1. Bagaimana pengaruh suhu harian terhadap jumlah penjualan minuman?
2. Bagaimana penerapan metode Deep Learning berbasis Neural Network dalam prediksi penjualan?
3. Bagaimana arsitektur Neural Network yang optimal untuk permasalahan ini?
4. Bagaimana perbandingan kinerja Deep Learning dengan metode machine learning tradisional?
5. Seberapa akurat hasil prediksi berdasarkan metrik evaluasi yang digunakan?

---

### 1.3 Tujuan Penelitian
1. Menganalisis hubungan suhu harian terhadap jumlah penjualan minuman.
2. Menerapkan metode Deep Learning berbasis Neural Network.
3. Merancang arsitektur model Deep Learning yang sesuai.
4. Membandingkan performa Deep Learning dengan metode tradisional.
5. Mengevaluasi akurasi model prediksi.

---

### 1.4 Manfaat Penelitian
- Memberikan pemahaman penerapan Deep Learning dalam prediksi penjualan.
- Membantu pelaku usaha dalam perencanaan stok dan strategi penjualan.
- Menjadi referensi bagi penelitian selanjutnya di bidang prediksi penjualan.

---

## BAB II – DESKRIPSI DATASET

### 2.1 Sumber Dataset
Dataset yang digunakan merupakan **data simulasi** berdasarkan suhu harian dan jumlah penjualan minuman selama periode tertentu (±30 hari) atau berasal dari data penjualan toko.

### 2.2 Struktur Dataset

| Kolom | Deskripsi |
|------|----------|
| Temperature (°C) | Suhu rata-rata harian |
| Sales (Unit) | Jumlah minuman terjual |

### 2.3 Ukuran Dataset
- Jumlah data: ±30–100 baris  
- Format: CSV  
- Jenis data: Numerik kontinu  
- Tujuan: Memprediksi nilai **Sales** berdasarkan **Temperature**

---

## BAB III – METODOLOGI

### 3.1 Tahapan Penelitian
1. **Pengumpulan Data**  
   Mengumpulkan data suhu dan penjualan dalam format CSV.
2. **Preprocessing Data**  
   Pembersihan data dan normalisasi.
3. **Perancangan Model**  
   Neural Network dengan beberapa hidden layer.
4. **Pelatihan Model**  
   Menggunakan framework TensorFlow.
5. **Evaluasi Model**  
   Menggunakan data pengujian dan metrik evaluasi.
6. **Analisis Hasil**  
   Membandingkan hasil Deep Learning dengan metode tradisional.

---

### 3.2 Alur Penelitian
Dataset → Preprocessing → Training Model Deep Learning
→ Evaluasi → Analisis Hasil → Kesimpulan


---

## BAB IV – PENUTUP

### 4.1 Kesimpulan
Metode Deep Learning berbasis Neural Network mampu memprediksi jumlah penjualan minuman berdasarkan suhu harian dengan lebih baik dibandingkan metode tradisional. Model ini berpotensi memberikan prediksi yang lebih akurat dan dapat dimanfaatkan dalam pengambilan keputusan bisnis.

---

## BAB V – TINJAUAN PUSTAKA
1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly Media.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
3. Alpaydin, E. (2020). *Introduction to Machine Learning*. MIT Press.
4. Han, J., Kamber, M., & Pei, J. (2011). *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
5. TensorFlow Documentation (2024). *Neural Network and Deep Learning*.
