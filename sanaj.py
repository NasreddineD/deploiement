#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[13]:


data = pd.read_csv("./df_foodapp.csv")

data=data.reset_index(drop=True)

st.title("SANAJ")
st.plotly_chart(px.histogram(data, x="nutriscore_grade", color="nova_group"))


# In[10]:


st.plotly_chart(px.histogram(data, x="nutriscore_grade", color="ecoscore_grade_fr").update_xaxes(categoryorder="category ascending"))


# In[12]:


st.plotly_chart(px.pie(data, values='nova_group', names='nova_group', color_discrete_sequence=px.colors.sequential.RdBu))


# In[18]:


st.plotly_chart(px.sunburst(data, 
                  path=['nutriscore_grade', 'nova_group'],
                  values='ecoscore_score_fr',
                  title="Nova_group proportion by Nutriscore"
                 ))

