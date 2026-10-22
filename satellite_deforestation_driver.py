"""
Studi Kasus Materi 6: Satellite Deforestation Alert Driver Attribution
Pembicara: Dr. Bart Slagter (Wageningen University & Research)
Deskripsi: Mensimulasikan klasifikasi otomatis penggerak deforestasi
           (Direct Drivers of Deforestation) berbasis data fitur spektral satelit.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def generate_mock_satellite_features():
    """
    Generasi data sampel fitur citra satelit (Optik + Radar)
    Features:
    - ndvi_drop: Penurunan indeks vegetasi (Optik)
    - sar_backscatter_diff: Perubahan pantulan radar Sentinel-1 (dB)
    - area_hectares: Luas area perubahan tutupan pohon
    - distance_to_road_m: Jarak ke jalan terdekat (meter)
    - fire_hotspot_detected: Flag deteksi titik panas thermal (0/1)
    """
    np.random.seed(42)
    n_samples = 200

    drivers = ['Small_Agriculture', 'Large_Agriculture', 'Selective_Logging', 'Mining', 'Wildfire']
    labels = np.random.choice(drivers, size=n_samples, p=[0.35, 0.20, 0.20, 0.10, 0.15])

    data = []
    for label in labels:
        if label == 'Small_Agriculture':
            ndvi = np.random.uniform(0.3, 0.6)
            sar = np.random.uniform(-3.0, -1.0)
            area = np.random.uniform(0.1, 2.0) # < 2 ha
            dist_road = np.random.uniform(100, 1000)
            fire = np.random.choice([0, 1], p=[0.8, 0.2])
        elif label == 'Large_Agriculture':
            ndvi = np.random.uniform(0.5, 0.8)
            sar = np.random.uniform(-6.0, -3.0)
            area = np.random.uniform(5.0, 50.0) # > 5 ha
            dist_road = np.random.uniform(50, 500)
            fire = np.random.choice([0, 1], p=[0.5, 0.5])
        elif label == 'Selective_Logging':
            ndvi = np.random.uniform(0.1, 0.3)
            sar = np.random.uniform(-2.0, 0.0)
            area = np.random.uniform(0.1, 1.5)
            dist_road = np.random.uniform(0, 100) # Sangat dekat jalan
            fire = 0
        elif label == 'Mining':
            ndvi = np.random.uniform(0.6, 0.9) # Hilang total
            sar = np.random.uniform(-8.0, -4.0)
            area = np.random.uniform(1.0, 10.0)
            dist_road = np.random.uniform(200, 2000)
            fire = 0
        else: # Wildfire
            ndvi = np.random.uniform(0.4, 0.7)
            sar = np.random.uniform(-4.0, -1.0)
            area = np.random.uniform(2.0, 30.0)
            dist_road = np.random.uniform(500, 5000)
            fire = 1 # Ada hotspot
        
        data.append({
            'ndvi_drop': round(ndvi, 3),
            'sar_backscatter_diff': round(sar, 3),
            'area_hectares': round(area, 2),
            'distance_to_road_m': round(dist_road, 1),
            'fire_hotspot': fire,
            'driver_label': label
        })
    return pd.DataFrame(data)

def main():
    print("=== SIMULASI KLASIFIKASI PENGGERAK DEFORESTASI (AI & REMOTE SENSING) ===")
    df = generate_mock_satellite_features()
    print("\nSample Dataset Fitur Satelit (Sentinel-1 & Sentinel-2):")
    print(df.head(10))

    # Feature & Target Split
    X = df[['ndvi_drop', 'sar_backscatter_diff', 'area_hectares', 'distance_to_road_m', 'fire_hotspot']]
    y = df['driver_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # Model Training
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    print("\n[INFO] Pelatihan Model AI untuk Klasifikasi Driver Deforestasi Selesai.")

    # Evaluation
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nAkurasi Model (Accuracy): {acc * 100:.2f}%
")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Inference / Testing New Alert
    print("=== SIMULASI PREDIKSI ALERT DEFORESTASI BARU ===")
    new_alert = pd.DataFrame([{
        'ndvi_drop': 0.65,
        'sar_backscatter_diff': -5.2,
        'area_hectares': 12.5,
        'distance_to_road_m': 120.0,
        'fire_hotspot': 1
    }])
    predicted_driver = clf.predict(new_alert)[0]
    print(f"Alert Baru (Luas 12.5ha, Hotspot (+)) -> Prediksi Driver: [{predicted_driver.upper()}]")

if __name__ == "__main__":
    main()
