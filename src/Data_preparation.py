# 5.1 Handling Missing Value

# Handling Missing Value
bank = bank.drop('duration', axis=1)
print("Kolom Duration telah terhapus")

# Handle Special Value -1 in pdays
bank['pdays'] = bank['pdays'].replace(-1, 999)
print("Nilai -1 pada kolom pdays Telah diubah menjadi 999")

# 5.2 Removing Duplicatet

cekDuplikat = len(bank)
bank.drop_duplicates(inplace=True)
cekSetelahDrop = len(bank)
print(f"Jumlah Duplikat Setelah Dihapus: ", {cekDuplikat - cekSetelahDrop})

# 5.3 Handling Outliers

numerik_fitur = ['balance', 'campaign']

for col in numerik_fitur:
  upper_limit = bank[col].quantile(0.95)
  bank[col] = np.where(bank[col] > upper_limit, upper_limit, bank[col])
  print(f"Outliers pada kolom {col} telah dibatasi pada Quantile 92 ({upper_limit:.2f}).")

# 5.4 Data Conversation

bank['y'] = bank['y'].map({'yes': 1, 'no': 0})
print("Variabel Target y telah dikonversi menjadi bilangan binner (1=yes, 0=no  )")

# Tampilkan setelah dilakukan cleaning
print("\nInformasi Data Setelah Data Cleaning ")
print(bank.head().to_markdown(index=False, numalign="left", stralign="left "))