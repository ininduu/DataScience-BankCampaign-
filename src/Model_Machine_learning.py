
# Identifikasi kolom kategorikal
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()

# Model

rf = RandomForestClassifier(
    n_estimators = 200,
    max_depth = 5,
    min_samples_split = 2,
    min_samples_leaf = 1,
    max_features = 'sqrt',
    random_state = 42,
    class_weight = 'balanced',
    n_jobs = -1
)

model = Pipeline([
    ("preprocess", preprocessor),
    ("rf", rf)
])

model.fit(X_train, y_train)

# Hasil Model

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:,1]

# Evaluasi

from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score,
    confusion_matrix, classification_report
)

# Acuracy, AOC

acc_rf = accuracy_score(y_test, y_pred)
f1_rf = f1_score(y_test, y_pred)
auc_rf = roc_auc_score(y_test, y_proba)

print("Accuracy : ", acc_rf)
print("F1 Score : ", f1_rf)
print("ROC AUC : ", auc_rf)

# Clasifikasi Report

hasilReport = classification_report(y_test, y_pred)
print(hasilReport)

# Prediksi

y_pred_test = model.predict(X_test)
y_proba_test = model.predict_proba(X_test)

# Akurasi
y_pred_train = model.predict(X_train)
train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred_test)

print(f"Akurasi Train : {train_acc:.4f}")
print(f"Akurasi Test : {test_acc:.4f}")

# Cek Overfitting
gap = train_acc - test_acc
print(f"Gap Akurasi : {gap:.4f}")