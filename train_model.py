import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

# Load training data
df = pd.read_csv(r"data/UNSW_NB15_training-set.csv").sample(50000, random_state=42)

features = ['dur','spkts','dpkts','rate','dload','sinpkt']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

dbscan = DBSCAN(eps=0.6, min_samples=10)
dbscan.fit(X_scaled)

pca = PCA(n_components=2)
pca.fit(X_scaled)

joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(dbscan, "model/dbscan.pkl")
joblib.dump(pca, "model/pca.pkl")

print("✅ Model saved successfully")
