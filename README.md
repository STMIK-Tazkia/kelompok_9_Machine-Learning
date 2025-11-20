PROPOSAL
Prediksi Jumlah Penjualan Minuman Berdasarkan Suhu Harian Menggunakan Linear Regression

Disusun Oleh:

Denvi Sekartazi Iskandar (241552010020)
Muhammad Ma’rufil Kurhi (241552010002)

Dosen Pengampu:
Hendri Karisma S.Kom M,T

Fakultas Ilmu Komputer
Jurusan Teknik Informatika
Sekolah Tinggi Manajemen Ilmu Komputer Tazkia
( Stmik Tazkia)




BAB I
PENDAHULUAN

1.1 Latar Belakang
Kondisi lingkungan, terutama suhu udara harian, memiliki pengaruh yang signifikan terhadap tingkat penjualan minuman. Saat suhu meningkat, kebutuhan masyarakat terhadap minuman juga cenderung bertambah sebagai bentuk penyesuaian terhadap cuaca yang lebih panas.
Dengan memanfaatkan teknologi machine learning, khususnya metode supervised learning menggunakan algoritma Linear Regression, hubungan antara suhu udara dan volume penjualan dapat dianalisis untuk menghasilkan model prediksi yang akurat.
Penelitian ini berfokus pada pemanfaatan data sederhana sebagai dasar analisis prediktif untuk membantu pelaku usaha memperkirakan penjualan berdasarkan kondisi cuaca. Dengan pendekatan ini, pengelolaan stok serta strategi pemasaran dapat dilakukan secara lebih efisien dan tepat sasaran.

1.2 Rumusan Masalah
1.	Bagaimana pengaruh suhu udara harian terhadap jumlah penjualan minuman?
2.	Bagaimana penerapan algoritma Linear Regression dalam memprediksi jumlah penjualan?
3.	Seberapa tinggi tingkat akurasi model prediksi yang dihasilkan berdasarkan data suhu harian?

1.3 Tujuan Penelitian
1.	Menganalisis hubungan antara suhu udara harian dengan penjualan minuman.
2.	Mengembangkan model Linear Regression untuk memprediksi jumlah penjualan.

1.4 Manfaat Penelitian
1.	Memberikan acuan bagi pelaku usaha dalam menentukan jumlah stok penjualan yang optimal.
2.	Menunjukkan penerapan praktis metode machine learning sederhana dalam bidang penjualan.
3.	Menjadi referensi bagi pembelajaran konsep supervised learning dengan menggunakan data realistis.








BAB II
DESKRIPSI DATASET

2.1 Sumber Dataset
Dataset yang digunakan dalam penelitian ini merupakan data simulasi yang dibangun berdasarkan suhu udara harian dan jumlah penjualan minuman selama periode tertentu (misalnya 30 hari). Data tersebut dapat dibuat secara manual atau dikumpulkan dari catatan penjualan toko untuk memberikan gambaran realistis terhadap kondisi sebenarnya.

2.2 Struktur Dataset
Kolom 	Deskripsi 
Temperatur (°C)	Suhu rata-rata harian 
Sales (unit)	Jumlah minuman yang terjual 

2.3 Ukuran Dataset
•	Jumlah data: ±30–100 baris
•	Format: .csv
•	Jenis data: Numerik kontinu
•	Tujuan: Memprediksi nilai Sales berdasarkan variabel Temperature


BAB III
METODOLOGI PENELITIAN

3.1 Tahapan Penelitian
1.	Pengumpulan Data
Mengumpulkan data suhu udara dan penjualan dari catatan toko atau dengan membuat data simulasi.
2.	Preprocessing
Membersihkan data, menghapus nilai kosong, serta memastikan semua data berformat numerik dan siap digunakan.
3.	Pemodelan
Menggunakan algoritma Linear Regression dengan bantuan pustaka Python seperti pandas, scikit-learn, dan matplotlib.
4.	Evaluasi Model
Mengukur performa model menggunakan metrik Mean Squared Error (MSE) dan R² Score untuk menilai tingkat akurasi.
5.	Visualisasi
Menampilkan grafik hubungan antara suhu dan penjualan, serta menambahkan garis regresi untuk memperlihatkan pola prediksi.

3.2 Alur Penelitian
Input Data → Preprocessing → Training Model → Evaluasi → Visualisasi → Kesimpulan


BAB IV
KESIMPULAN

4.1 Kesimpulan 
Berdasarkan hasil perancangan dan analisis model Linear Regression, dapat disimpulkan bahwa suhu udara harian memiliki hubungan positif terhadap jumlah penjualan minuman. Semakin tinggi suhu udara, semakin besar pula potensi peningkatan penjualan minuman.
Penerapan metode Linear Regression terbukti mampu memprediksi penjualan dengan tingkat akurasi yang cukup baik, meskipun data yang digunakan sederhana atau hasil simulasi. Model ini dapat dijadikan dasar bagi pelaku usaha untuk memperkirakan kebutuhan stok dan strategi penjualan berdasarkan kondisi cuaca harian.

BAB V 
TINJAUAN PUSTAKA

1.	Han, J., Kamber, M., & Pei, J. (2011). Data Mining: Concepts and Techniques. Morgan Kaufmann.
2.	Géron, A. (2022). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. O’Reilly Media.
3.	Alpaydin, E. (2020). Introduction to Machine Learning. MIT Press.
4.	UCI Machine Learning Repository. (2024). Temperature vs Sales Sample Dataset.

