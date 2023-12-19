
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('hehe :sparkles:')
st.subheader('Plot by Bapak Nug')

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

st.write(x,' ',satuan,' = ', konversi) 
                     
st.caption('source: Nugroho Adi Pramono nugroho.xyz')

