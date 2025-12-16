# Hyperparameter

params = {
    "solver": ["liblinear", "lbfgs"],
    "C": [0.01, 0.1, 1, 10],
    "class_weight": [None, "balanced"],
    "max_iter": [200, 500]
}

# --- MODEL ---

y_pred = best_model.predict(X_test)
y_proba = best_model.predict_proba(X_test)[:,1]

report = classification_report(y_test, y_pred, output_dict=True)
Auc = roc_auc_score(y_test, y_proba)

# Hasil Awal

print("Hasil model logistiv regression")

# Define LR metrics
acc_lr = report["accuracy"]
auc_lr = Auc
f1_lr = report["1"]["f1-score"] # F1-score for class 1 (yes)

result = {
    "Logistic Regression" : {
        "Accuracy" : round(acc_lr, 4),
        "AUC" : round(auc_lr, 4),
        "Recall_1" : round(report["1"]["recall"], 4)
    }
}

pd.DataFrame(result).T

# Logistic Regression Report

hasilReport = classification_report(y_test, y_pred)
print(hasilReport)

# Cek akurasi train dan test

train_acc = pipe.score(X_train, y_train)
test_acc = pipe.score(X_test, y_test)

print("Akurasi train: ", train_acc)
print("Akurasi test: ", test_acc)

# CEk prediksi
y_pred = pipe.predict(X_test)
y_proba = pipe.predict_proba(X_test)

print(f"Akurasi Train : {train_acc:.4f}")
print(f"Akurasi Test : {test_acc:.4f}")

import joblib

joblib.dump(best_model, "logisticRegression_model.pkl")