# 📘 Judul Proyek
Analisis dan Pemodelan Prediktif untuk Penentuan Keberhasilan Langganan Deposito Jangka Pendek (Studi Kasus: Bank Marketing Campaign)

## 👤 Informasi
- **Nama:** Rizqi Agus Sahputra
- **Repo:** https://github.com/ininduu/DataScience-BankCampaign-.git
- **Video:** https://youtu.be/h2rErXh-4r4?si=ACnx9gEqMCpsbQVQ

---

# 1. 🎯 Ringkasan Proyek
- Menyelesaikan permasalahan sesuai domain  
- Melakukan data preparation  
- Membangun 3 model: **Baseline**, **Advanced**, **Deep Learning**  
- Melakukan evaluasi dan menentukan model terbaik  

---

# 2. 📄 Problem & Goals
**Problem Statements:**  
- Ketidakseimbangan Kelas (Imbalance Data): Rasio kelas target $y$ sangat timpang ($\approx 88.5\% : 11.5\%$), yang dapat menyebabkan model bias dan gagal mengidentifikasi kelas minoritas (pelanggan potensial).
- Efisiensi Pemasaran: Bank perlu mengoptimalkan biaya kampanye dengan mengurangi panggilan telepon yang tidak berhasil (False Positive) dan memaksimalkan identifikasi pelanggan berpotensi (True Positive).

**Goals:**  
- Mencapai akurasi model di rentang $\mathbf{75\%}$ - $\mathbf{80\%}$ pada Test Set.
- Mengembangkan model yang memiliki skor AUC-ROC tertinggi untuk kemampuan diskriminasi yang superior.
- Mengidentifikasi fitur-fitur kunci yang mendorong keputusan klien untuk berlangganan deposito

---
## 📁 Struktur Folder
```
project/
│
├── data/                   # Dataset (tidak di-commit, download manual)
│
├── notebooks/              # Jupyter notebooks
│   └── ML_Project.ipynb
│
├── src/                    # Source code
│   
├── models/                 # Saved models
│   ├── model_baseline.pkl
│   ├── model_rf.pkl
│   └── model_cnn.h5
│
├── images/                 # Visualizations
│   └── r
│
├── requirements.txt        # Dependencies
├── .gitignore
└── README.md
```
---

# 3. 📊 Dataset
- **Sumber:** https://archive.ics.uci.edu/dataset/222/bank+marketing 
- **Jumlah Data:** 4507
- **Tipe:** Tabular

### Fitur Utama
| Variable Name | Role | Type | Demographic | Description | Missing Values |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **age** | Feature | Integer | Yes | Usia klien. | No |
| **job** | Feature | Categorical | No | Jenis pekerjaan ('admin.', 'blue-collar', 'management', dll.). | No |
| **marital** | Feature | Categorical | Yes | Status pernikahan ('divorced', 'married', 'single'). | No |
| **education** | Feature | Categorical | No | Tingkat pendidikan ('primary', 'secondary', 'tertiary', 'unknown'). | No |
| **default** | Feature | Binary | No | Apakah memiliki kredit yang gagal bayar (default). | No |
| **balance** | Feature | Integer | No | Rata-rata saldo tahunan (dalam Euros). | No |
| **housing** | Feature | Binary | No | Apakah memiliki pinjaman perumahan (housing loan). | No |
| **loan** | Feature | Binary | No | Apakah memiliki pinjaman pribadi (personal loan). | No |
| **contact** | Feature | Categorical | No | Jenis komunikasi kontak ('cellular', 'telephone'). | Yes (Implisit 'unknown') |
| **day** | Feature | Integer | No | Hari terakhir kontak dalam sebulan. | No |
| **month** | Feature | Categorical | No | Bulan terakhir kontak. | No |
| **duration** | Feature | Integer | No | Durasi kontak terakhir (detik). | No |
| **campaign** | Feature | Integer | No | Jumlah kontak yang dilakukan selama kampanye ini. | No |
| **pdays** | Feature | Integer | No | Jumlah hari sejak klien terakhir dihubungi dari kampanye sebelumnya (-1 berarti tidak pernah dihubungi). | No |
| **previous** | Feature | Integer | No | Jumlah kontak yang dilakukan sebelum kampanye ini. | No |
| **poutcome** | Feature | Categorical | No | Hasil dari kampanye pemasaran sebelumnya. | Yes (Implisit 'unknown') |
| **y** | Target | Binary | No | **Variabel Target:** Apakah klien berlangganan deposito berjangka? ('yes' atau 'no'). | No |
---

