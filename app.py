# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:10:25 2022

@author: dell
"""

import numpy as np
import joblib
import streamlit as st

#Loading the saved model
loaded_model=joblib.load("Sales_store_prediction.joblib")
#creating a function for prediction

def sales_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

   
  
def main():
    
    #creating a title
    st.title('Store sales Prediction Web app')
    
    #Getting input Data from User
    
    Item_Weight=st.number_input('Item_Weight',min_value=1.000,max_value=50.000)
    Item_Fat_Content=st.selectbox("Item Fat Content",["Low Fat","Regular"])
    Item_Visibility=st.number_input('Item_Visibility',min_value=0.0000000,max_value=1.0000000)
    Item_Type=st.selectbox('Item_Type',['Fruits and Vegetables','Snack Foods','Frozen Foods','Dairy','Canned',
                                        'Baking Goods','Health and Hygiene','Soft Drinks','Meat','Breads','Hard Drinks',
                                        'Starchy Foods','Breakfast','Seafood','Others'])
    Item_MRP=st.number_input('Item_MRP',min_value=20.0000,max_value=500.0000)
    Outlet_Establishment_Year=st.selectbox('Outlet_Establishment_Year',[1985,1987,1997,1998,1999,2002,2004,2007,2009])
    Outlet_Size=st.selectbox('Outlet_Size',['Small','Medium','High'])
    Outlet_Location_Type=st.selectbox('Outlet_Location_Type',['Tier 1','Tier 2','Tier 3'])
    Outlet_Type=st.selectbox('Outlet_Type',['Supermarket Type1','Grocery Store','Supermarket Type3','Supermarket Type2'])
    
    sq_Item_Visibility=np.sqrt(Item_Visibility)
    #coading for prediction
    diagnosis=[]
    
    #creating a button
    if st.button('sales prediction'):
        
        data=[Item_Weight, Item_Fat_Content, sq_Item_Visibility, Item_Type,
        Item_MRP, Outlet_Establishment_Year, Outlet_Size,
        Outlet_Location_Type,Outlet_Type]
        
        data1=[]
        data1.append(data[0])
        if data[1]=='Low Fat':
            data1.append(1)
        else:
            data1.append(2)
        data1.append(data[2]*data[2])
        
        if data[3]=='Fruits and Vegetables':
            data1.append(1)
        if data[3]=='Snack Foods':
            data1.append(2)
        if data[3]=='Household':
            data1.append(3)
        if data[3]=='Frozen Foods':
            data1.append(4)
        if data[3]=='Dairy':
            data1.append(5)
        if data[3]=='Canned':
            data1.append(6)
        if data[3]=='Baking Goods':
            data1.append(7)
        if data[3]=='Health and Hygiene':
            data1.append(8)
        if data[3]=='Soft Drinks':
            data1.append(9)
        if data[3]=='Meat':
            data1.append(10)
        if data[3]=='Breads':
            data1.append(11)
        if data[3]=='Hard Drinks':
            data1.append(12)
        if data[3]=='Others':
            data1.append(13)
        if data[3]=='Starchy Foods':
            data1.append(14)
        if data[3]=='Breakfast':
            data1.append(15)
        if data[3]=='Seafood':
            data1.append(16)
       
            
        data1.append(data[4])
        data1.append(data[5])
        
        if data[6]=='High':
            data1.append(1)
        if data[6]=='Medium':
            data1.append(2)
        if data[6]=='Small':
            data1.append(3)
       
            
        if data[7]=='Tier 1':
            data1.append(1)
        if data[7]=='Tier 2':
            data1.append(2)
        if data[7]=='Tier 3':
            data1.append(3)
        else:
            print("Invalid")
        
        if data[8]=='Supermarket Type1':
            data1.append(1)
        if data[8]=='Grocery Store':
            data1.append(2)
        if data[8]=='Supermarket Type3':
            data1.append(3)
        if data[8]=='Supermarket Type2':
            data1.append(4)
        
        diagnosis=sales_prediction(data1)
        
        
    st.success(diagnosis)
    
if __name__== '__main__':
    main()
        
