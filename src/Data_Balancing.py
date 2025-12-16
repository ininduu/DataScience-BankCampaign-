# Base model
log_reg = LogisticRegression(max_iter=5000, solver='lbfgs')

pipe = ImbPipeline([
    ('preprocess', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('logreg', LogisticRegression(
        solver='lbfgs',
        max_iter=5000
    ))
])