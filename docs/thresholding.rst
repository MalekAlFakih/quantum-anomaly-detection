Thresholding Logic
==================

The anomaly detector sets a threshold based on the **contamination** parameter supplied by the user.

.. code-block:: python

   detector = QuantumAnomalyDetector(k=10, contamination=0.5)

This threshold is computed by scoring all training samples.

Scores above this threshold are considered anomalous.

