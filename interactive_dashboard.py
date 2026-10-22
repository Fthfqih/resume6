"""
Studi Kasus Materi 5: Human-Computer Interaction & Data Visualization
Pembicara: Arafat Febriandirza, Ph.D. (BRIN)
Deskripsi: Mensimulasikan pembuatan Dashboard Visualisasi Data Interaktif
           menerapkan prinsip "Overview first, zoom and filter, details-on-demand"
           serta memaksimalkan Data-Ink Ratio (Edward Tufte).
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def generate_mock_sensor_data():
    """Generasi data sampel sensor IoT / Tren Kinerja Sistem."""
    dates = pd.date_range(start="2026-10-01", periods=30, freq="D")
    np.random.seed(42)
    data = {
        "Tanggal": dates,
        "CPU_Usage_%": np.random.normal(loc=45, scale=10, size=30).round(2),
        "Memory_Usage_%": np.random.normal(loc=65, scale=8, size=30).round(2),
        "Active_Users": np.random.randint(low=120, high=500, size=30),
        "Region": np.random.choice(["Bengkulu", "Jakarta", "Bandung"], size=30)
    }
    return pd.DataFrame(data)

def build_interactive_dashboard():
    df = generate_mock_sensor_data()
    print("=== DATASET KINERJA SISTEM (SAMPLE DATA) ===")
    print(df.head())

    # 1. Line Chart: Overview Trend Kinerja CPU & Memory Seiring Waktu
    fig_line = px.line(
        df, 
        x="Tanggal", 
        y=["CPU_Usage_%", "Memory_Usage_%"],
        title="1. Overview: Tren Penggunaan Resource Sistem (Line Chart)",
        labels={"value": "Persentase (%)", "variable": "Metrik"},
        template="plotly_white"
    )
    fig_line.update_traces(mode="lines+markers")

    # 2. Bar Chart: Perbandingan Rata-rata Pengguna Aktif per Wilayah
    df_region = df.groupby("Region")["Active_Users"].mean().reset_index()
    fig_bar = px.bar(
        df_region,
        x="Region",
        y="Active_Users",
        title="2. Comparison: Rata-rata Pengguna Aktif per Wilayah (Bar Chart)",
        color="Region",
        template="plotly_white"
    )

    # Combine into a single HTML Dashboard
    html_content = f"""
    <html>
    <head>
        <title>Dashboard HCI & Data Visualization - BRIN & UNIB</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f8f9fa; }}
            h1 {{ color: #2c3e50; text-align: center; }}
            .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            .chart-box {{ margin-bottom: 40px; }}
            .footer {{ text-align: center; font-size: 12px; color: #7f8c8d; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Dashboard Visualisasi Data Interaktif</h1>
            <p><b>Materi 5:</b> Human-Computer Interaction & Data Visualization (Arafat Febriandirza, Ph.D. - BRIN)</p>
            <hr>
            <div class="chart-box">
                {fig_line.to_html(full_html=False, include_plotlyjs='cdn')}
            </div>
            <div class="chart-box">
                {fig_bar.to_html(full_html=False, include_plotlyjs=False)}
            </div>
            <div class="footer">
                Di-generate secara otomatis untuk Studi Kasus IMK & Visualisasi Data Universitas Bengkulu.
            </div>
        </div>
    </body>
    </html>
    """

    output_html = "dashboard_interactive.html"
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"\n[SUCCESS] Dashboard interaktif berhasil dibuat: {output_html}")
    print("Buka file 'dashboard_interactive.html' di browser Anda untuk melihat visualisasi interaktif.")

if __name__ == "__main__":
    build_interactive_dashboard()
