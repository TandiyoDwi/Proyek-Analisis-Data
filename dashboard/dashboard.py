import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("../dashboard/main_data.csv")

st.title("Diagram Penyewaan Sepeda Tiap Musim dan Tahun")

# Mapping kategori data
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['yr'] = day_df['yr'].map({
    0: '2011', 1: '2012',
})

day_df['season'] = day_df['season'].astype('category')
day_df['yr'] = day_df['yr'].astype('category')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])  # Konversi ke tipe datetime

# Sidebar Filter
option = st.sidebar.selectbox("Pilih Data", ["Pinjaman Tiap Musim", "Performa Rental 2 Tahun"])
season_filter = st.sidebar.selectbox("Filter berdasarkan musim:", ["All"] + list(day_df['season'].unique()))
date_range = st.sidebar.date_input("Pilih rentang tanggal:", [day_df['dteday'].min(), day_df['dteday'].max()])

# Menampilkan rentang tanggal yang dipilih
st.write(f"**Rentang tanggal yang dipilih:** {date_range[0]} hingga {date_range[1]}")

if option == "Pinjaman Tiap Musim":
    st.header("Pinjaman Sepeda Tiap Musim")
    
    # Filter data berdasarkan musim dan tanggal
    filtered_df = day_df.copy()
    if season_filter != "All":
        filtered_df = filtered_df[filtered_df['season'] == season_filter]
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[(filtered_df['dteday'] >= pd.to_datetime(start_date)) & (filtered_df['dteday'] <= pd.to_datetime(end_date))]
    
    season_usage = filtered_df.groupby("season", observed=False)[["registered", "casual"]].sum().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.bar(
        season_usage["season"],
        season_usage["registered"],
        label="Registered",
        color="blue"
    )
    plt.bar(
        season_usage["season"],
        season_usage["casual"],
        label="Casual",
        color="red"
    )

    plt.xlabel(None)
    plt.ylabel(None)
    plt.title("Jumlah penyewaan sepeda berdasarkan musim")
    plt.legend()
    st.pyplot(fig)

elif option == "Performa Rental 2 Tahun":
    st.header("Performa Rental Sepeda dalam 2 Tahun")
    rent_year = day_df.groupby("yr", observed=False)[["cnt"]].sum().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.bar(
        rent_year["yr"],
        rent_year["cnt"],
        color= "blue",
        label="2011 - 2012"
    )

    plt.xlabel(None)
    plt.ylabel(None)
    plt.title("Jumlah Penyewaan Sepeda Berdasarkan Tahun")
    plt.legend()
    st.pyplot(fig)