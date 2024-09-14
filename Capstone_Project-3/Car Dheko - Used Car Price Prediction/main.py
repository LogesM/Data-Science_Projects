import streamlit as st
import webbrowser
import pandas as pd
import plotly.express as px
from PIL import Image
import pickle

# icon=Image.open(r"C:\Users\ADMIN\Videos\career_fair\carDekho\download.png")
# st.set_page_config(page_title='CarDekho Used Car Price Prediction',
#                 page_icon= icon,  
#                    layout="wide", initial_sidebar_state="auto") 
df=pd.read_csv(r"dont_ordinalencoding_cardekho.csv")
df1=pd.read_csv(r"ml_cardekho.csv")
df2=pd.read_csv(r"cardekho.csv")

with st.sidebar:
    st.sidebar.markdown("# :rainbow[Select an option to filter:]")
    selected = st.selectbox("**Menu**", ("Home","Analysis","prediction"))
    
    
if selected=="Home":
   

    st.markdown('## :green[welcome to Home page:]')
    with st.form(key = 'form',clear_on_submit=False):   
        st.markdown('## :blue[Project Title:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;CarDekho Used Car Price Prediction ")
        st.markdown('## :blue[Skills takes away From This project:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Data Cleaning, Exploratory Data Analysis (EDA), Visualization and Machine Learning")
        st.markdown('## :blue[Domain:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Automobile")
        st.markdown('## :blue[Problem:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; The primary objective of is project is to create a data science solution for the car")
        st.subheader('for predicting used car prices accurately by analyzing a diverse dataset including car model,')
        st.subheader('no. of owners, age, mileage, fuel type, kilometers driven, features and location. The aim is ')
        st.subheader('to build a machine learning model that offers users to find current valuations for used cars.')
        

        link="https://github.com/LogesM/Data-Science_Projects/Capstone_project-2"
        link1='www.linkedin.com/in/logeswaran-mohanraj-172000'
        colum3,colum4,colum5= st.columns([0.015,0.020,0.1])
        with colum3:
            if st.form_submit_button('GidHub',use_container_width=True):
                webbrowser.open_new_tab(link)
        with colum4:
            if st.form_submit_button("LinkedIn",use_container_width=True):
                webbrowser.open_new_tab(link1)
                               
if selected=='prediction':
    st.markdown('## :green[welcome to Car Price Prediction :]')
    with st.form(key = 'form',clear_on_submit=False):    
        def inver(x):
            if x!=0:
                return 1/x
            else:
                return 0   
            
                
        column1,column2 = st.columns([2,2], gap = 'small')
        fuel_type1 = df['fuel_type'].unique()
        min_kilometer = df2['kilometer'].min()
        max_kilometer = df2['kilometer'].max()
        transmission_type = df['transmission_type'].unique()
        # owner_no = df['owner_no']
        # brand1= df['brand'].unique()
        model1 = df['model'].unique()
        # model_year = df['model_year']
        min_seats_count = df['seats_count'].min()
        max_seats_count = df['seats_count'].max()
        min_car_engine_cc = df['car_engine_cc'].min()
        max_car_engine_cc = df['car_engine_cc'].max()
        min_mileage = df['mileage'].min()
        max_mileage = df['mileage'].max()
        location = df['location'].unique()
        age = df['age']       
                
        with column1:

            fuel_type_1 = st.radio("**:green[Select a fuel_type:]**",fuel_type1,horizontal=True )
            kilometer_2 = st.number_input(f'**:green[Enter kilometer:]  &nbsp;&nbsp; :red[(Minimum : {min_kilometer}, Maximun : {max_kilometer})]**',format="%.1f")
            seats_count_8 = st.number_input(f'**:green[Enter seats_count of:] &nbsp;&nbsp;  :red[(Minimum : {min_seats_count}, Maximun : {max_seats_count})]**',format="%.0f")
            owner_no_4 = st.number_input(f'**:green[Enter owner_no:]**',format="%.0f") 
            # brand_5 = st.selectbox("**Select a brand:**",brand1)
            model_6 = st.selectbox("**:green[Select a model:]**",model1)
            model_year_7 = st.number_input(f'**:green[Enter the Manufacturing year:]**',format="%.0f")
            
        with column2:
            transmission_type_3 = st.radio(f'**:green[Select transmission_type:]**',transmission_type,horizontal=True) 
            
            car_engine_cc_9 = st.number_input(f'**:green[Enter car_engine_cc of:] &nbsp;&nbsp;   :red[(Minimum : {min_car_engine_cc}, Maximun : {max_car_engine_cc})]**',format="%.0f")
            mileage_10 = st.number_input(f'**:green[Enter Mileage of:] &nbsp;&nbsp;   :red[(Minimum : {min_mileage}, Maximun : {max_mileage})]**',format="%.1f")
            location_11 = st.selectbox("**:green[Select a Location:]**",location)
            age_12 = st.number_input(f'**:green[Enter Age:]**',format="%.0f") 
        
        
        for i in df.columns:
            if (df[i].dtype == 'object'):
                col_name = i
                decode = df[i].sort_values().unique() # status
                encode = df1[i].sort_values().unique() # 0,1,2
                globals()[col_name] = {}
                globals()[i] = dict(zip(decode, encode))

        with open(r"random_regression.pkl",'rb') as file:
            Result = pickle.load(file)
        
        kilo=inver(kilometer_2)
        
        d=[[fuel_type[fuel_type_1],kilo,transmission_type[transmission_type_3],owner_no_4,model[model_6],model_year_7,seats_count_8,car_engine_cc_9,mileage_10,location[location_11],age_12]]  
        
        # st.write(d)
        if st.form_submit_button("submit"): 
                k=Result.predict(d)
                
                st.write(f"# :green[Prediction of current weekly sales price is: :red['{k}']]")
            
if selected =='Analysis':
    
    data=df2.groupby(['registration_year']).sum(['price']).sort_values('registration_year')
    # data
    fig = px.line(data, y='price', x=data.index,title="Total price in year vize line plot:")
    # fig.show()
    fig.update_traces(line_color='#8EF316',line={'width':3})
    st.plotly_chart(fig,use_container_width=True)
    
    ######################
    
    data = df2.groupby(['brand'])['seats_count'].max().reset_index()
    # data
    fig=px.area(data, x = data['brand'], y = data['seats_count'],color =data['seats_count'],title="Hightst seat count cars list:")
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)
    #######################
    
    colum3,colum4= st.columns([0.9,1])
    with colum3:
        radio=st.slider("select the year:",df2['registration_year'].max(),df2['registration_year'].min())
    
    with colum4:
        column=st.selectbox("select the columns:",(df.drop('price',axis = 1).columns))
    # st.markdown(f"** [{column} in weakly_sales]")
    data=df2[df2['registration_year']==radio]
    da=data.groupby(column)['price'].sum().reset_index()
    # # st.write(data)
    fig=px.histogram(da,x=column,y='price',title=f"{column} in price",color=da.index)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig,use_container_width=True)
    colum3,colum4= st.columns([0.9,1])
    with colum3:
        choice = st.selectbox("**Select an option to Explore their data:**", (df2.drop('price',axis = 1).columns))  
    
    st.markdown(f"## :white[Car Price vs {choice}:]")
    hist = px.histogram(df2, x = choice, y = 'price',width=950)
    st.plotly_chart(hist,use_container_width=True)
    ########################
    
    colum3,colum4= st.columns([1,1])
    with colum3:
        brand = df2.groupby('brand').count().reset_index()[['brand','fuel_type']]
        # st.dataframe(brand)
        bar = px.bar(brand, x = 'brand', y = 'fuel_type', labels={'fuel_type':'Total Count of Car brand'},width=950,color = 'brand',title="Which Car Brand is highly available:")
        bar.update_layout(showlegend=False)
        st.plotly_chart(bar,use_container_width=True)

    with colum4:
        data = df2.groupby(['brand'])['age'].max().reset_index()
        fig=px.bar(data, x = data['brand'], y = data['age'],title="Highest Oldest car list using age:")
        # fig.show()
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig,use_container_width=True)
    ##############################
    
    column1,column2=st.columns([1,1])
    with column1:
        d=st.selectbox("**Select_the_brand**:", df2['brand'].unique())
        d1=df2[df2['brand']==d]
       
    with column2:
        model_one=st.selectbox("**Select_the_car_model**:",d1['model'].unique())
        
    # model_one='Ambassador'
    
    column1,column2=st.columns([1,1])
    with column1:
        new_data=df2.groupby(['model','registration_year'])['price'].mean().reset_index()
        kd=new_data[(new_data['model']== model_one)]
        # kd
        fig=px.pie(kd,  kd['registration_year'], kd['price'],title="Sum of car price in year:")
        # fig.show()
        st.plotly_chart(fig,use_container_width=True)
        
    
    with column2:
        new_data=df2.groupby(['model']).head()
        kd=new_data[(new_data['model']== model_one)]
        # kd
        fig=px.bar(kd,  kd['registration_year'], kd['price'],title="Body type highest price:")
        # fig.show()
        st.plotly_chart(fig,use_container_width=True)
        
    new_data=df2.groupby(['model']).head()
    kd=new_data[(new_data['model']== model_one)]
    # kd
    fig=px.bar(kd,  x=kd['color'], y=kd['price'],title="Highest selling color:",color=kd['color'])
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)
    
    new_data=df2.groupby(['model']).head()
    kd=new_data[(new_data['model']== model_one)]
    # kd
    fig=px.bar(kd,  x=kd['location'], y=kd['price'],title="Location vize highest price:",color=kd['price'])
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)
    
    
    
    fg=df2[['registration_year','kilometer','price']].sort_values('registration_year',ascending=True)
    # fg
    fig=px.scatter(fg, x=fg['kilometer'], y=fg["price"],
                size="price", color="price",log_x=True, size_max=50,
                title="Store vize total_markdown in month:")
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)
        
   
