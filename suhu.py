
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('hehe :sparkles:')
st.subheader('Konversi Suhu')

nama = st.text_input('Nama', 'Naily', label_visibility='collapsed')
st.write('Halo ', nama)

c1, c2 = st.columns(2)

with c1:
 x = st.number_input('suhu ',value=100)
 st.write('Dikonversi ke: ')
with c2:
 satuan = st.selectbox(
    'Satuan',
    ('C','F', 'R', 'K'), key='k1')
 konversi = st.selectbox(
    'Konversi',
    ('C','F', 'R', 'K'), key='k2')


if(satuan=='C'):
 if(konversi=='C'):
  y = x
 elif(konversi=='F'):
  y = x*9/5 + 32
 elif(konversi=='R'):
  y = x*4/5
 elif(konversi=='K'):
  y = x + 273
elif(satuan=='F'):
 if(konversi=='F'):
  y = x
 elif(konversi=='C'):
  y = (x-32)*5/9
 elif(konversi=='R'):
  y = (x-32)*4/9
 elif(konversi=='K'):
  y = (x-32)*5/9 + 273
elif(satuan=='R'):
 if(konversi=='F'):
  y = x*9/4 + 32
 elif(konversi=='C'):
  y = x*5/4 
 elif(konversi=='R'):
  y = x
 elif(konversi=='K'):
  y = x*5/4 + 273
if(satuan=='K'):
 if(konversi=='C'):
  y = x - 273
 elif(konversi=='F'):
  y = (x-273)*9/5 + 32
 elif(konversi=='R'):
  y = (x-273)*4/5
 elif(konversi=='K'):
  y = x 


st.write(x,' ',satuan,' = ',y,' ', konversi) 
                     
st.caption('source: Nugroho Adi Pramono nugroho.xyz')

