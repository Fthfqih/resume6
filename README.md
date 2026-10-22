# Seri Studi Kasus 6: Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

Repositori ini berisi ringkasan materi, studi kasus, serta implementasi coding untuk **Materi 6** pada kegiatan *Informatics Practitioner Lecture Series* Universitas Bengkulu.

- **Pembicara**: Dr. Bart Slagter (Postdoctoral Researcher in Remote Sensing & AI, Wageningen University & Research / WUR, Netherlands)
- **Topik**: *Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI* (Identifikasi Penggerak Langsung Deforestasi Menggunakan Citra Satelit dan Kecerdasan Buatan)

---

## 📌 Ringkasan Materi

### 1. Pentingnya Hutan Tropis & Tantangan Deforestasi
- Hutan tropis merupakan penyimpan karbon terbesar, pengatur siklus air, dan rumah bagi keanekaragaman hayati.
- Deforestasi dan degradasi hutan terjadi secara cepat akibat pembukaan lahan pertanian (*agriculture*), ekstraksi sumber daya (*logging* & *gold mining*), kebakaran hutan (*wildfires*), dan infrastruktur (jalan).

### 2. Kombinasi Sensor Satelit (Optical vs. Radar)
- **Optical Satellite (Sentinel-2 / Landsat)**: Memberikan detail warna dan kebugaran vegetasi (inframerah), tetapi sering terhalang oleh tutupan awan tropis (*cloud cover*).
- **Radar Satellite (Sentinel-1 SAR)**: Memancarkan pulsa radar yang menembus awan dan dapat mengamati perubahan struktur hutan secara konsisten dalam kondisi cuaca apa pun.
- *Deforestation Alerts System* (seperti RADD / GLAD Alerts): Memeriksa tutupan pohon secara mingguan pada resolusi $10-30	ext{ meter}$.

### 3. Peran AI & Deep Learning (Convolutional Neural Networks / CNN)
- **Batasan Sistem Alert Tradisional**: Alert biasa hanya mendeteksi *bahwa* tutupan pohon hilang, tetapi **tidak tahu penyebabnya**.
- **Model CNN Multi-Sensor**: Menerima tumpukan (*stack*) citra Sentinel-1 & Sentinel-2 pasca-alert, lalu menganalisis pola spasiotemporal serta konteks sekitarnya untuk mengklasifikasikan penggerak (*direct driver*) secara otomatis:
  1. *Small-Scale Agriculture* (Pertanian skala kecil/petani swadaya).
  2. *Large-Scale Agriculture* (Pertanian skala industri/perkebunan).
  3. *Selective Logging* (Penebangan kayu selektif & pembukaan jalan logistik).
  4. *Mining* (Penambangan emas/sumber daya).
  5. *Wildfire* (Kebakaran hutan).
  6. *Natural Disturbances* (Bencana alam/banjir/angin puting beliung).

### 4. Tantangan & Implementasi Praktis
- **Trade-off Latensi & Akurasi**: Klasifikasi diperbarui bulanan untuk menjaga keseimbangan antara kecepatan deteksi dan tingkat keakuratan.
- **Ketersediaan Ground Truth**: Integrasi data lapangan (*field data*) dan kecerdasan gabungan sangat penting untuk membedakan kasus yang ambigu (seperti banjir vs. kebakaran atau pertanian vs. penebangan).

---

## 🛠️ Studi Kasus Implementation: Satellite Image Classification Simulation (CNN Concept with PyTorch/Scikit-Learn)

Dalam modul ini, disediakan script Python untuk mensimulasikan **Klasifikasi Penggerak Deforestasi (Satellite Multiband Feature Classification)** menggunakan algoritma *Machine Learning / Convolutional Features Simulation* untuk memprediksi penyebab hilangnya tutupan pohon berdasarkan sinyal spektral/radar.

---

## 🚀 Cara Menjalankan Program

1. **Clone repositori ini atau ekstrak file ZIP.**
2. Pastikan Python 3.8+ sudah terinstal.
3. Install dependencies yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan script klasifikasi citra satelit:
   ```bash
   python satellite_deforestation_driver.py
   ```

---

## 📂 Struktur File

- `README.md`: Dokumen penjelasan materi dan panduan.
- `satellite_deforestation_driver.py`: Program Python klasifikasi multi-sensor (fitur radar + optik) untuk menentukan penyebab deforestasi.
- `requirements.txt`: Library pendukung (`pandas`, `numpy`, `scikit-learn`).
