# Seri Studi Kasus 5: Human-Computer Interaction & Data Visualization

Repositori ini berisi ringkasan materi, studi kasus, serta implementasi coding untuk **Materi 5** pada kegiatan *Informatics Practitioner Lecture Series* Universitas Bengkulu.

- **Pembicara**: Arafat Febriandirza, Ph.D. (Chair of Research Group for Human Computer Interaction and Visualization, Pusat Riset Sains Data dan Informasi - BRIN / Badan Riset dan Inovasi Nasional)
- **Topik**: *Human-Computer Interaction (HCI) & Data Visualization* (Panduan Komprehensif Membangun Antarmuka Intuitif, Psikologi Kognitif, dan Visualisasi Data Interaktif)

---

## 📌 Ringkasan Materi

### 1. Pengantar & Ruang Lingkup IMK (Human-Computer Interaction)
- **Definisi**: IMK/HCI adalah studi ilmu yang mempelajari jembatan komunikasi dua arah antara manusia (*Human*), sistem pemroses perintah (*Computer*), dan antarmuka (*Interface*).
- **Prinsip Utama**: *"You are not your user"* – Perancang UI/UX dilarang merancang sistem berdasarkan selera pribadi (*Self-Reference Design*), melainkan harus menerapkan **User-Centered Design (UCD)**.
- **Evolusi Antarmuka**: Punch Cards (1940-an) -> Command Line Interface / CLI (1970-an) -> Graphical User Interface / GUI (1980-an) -> Natural User Interface / NUI (Touch, Voice, AR/VR, Gesture).

### 2. Aspek Psikologi Kognitif & Beban Otak (*Cognitive Load*)
- **working Memory vs Long-Term Memory**: Otak hanya dapat menyimpan sekitar $7 \pm 2$ unit informasi sementara di *Working Memory*. Oleh karena itu, prinsip desain utama adalah utamakan **Recognition over Recall** (gunakan simbol/ikon standar yang sudah diingat pengguna di *Long-Term Memory*).
- **Teori Beban Kognitif (*Cognitive Load Theory*)**:
  - *Intrinsic Load*: Kesulitan alami data/informasi.
  - *Germane Load*: Beban positif untuk membangun pemahaman baru.
  - *Extraneous Load*: **Beban sia-sia** akibat layout berantakan/bingung. Tugas desainer adalah menekan *Extraneous Load* mendekati nol.
- **Hukum Gestalt**: Otak mengelompokkan elemen visual berdasarkan *Proximity* (kedekatan), *Similarity* (kesamaan), *Enclosure* (pengurungan/batas), *Continuity*, *Closure*, dan *Figure/Ground*.

### 3. Evaluasi Usability & Standar Heuristik
- **10 Prinsip Heuristik Jakob Nielsen**:
  1. *Visibility of System Status* (contoh: loading bar, indikator status).
  2. *Match Between System and Real World* (bahasa/ikon familiar seperti ikon tempat sampah untuk hapus).
  3. *User Control and Freedom* (tombol Undo/Cancel/Pintu keluar darurat).
  4. *Consistency and Standards* (keseragaman aturan & warna).
  5. *Error Prevention* (pencegahan kesalahan sebelum terjadi).
  6. *Recognition Rather Than Recall* (opsi terlihat jelas).
  7. *Flexibility and Efficiency of Use* (tombol pintas/shortcut).
  8. *Aesthetic and Minimalist Design* (ruang kosong/whitespace proporsional).
  9. *Help Users Recognize, Diagnose, and Recover from Errors* (pesan error ramah pengguna).
  10. *Help and Documentation* (pusat bantuan/FAQ).

### 4. Visualisasi Data Interaktif & Dashboard
- **Prinsip Data-Ink Ratio (Edward Tufte)**: Memaksimalkan informasi data murni dan membuang elemen hiasan yang tidak berguna (*Chartjunk* seperti efek 3D berlebihan atau garis kisi tebal).
- **Visual Information Seeking Mantra (Ben Shneiderman)**: *"Overview first, zoom and filter, then details-on-demand"*.
  1. Tampilkan gambaran umum data secara makro.
  2. Sediakan fitur filter/zoom untuk menyaring data spesifik.
  3. Berikan rincian data detail saat elemen di-hover atau di-klik (*Details-on-demand*).

---

## 🛠️ Studi Kasus Implementation: Interactive Data Visualization Dashboard (Plotly & Dash)

Dalam modul ini, disediakan contoh aplikasi **Dashboard Visualisasi Data Interaktif** berbasis Python menggunakan pustaka `plotly` dan `pandas` yang menerapkan prinsip *User-Centered Design*, *Filtering*, dan *Overview First, Details-on-Demand*.

---

## 🚀 Cara Menjalankan Program

1. **Clone repositori ini atau ekstrak file ZIP.**
2. Pastikan Python 3.8+ sudah terinstal.
3. Install dependencies yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan script visualisasi interaktif:
   ```bash
   python interactive_dashboard.py
   ```

---

## 📂 Struktur File

- `README.md`: Dokumen penjelasan materi dan panduan.
- `interactive_dashboard.py`: Program Python visualisasi data interaktif (Line Chart, Bar Chart, & Scatter Plot) menggunakan Plotly HTML.
- `requirements.txt`: Library pendukung (`pandas`, `plotly`).
