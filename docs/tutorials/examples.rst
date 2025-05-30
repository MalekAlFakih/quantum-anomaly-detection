Tutorials
=========

.. contents::
   :local:

Quickstart
----------

.. code-block:: python

   from quantum_anomaly_detection import QuantumAnomalyDetector

   qad = QuantumAnomalyDetector(k=10, contamination=0.5)
   qad.fit(X_train)
   scores = qad.predict(X_test)
   preds = [qad.is_anomalous(s) for s in scores]

Run on Hypothyroid Dataset (Google Colab)
-----------------------------------------

(https://colab.research.google.com/drive/1zYoGgQ6UlfMEGI3hvNdYVmDFXX5hHRlr)

This tutorial demonstrates how to load, clean, and evaluate the quantum anomaly detector on a real-world medical dataset.
