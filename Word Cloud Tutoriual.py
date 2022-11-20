#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
# nltk.download('stopwords')
# nltk.download('punkt')


# In[ ]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
print(stop_words) 


# In[ ]:


data = ''' Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the 
natural intelligence displayed by humans or animals. Leading AI textbooks define the field as the study 
of "intelligent agents": any system that perceives its environment and takes actions that maximize its chance 
of achieving its goals. Some popular accounts use the term "artificial intelligence" to describe machines that 
mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving", 
however this definition is rejected by major AI researchers. AI applications include advanced web search engines, 
recommendation systems (used by YouTube, Amazon and Netflix), understanding human speech (such as Siri or Alexa), 
self-driving cars (e.g. Tesla), and competing at the highest level in strategic game systems (such as chess and Go),
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the 
definition of AI, a phenomenon known as the AI effect. For instance, optical character recognition is frequently 
excluded from things considered to be AI, having become a routine technology.'''


# In[ ]:


def data_processing(data):
    #lowercase conversion
    data = data.lower()
    #word tokenize data
    data_tokens = word_tokenize(data)
    #remove stopwords
    processed_words = [w for w in data_tokens if not w in stop_words]
    return " ".join(processed_words)


# In[4]:


data_processed = data_processing(data)


# In[9]:


plt.figure(figsize = (20,20), facecolor = 'none') 
wordcloud = WordCloud(background_color=None, mode='RGBA').generate(data_processed) 
plt.imshow(wordcloud, interpolation=None) 
plt.axis("off") 
plt.show()


# In[10]:


plt.figure(figsize = (10, 10), facecolor = 'red') 
wordcloud = WordCloud().generate(data_processed)
plt.imshow(wordcloud)
plt.axis("off") 
plt.show()


# In[11]:


plt.figure(figsize = (10, 10), facecolor = 'none') 
wordcloud = WordCloud(background_color="white").generate(data_processed)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# In[5]:


# import os
# os.chdir(r'<Add your file path here>')


# In[13]:


wordcloud.to_file("wordcloud.png")


# In[7]:


from PIL import Image
mask = np.array(Image.open("brain.jpg"))


# In[9]:


mwc = WordCloud(background_color='black', mask=mask)
mwc.generate(data_processed)
plt.figure(figsize=(10, 10))
plt.imshow(mwc)
plt.axis('off')
plt.show()


# In[19]:


quotes_data = pd.read_excel('data_file.xlsx')
print (quotes_data)


# In[20]:


quotes_data.Quote = quotes_data['Quote'].apply(data_processing)


# In[21]:


quote_text = ' '.join([ w for w in quotes_data['Quote']])
plt.figure(figsize = (15,20), facecolor = 'None') 
wordcloud = WordCloud(width=480, height=240,background_color=None, mode='RGBA').generate(quote_text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# In[22]:


wordcloud.to_file("wordcloud_white.png")


# In[23]:


mwc2 = WordCloud(background_color='white', mask=mask)
mwc2.generate(quote_text)
plt.figure(figsize=(10, 10))
plt.imshow(mwc2)
#plt.tight_layout(pad=0)
plt.axis('off')
plt.show()


# In[24]:


mwc2.to_file("wordcloud_white.png")


# In[11]:


mwct = WordCloud(background_color=None, 
                 mask=mask, mode='RGBA')
mwct.generate(data_processed)
plt.figure(figsize=(10, 10))
plt.imshow(mwct)
plt.axis('off')
plt.show()


# In[29]:


mwct.to_file("wordcloud_transparent_big.png")


# In[13]:


from PIL import Image
masks = np.array(Image.open("silhouette.png"))


# In[16]:


mwct = WordCloud(background_color='black', 
                 mask=masks, contour_color='grey', 
                 contour_width=2)
mwct.generate(data_processed)
plt.figure(figsize=(20, 10))
plt.imshow(mwct)
plt.axis('off')
plt.show()


# In[34]:


mwct.to_file("wordcloud_transparent2.png")

