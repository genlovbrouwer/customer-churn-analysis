from sklearn.metrics import (
    roc_auc_score,
    classification_report,
    confusion_matrix
)


def evaluate_model(model, X_test, y_test):
    probs = model.predict_proba(X_test)[:, 1]
    preds = model.predict(X_test)

    return {
        "roc_auc": roc_auc_score(y_test, probs),
        "report": classification_report(y_test, preds),
        "confusion_matrix": confusion_matrix(y_test, preds)
    }