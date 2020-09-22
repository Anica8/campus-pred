#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[2]:


place=pd.read_csv("place.csv")


# In[3]:


place


# In[4]:


place.isnull().sum()


# In[5]:


place=place.fillna(0)


# In[6]:


place.isnull().sum()


# In[7]:


sex=pd.get_dummies(place["gender"],drop_first=True)


# In[8]:


sex


# In[9]:


place=pd.concat([place.drop("gender",axis=1),sex],axis=1)


# In[10]:


place.head(5)
place.isnull().sum()


# In[11]:


board=pd.get_dummies(place["ssc_b"],drop_first=True)
board


# In[12]:


place=pd.concat([place.drop("ssc_b",axis=1),board],axis=1)
place.head(7)


# In[13]:


stream=pd.get_dummies(place["hsc_s"],drop_first=True)
stream


# In[14]:


place=pd.concat([place.drop("hsc_s",axis=1),stream],axis=1)
place


# In[15]:


exp=pd.get_dummies(place["workex"],drop_first=True)
exp


# In[16]:


place=pd.concat([place.drop("workex",axis=1),exp],axis=1)
place


# In[17]:


place.drop("Others",axis=1)


# In[18]:


place.head(5)


# In[19]:


place=place.drop("Others",axis=1)


# In[20]:


place.head(5)


# In[21]:


place=place.drop("hsc_b",axis=1)
place.head(5)


# In[22]:


sa=pd.get_dummies(place["degree_t"],drop_first=True)
sa


# In[23]:


place=pd.concat([place.drop("degree_t",axis=1),sa],axis=1)
place.head(5)


# In[24]:


special=pd.get_dummies(place["specialisation"],drop_first=True)
special


# In[25]:


place=pd.concat([place.drop("specialisation",axis=1),special],axis=1)
place.head(5)


# In[26]:


pla=pd.get_dummies(place["status"])
pla


# In[27]:


place=pd.concat([place.drop("status",axis=1),pla],axis=1)
place.head(5)


# In[28]:


place


# In[29]:


place=place.drop("sl_no",axis=1)
place.head(10)


# In[30]:


place=place.drop("Not Placed",axis=1)
place=place.drop("salary",axis=1)
place=place.rename(columns={"ssc_p":"10th_p","hsc_p":"12th_p","Yes":"work_exp","M":"gender","Mkt&HR":"mba_spl","Others":"field_1","Sci&Tech":"field_2"})
place.head(5)


# In[31]:


sns.countplot(x="Placed", hue="gender",data=place)


# In[32]:


sns.countplot(x="Placed", hue="work_exp", data=place)


# In[33]:


sns.countplot(x="Placed", hue="mba_spl", data=place)


# In[34]:


X=place.drop("Placed",axis=1)
y=place["Placed"]


# In[35]:


from sklearn.model_selection import train_test_split


# In[36]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)


# In[ ]:





# In[37]:


from sklearn.linear_model import LogisticRegression


# In[38]:


logmodel=LogisticRegression(max_iter=5000)


# In[39]:


logmodel.fit(X_train,y_train)


# In[40]:


predictions=logmodel.predict(X_test)


# In[41]:


from sklearn.metrics import classification_report


# In[42]:


classification_report(y_test,predictions)


# In[43]:


from sklearn.metrics import confusion_matrix


# In[44]:


confusion_matrix(y_test,predictions)


# In[45]:


from sklearn.metrics import accuracy_score


# In[46]:


accuracy_score(y_test,predictions)


# In[47]:


a=[[79,78,77.4,86.5,66.28,1,0,1,1,0,1,0]]
p=logmodel.predict(a)
print(p)


# In[ ]:





# In[ ]:





# In[ ]:




