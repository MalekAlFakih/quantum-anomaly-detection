Usage
=====

Import and use the detector:

.. code-block:: python

   from quantum_anomaly_detection import QuantumAnomalyDetector

   model = QuantumAnomalyDetector(k=10, contamination=0.05)
   model.fit(X_train)
   scores = model.predict(X_test)
   preds = [model.is_anomalous(s) for s in scores]

