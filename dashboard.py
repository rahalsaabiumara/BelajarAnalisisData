import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard Analisis Data Kualitas Udara')
st.caption('Copyright by Rahalsa Abi Umara (c) 2024')

df = pd.read_csv('PRSA_Data_Wanshouxigong_20130301-20170228.csv')
df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

st.sidebar.title("Pilihan Analisis")
option = st.sidebar.selectbox("Pilih jenis analisis", ("Konsentrasi Rata-rata PM2.5", "Korelasi Variabel Cuaca"))

if option == "Konsentrasi Rata-rata PM2.5":
    st.subheader('Konsentrasi Rata-rata PM2.5 (2013-2017)')
    df['year'] = df['date'].dt.year
    pm25_mean_yearly = df.groupby('year')['PM2.5'].mean()
    def plot_pm25_mean(data):
        plt.figure(figsize=(10, 6))
        data.plot(marker='o')
        plt.title('Konsentrasi Rata-rata PM2.5 (2013-2017)')
        plt.xlabel('Tahun')
        plt.ylabel('Rata-rata PM2.5')
        plt.grid(True)
        st.pyplot(plt)
    
    plot_pm25_mean(pm25_mean_yearly)
    
    st.write('''
Dari diagram tersebut diperoleh tren kenaikan dan penurunan rata-rata konsentrasi PM2.5. 
Pada tahun 2013, konsentrasi PM2.5 dimulai pada tingkat tertentu. 
Kemudian terjadi penurunan rata-rata konsentrasi pada tahun 2014 hingga 2016. 
Lonjakan rata-rata secara signifikan kembali terjadi pada tahun 2016 hingga 2017.
''')

elif option == "Korelasi Variabel Cuaca":
    st.subheader('Korelasi Antara Variabel Cuaca dan Polusi')
    correlation_matrix = df[['TEMP', 'PRES', 'DEWP', 'RAIN']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Korelasi Antara Variabel Cuaca')
    st.pyplot(plt) 
    st.write('''
Heatmap ini menunjukkan korelasi antara empat variabel, yaitu antara lain TEMP (suhu), PRES (tekanan), DEWP (titik embun), dan RAIN (curah hujan). Suhu (TEMP) memiliki korelasi positif dengan  titik embun (DEWP) yang menunjukkan bahwa ketika suhu meningkat, kelembapan juga meningkat, dan memiliki korelasi negatif dengan tekanan udara (PRES), dimana suhu yang lebih tinggi cenderung berhubungan dengan tekanan yang lebih rendah
''')