# Cek 5 Baris Awal dan 5 baris akhir

cekAwal = bank.head(5)
cekAwal

# 5 baris akhir

cekAkhir = bank.tail(5)
cekAkhir

# Cek information about dataset
print("\n Cek Information About Dataset ")
bank.info()

# Cek Ukuran

print("\n Ukuran Dataset ")
bank.shape

# Hitung nilai kolom kategorikal

Nilai = bank['y'].value_counts()
Nilai

# Jumlah Job

JumlahJob = bank['job'].value_counts()
JumlahJob

# Hitung Nilai Hilang atau Missing Value

MissingValue = bank.isnull().sum()
MissingValue

# Cek Duplikat

cekDuplikat = bank.duplicated().sum()
cekDuplikat

# jumlah martial

jumlahMartial = bank['marital'].value_counts()
jumlahMartial

# Calculate the proportion of 'yes' for each job
job_y_counts = bank.groupby('job')['y'].value_counts(normalize=True).unstack()
job_y_proportion = job_y_counts['yes'].reset_index()
job_y_proportion.columns = ['job', 'proportion']

# Visualisasi Data
plt.figure(figsize=(8,4))
sns.barplot(x='job', y='proportion', data=job_y_proportion)
plt.title('Persentase Langganan Deposito berjangka Berdasarkan Pekerjaan')
plt.xlabel('Pekerjaan')
plt.ylabel('Persentase Langganan (%)')
plt.xticks(rotation=40, ha='right')
plt.tight_layout()
plt.show()

# 1. Bivariate Analysis for Numerical Feature: 'age' vs 'y' (Target)
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='age', data=bank)
plt.title('Distribusi Umur Berdasarkan Langganan Deposito Jangka Pendek (y)')
plt.xlabel('Langganan (y)')
plt.ylabel('Usia (age)')
plt.show()

# Bar plot untuk Y

plt.figure(figsize=(5,6))
sns.countplot(x='y', data=bank)
distribusi = bank['y'].value_counts()