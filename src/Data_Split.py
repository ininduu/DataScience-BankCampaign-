# 1. Mendefinisikan Kelompok Fitur

# Fitur numerik
numerik_fitur = ['age', 'pdays', 'campaign', 'balance', 'previous', 'month_num']

# Fitur Ordinal
ordinal_fitur = ['default', 'housing', 'loan', 'education', 'pdays_group']

# Mendefinisikan untuk kategori ordinal encoding
education_mapping = ['unknown', 'primary', 'secondary','tertiary'] # Corrected typo
pdays_group_mapping = ['Not Contacted', 'Fresh Contacted', 'Regular Contacted', 'Old Contacted'] # Corrected typo

# Fitur Kategori
kategori_fitur = ['job', 'marital', 'contact'] # Corrected typo

X = bank.drop('y', axis=1)
y = bank['y']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

from sklearn.decomposition import PCA

X_train_scaled = preprocesor.fit_transform(X_train)
X_test_scaled = preprocesor.transform(X_test)

pca = PCA(n_components=0.95, random_state=42)

X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

print("Fitur sebelum PCA:", X_train.shape[1])
print("Fitur setelah PCA:", X_train_pca.shape[1])