.. _usage:

Usage
=====

This section shows how to use the `QuantumAnomalyDetector` class.

.. code-block:: python

   from quantum_anomaly_detection import QuantumAnomalyDetector
   import numpy as np
   data = np.random.rand(10, 2)
   detector = QuantumAnomalyDetector(threshold=0.6)
   detector.fit(data)
   scores = detector.predict(data)
   print("Anomaly Scores:", scores)
   print("Is anomalous:", detector.is_anomalous(scores[0]))