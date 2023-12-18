
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('hehe :sparkles:')
st.subheader('Plot by Bapak Nug')

nama = st.text_input('Nama', 'Naily', label_visibility='collapsed')
st.write('Halo ', nama)
option = st.selectbox(
    'satuan',
    ('C','F', 'R', 'K'))

f1 = st.number_input('f1= ', value=1)
 
st.caption('source: Nugroho Adi Pramono nugroho.xyz')

