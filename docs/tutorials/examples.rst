Tutorials
=========

.. contents::
   :local:

Quickstart
----------

.. code-block:: python

   from quantum_anomaly_detection import QuantumAnomalyDetector

   qad = QuantumAnomalyDetector(k=10, contamination=0.05)
   qad.fit(X_train)
   scores = qad.predict(X_test)
   preds = [qad.is_anomalous(s) for s in scores]

Run on Hypothyroid Dataset
---------------------------

See how we load, clean, and evaluate the model on real-world multivariate data.

.. literalinclude:: ../notebooks/Hypothyroid_LOF_Quantum.ipynb
   :language: python
   :start-after: "# Quantum Anomaly Detection (LOF-Inspired)"
   :end-before: "# End of Notebook"
