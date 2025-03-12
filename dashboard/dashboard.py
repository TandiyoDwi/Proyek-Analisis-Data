import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("dashboard/main_data.csv")

st.title("Diagram Penyewaan Sepeda Tiap Musim dan Tahun")

# Merubah data
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['yr'] = day_df['yr'].map({
    0: '2011', 1: '2012',
})

day_df['season'] = day_df['season'].astype('category')
day_df['yr'] = day_df['yr'].astype('category')

# Sidebar
option = st.sidebar.selectbox("Pilih Data", ["Pinjaman Tiap Musim", "Performa Rental 2 Tahun"])

if option == "Pinjaman Tiap Musim":
    st.header("Pinjaman Sepeda Tiap Musim")
    season_usage = day_df.groupby("season", observed=False)[["registered", "casual"]].sum().reset_index()
    
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
