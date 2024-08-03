# importing libraries
import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# kerala bus
lists_kl=[]
df_kl=pd.read_csv("df_kl.csv")
for i,r in df_kl.iterrows():
    lists_kl.append(r["Route_Name"])
    
#Andhra bus
lists_an=[]
df_an=pd.read_csv("df_an.csv")
for i,r in df_an.iterrows():
    lists_an.append(r["Route_Name"])
    
#Telungana bus
lists_tl=[]
df_tl=pd.read_csv("df_tl.csv")
for i,r in df_tl.iterrows():
    lists_tl.append(r["Route_Name"])
    
#Goa bus
lists_goa=[]
df_goa=pd.read_csv("df_goa.csv")
for i,r in df_goa.iterrows():
    lists_goa.append(r["Route_Name"])
    
#Rajastan bus
lists_rj=[]
df_rj=pd.read_csv("df_rj.csv")
for i,r in df_rj.iterrows():
    lists_rj.append(r["Route_Name"])
    
# South bengal bus 
lists_sb=[]
df_sb=pd.read_csv("df_sb.csv")
for i,r in df_sb.iterrows():
    lists_sb.append(r["Route_Name"])
    
# Haryana bus
lists_hr=[]
df_hr=pd.read_csv("df_hr.csv")
for i,r in df_hr.iterrows():
    lists_hr.append(r["Route_Name"])
    
#Assam bus
lists_as=[]
df_as=pd.read_csv("df_as.csv")
for i,r in df_as.iterrows():
    lists_as.append(r["Route_Name"])
    
#UP bus
lists_up=[]
df_up=pd.read_csv("df_up.csv")
for i,r in df_up.iterrows():
    lists_up.append(r["Route_Name"])
    
#West bengal bus
lists_wb=[]
df_wb=pd.read_csv("df_wb.csv")
for i,r in df_wb.iterrows():
    lists_wb.append(r["Route_Name"])
    
#StreamLit page setting

with st.sidebar:
    st.title(":green[Red Bus Information Gathering]")
    st.subheader(":red[Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit]")
    st.caption("Tool and Technologies Covered")
    st.caption("1. Python")
    st.caption("2. Web Scraping using Selenium")
    st.caption("3. Data base management by MySql")
    st.caption("4. Streamlit")
    
# States and Routes page setting
S = st.selectbox("Lists of States", ["Kerala", "Andhra Pradesh", "Telugana", "Goa", "Rajastan", 
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"])
col1,col2=st.columns(2)

with col2:
    select_fare = st.radio("Choose bus fare range", ("50-2000","50-500","500-1000", "1000 and above"))

#TIME=st.time_input("select the time")

# Kerala bus fare filtering
if S == "Kerala":
    K = st.selectbox("List of routes",lists_kl)

    def type_and_fare(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  # assuming a high max value for "2000 and above"


        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare( select_fare)
    st.dataframe(df_result)
    
# Adhra Pradesh bus fare filtering
if S=="Andhra Pradesh":
    A=st.selectbox("list of routes",lists_an)

    def type_and_fare_A(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  

        
        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare_A(select_fare)
    st.dataframe(df_result)
    
# Telugana bus fare filtering
if S=="Telugana":
    T=st.selectbox("list of routes",lists_tl)

    def type_and_fare_T(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        # elif fare_range == "1000-2000":
        #     fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 1000, 100000  

        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare_T(select_fare)
    st.dataframe(df_result)
    
# Goa bus fare filtering
if S=="Goa":
    G=st.selectbox("list of routes",lists_goa)

    def type_and_fare_G(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  


        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{G}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare_G(select_fare)
    st.dataframe(df_result)

# Rajastan bus fare filtering
if S=="Rajastan":
    R=st.selectbox("list of routes",lists_rj)

    def type_and_fare_R(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  


        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare_R(select_fare)
    st.dataframe(df_result)
    
# South Bengal bus fare filtering       
if S=="South Bengal":
    SB=st.selectbox("list of routes",lists_sb)

    def type_and_fare_SB(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
            # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  

        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{SB}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare_SB(select_fare)
    st.dataframe(df_result)
    
# Haryana bus fare filtering
if S=="Haryana":
    H=st.selectbox("list of routes",lists_hr)

    def type_and_fare_H(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  

        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{H}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare_H(select_fare)
    st.dataframe(df_result)
    
# Assam bus fare filtering
if S=="Assam":
    AS=st.selectbox("list of routes",lists_as)

    def type_and_fare_AS(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  

        query = f'''
                SELECT * FROM bus_details 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}"
                ORDER BY Price and Start_time DESC
            '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
        return df

    df_result = type_and_fare_AS(select_fare)
    st.dataframe(df_result)

# Uttra Pradesh bus fare filtering
if S=="Uttar Pradesh":
    UP=st.selectbox("list of routes",lists_up)

    def type_and_fare_UP(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  
        
        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{UP}"
            ORDER BY Price and Start_time DESC
        '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])
        return df

    df_result = type_and_fare_UP(select_fare)
    st.dataframe(df_result)
    
# West Bengal bus fare filtering
if S=="West Bengal":
    WB=st.selectbox("list of routes",lists_wb)

    def type_and_fare_WB(fare_range):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Loges179@", database="red_bus_db")
        cursor = mydb.cursor()
        # Define fare range based on selection
        if fare_range == "50-2000":
            fare_min, fare_max = 50, 2000
        elif fare_range == "50-500":
            fare_min, fare_max = 50, 500
        elif fare_range == "500-1000":
            fare_min, fare_max = 50, 1000
        else:
            fare_min, fare_max = 1000, 100000  

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{WB}"
            ORDER BY Price and Start_time  DESC
        '''
        cursor.execute(query)
        out = cursor.fetchall()
        mydb.close()

        df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])
        return df

    df_result = type_and_fare_WB(select_fare)
    st.dataframe(df_result)

