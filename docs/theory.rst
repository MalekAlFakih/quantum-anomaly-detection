Theory
======

QuantumAnomalyDetector is inspired by distance-based anomaly detection techniques, particularly **k-Nearest Neighbors (k-NN)** and **Local Outlier Factor (LOF)**.

The model calculates the average distance to the `k` nearest training points and normalizes this by the average local density in the training set. This normalization accounts for varying density across the dataset and mimics the behavior of LOF while remaining efficient and interpretable.

The score returned is:
.. math::

   \text{score}(x) = \frac{\text{avg. distance of } x \text{ to kNN}}{\text{avg. density of training kNNs}}

