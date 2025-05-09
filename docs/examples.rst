Examples
========

Here is an example using the hypothyroid dataset:

.. code-block:: python

   import pandas as pd
   from sklearn.preprocessing import LabelEncoder, StandardScaler
   from sklearn.model_selection import train_test_split
   from quantum_anomaly_detection import QuantumAnomalyDetector

   df = pd.read_csv("hypothyroid.csv")
   y = LabelEncoder().fit_transform(df["binaryClass"])
   X = df.drop(columns=["referral source", "binaryClass"]).select_dtypes(exclude="object").dropna()
   X_scaled = StandardScaler().fit_transform(X)
   X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, stratify=y, test_size=0.3)

   model = QuantumAnomalyDetector(k=10, contamination=0.05)
   model.fit(X_train)
   scores = model.predict(X_test)
   preds = [model.is_anomalous(s) for s in scores]