# 4. 🔧 Data Preparation
- Cleaning : Tidak ada missing values eksplisit, namun 'unknown' pada poutcome, contact, education, dan job ditangani sebagai kategori terpisah.  
- Transformasi : Encoding: One-Hot Encoding pada fitur nominal (job, marital, contact). Ordinal Encoding pada fitur biner/ordinal (education, housing, loan). Scaling: StandardScaler diterapkan pada semua fitur numerik (age, balance, campaign, dll.).
- Splitting : Strategi 80% Training Set, 20%Test Set.

---

# 5. 🤖 Modeling
- **Model 1 – Baseline:** Logisti Regression 
- **Model 2 – Advanced ML:** Random Forest
- **Model 3 – Deep Learning:** MLP

---

# 6. 🧪 Evaluation
**Metrik:** Accuracy / F1 / MAE / MSE (pilih sesuai tugas)

### Hasil Singkat
| Model | Score | Catatan |
|-------|--------|---------|
| Baseline | 0.65 % | |
| Advanced | 0.76 % | |
| Deep Learning | 0.87 % | |

---

# 7. 🏁 Kesimpulan
- Model terbaik: Random Forest Classifier
- Alasan: Model ini memberikan skor AUC-ROC tertinggi 0.7382%, yang merupakan metrik paling handal untuk data tidak seimbang. Akurasi keseluruhannya 75.36 % berada di rentang target 75%-80%. Tuning berhasil menyeimbangkan Recall kelas minoritas 0.54 tanpa mengorbankan terlalu banyak Presisi.
- Insight penting: Kontak Sebelumnya Kunci: Fitur has_previous_contact dan pdays_group menunjukkan bahwa kontak sebelumnya, terutama yang baru, sangat memengaruhi konversi. 

---

# 8. 🔮 Future Work

 
Data
 [x] Mengumpulkan lebih banyak data
 [x] Menambah variasi data
 [x] Feature engineering lebih lanjut
 
Model
 [x] Mencoba arsitektur DL yang lebih kompleks
 [x] Hyperparameter tuning lebih ekstensif
 [x] Ensemble methods (combining models)
 [x] Transfer learning dengan model yang lebih besar
 
Deployment
 [] Membuat API (Flask/FastAPI)
 [] Membuat web application (Streamlit/Gradio)
 [] Containerization dengan Docker
 [] Deploy ke cloud (Heroku, GCP, AWS)
 
Optimization
 [] Model compression (pruning, quantization)
 [] Improving inference speed
 [x] Reducing model size

---

# 9. 🔁 Reproducibility

Gunakan environment:
- Environment
- Python: 3.12
- Operating System: Windows / Linux / macOS

Dependencies
- numpy==1.24.3
- pandas==2.0.3
- scikit-learn==1.3.0
- matplotlib==3.7.2
- seaborn==0.12.2
- tensorflow==2.14.0

# 🚀 10. Cara Menjalankan Proyek
Panduan berikut menjelaskan cara menjalankan proyek klasifikasi status batu empedu baik secara lokal maupun menggunakan Google Colab.

Clone Repository
- git clone https://github.com/ininduu/DataScience-BankCampaign-.git
- cd DataScience-BankCampaign

Create Virtual Environment (Opsional)
- Linux / macOS
- python3 -m venv venv
- source venv/bin/activate

Windows
- python -m venv venv
- venv\Scripts\activate

Install Dependencies
- pip install -r requirements.txt
- Download Dataset

Unduh dataset dari Kaggle:
- https://archive.ics.uci.edu/dataset/222/bank+marketing

Simpan sebagai:
- bank_.csv

Running the Project
- Option 1: Script Modular
- python src/Download dan Load Dataset.py
- python src/Exploratory Data Analysis (EDA).py
- python src/Data Cleaning.py
- python src/Feature Engineering.py
- python src/Data Splitting.py
- python src/Data Transformation.py
- python src/Modeling.py

- Output model:
```
models/
├── logistic_regression_model.pkl
├── gradient_boosting_model.pkl
└── mlp_deep_learning_model.h5
```

- Option 2: Jupyter Notebook
jupyter notebook
Buka:
- notebooks/UAS_234311053_Rizqi.AS.ipynb
- Option 3: Google Colab
- Buka https://colab.research.google.com
- Upload notebook UAS_234311053_Rizqi A.S.ipynb

Run All
Estimasi waktu: 10–15 menit
