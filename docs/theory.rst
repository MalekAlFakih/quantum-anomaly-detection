Theory
======

QuantumAnomalyDetector is inspired by distance-based anomaly detection techniques, particularly **k-Nearest Neighbors (k-NN)** and **Local Outlier Factor (LOF)**.

The model calculates the average distance to the `k` nearest training points and normalizes this by the average local density in the training set.

The score returned is:

.. math::

   \text{score}(x) = \frac{\mathrm{avg\_dist}(x, \mathrm{kNN})}{\mathrm{mean\_density}(kNN)}

This mimics the behavior of LOF while remaining interpretable and efficient.
