Usage
=====

.. code-block:: python

   from quantum_anomaly_detection import QuantumAnomalyDetector

   detector = QuantumAnomalyDetector(k=10, contamination=0.05)
   detector.fit(X_train)
   scores = detector.predict(X_test)
   anomalies = [detector.is_anomalous(s) for s in scores]
