Evaluation Strategy
===================

We evaluate the anomaly detector using standard binary classification metrics:

- **Accuracy**: proportion of correct predictions.
- **F1 Score**: harmonic mean of precision and recall.
- **ROC AUC**: area under the ROC curve, useful for imbalance.

.. code-block:: python

   from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

   accuracy_score(y_true, y_pred)
   f1_score(y_true, y_pred)
   roc_auc_score(y_true, scores)

