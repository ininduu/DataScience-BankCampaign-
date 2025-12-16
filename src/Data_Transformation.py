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

# 2. Membuat ColumnTransformer

preprocesor = ColumnTransformer([

    # Transformasi 1 : Srandard Scaling untu, fitru Numerik
    ('numerik', StandardScaler(), numerik_fitur),

    # Transformasi 2 : Ordinal Encoding Untuk fitur ordinal
    ('ord', OrdinalEncoder(categories = [
        ['no', 'yes'],
        ['no', 'yes'],
        ['no', 'yes'],
        education_mapping,
        pdays_group_mapping
    ]), ordinal_fitur),

    # Transformasi 3 : One Hot Encoding untuk Fitur Nominal
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), kategori_fitur)
],
    remainder='passthrough'
)