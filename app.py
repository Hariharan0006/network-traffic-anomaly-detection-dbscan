from flask import Flask, render_template, request
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PLOT_FOLDER = "static/plots"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PLOT_FOLDER, exist_ok=True)

# Load models
scaler = joblib.load("model/scaler.pkl")
dbscan = joblib.load("model/dbscan.pkl")
pca = joblib.load("model/pca.pkl")

FEATURES = ['dur','spkts','dpkts','rate','dload','sinpkt']

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        df = pd.read_csv(filepath)
        X = df[FEATURES]
        X_scaled = scaler.transform(X)

        df["cluster"] = dbscan.fit_predict(X_scaled)
        anomalies = (df["cluster"] == -1).sum()

        # PCA plots
        X_pca = pca.transform(X_scaled)

        # BEFORE
        plt.figure(figsize=(6,4))
        plt.scatter(X_pca[:,0], X_pca[:,1], s=5)
        plt.title("Before DBSCAN")
        plt.savefig(f"{PLOT_FOLDER}/before.png")
        plt.close()

        # AFTER
        plt.figure(figsize=(6,4))
        plt.scatter(
            X_pca[df["cluster"] != -1,0],
            X_pca[df["cluster"] != -1,1],
            s=5, label="Normal"
        )
        plt.scatter(
            X_pca[df["cluster"] == -1,0],
            X_pca[df["cluster"] == -1,1],
            s=10, label="Anomaly"
        )
        plt.legend()
        plt.title("After DBSCAN")
        plt.savefig(f"{PLOT_FOLDER}/after.png")
        plt.close()

        result = {
            "rows": df.shape[0],
            "anomalies": anomalies
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
