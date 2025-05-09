Conclusion
==========

Despite its simplicity and unsupervised nature, our **QuantumAnomalyDetector** demonstrates competitive performance with classical anomaly detection techniques.

Key takeaways:

- The model leverages a locally normalized k-NN scoring method, inspired by LOF.
- It is fully unsupervised and does not rely on labeled data for training.
- On the Hypothyroid dataset, it outperformed Isolation Forest and approached the performance of One-Class SVM in terms of F1 and AUC.

While the current implementation is relatively simple, future improvements could include:
- Quantum kernel methods for more expressive decision boundaries
- Dimensionality reduction using variational quantum circuits
- Integration with supervised post-training refinement

The detector provides a foundation for exploring lightweight quantum-inspired approaches in real anomaly detection pipelines.
