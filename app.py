import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime, timedelta

st.set_page_config(page_title="TradeCompass AI", layout="wide")

st.title("🛰️ TRADECOMPASS AI - KÜRESEL EMTAA İSTİHBARAT SİTESİ")
st.write("---")

# Canlı simüle veri tabanı
canli_gemiler = {
    "9432101 / MV SUNFLOWER-1 (Ham Ayçiçek Yağı)": {"lat": 38.25, "lon": 26.85, "tip": "Sıvı Yük Tankeri (Yağ)", "hiz": "12.4 Knot", "hedef": "İzmir Port"},
    "9567822 / MV PACIFIC-METALS (Alüminyum A7)": {"lat": 39.12, "lon": 25.45, "tip": "Kuru Yük (Alüminyum)", "hiz": "14.1 Knot", "hedef": "Yarımca Port"}
}

# Sol Menü Tasarımı
st.sidebar.header("💳 Mikro Ödeme Paneli")
gemi_secim = st.sidebar.selectbox("🚢 Takip Edilecek Gemi:", list(canli_gemiler.keys()))
satinal_butonu = st.sidebar.button("⚡ 13$ CANLI TAKİP BAŞLAT")

# Sağ Harita Ekranı
if satinal_butonu:
    gemi_detay = canli_gemiler[gemi_secim]
    bitis = datetime.now() + timedelta(hours=24)
    
    st.success("💳 MİKRO ÖDEME ONAYLANDI!")
    col1, col2, col3 = st.columns(3)
    col1.metric("Tahsil Edilen", "13.00 USD")
    col2.metric("API Maliyeti", "3.00 USD")
    col3.metric("Şirket Net Kârı", "10.00 USD")
    
    st.info(f"⏱️ 24 Saatlik Sayaç Aktif! Bitiş Zamanı: {bitis.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Harita Motoru
    harita = folium.Map(location=[gemi_detay["lat"], gemi_detay["lon"]], zoom_start=7, tiles="Cartodb Positron")
    folium.Marker(
        location=[gemi_detay["lat"], gemi_detay["lon"]],
        popup=f"<b>Gemi:</b> {gemi_secim}<br><b>Hız:</b> {gemi_detay['hiz']}",
        icon=folium.Icon(color="green", icon="ship", prefix="fa")
    ).add_to(harita)
    
    st_folium(harita, width=800, height=500)
else:
    st.warning("⚠️ Şu an 24 saat gecikmeli ücretsiz sürümdesiniz. Canlı uydu verisi ve harita aktivasyonu için soldaki yeşil butona basarak 13$'lık mikro ödemeyi simüle edin.")
