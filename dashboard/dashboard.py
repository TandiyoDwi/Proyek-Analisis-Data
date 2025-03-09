import streamlit as st
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("../data/day.csv")
hour_df = pd.read_csv("../data/hour.csv")

# Dashboard
st.title("Bike Sharing Dashboard")

# Sidebar
option = st.sidebar.selectbox("Pilih Data", [ "Pinjaman Tiap Musim", "Performa Rental 2 Tahun"])

if option == "Pinjaman Tiap Musim":
    st.header("Pinjaman Sepeda Tiap Musim")
    
    season_rentals = day_df.groupby("season")["cnt"].sum()
    fig, ax = plt.subplots()
    season_rentals.plot(kind='bar', color=['blue', 'green', 'red', 'orange'], ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Total Penyewaan")
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Musim")
    ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"], rotation=0)
    st.pyplot(fig)

elif option == "Performa Rental 2 Tahun":
    st.header("Performa Rental Sepeda dalam 2 Tahun")
    
    year_rentals = day_df.groupby("yr")["cnt"].sum()
    fig, ax = plt.subplots()
    year_rentals.plot(kind='bar', color=['blue', 'green'], ax=ax)
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Total Penyewaan")
    ax.set_title("Total Penyewaan Sepeda Tahun 2011 vs 2012")
    ax.set_xticklabels(["2011", "2012"], rotation=0)
    st.pyplot(fig)
