#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.chat.util import Chat,reflections


# In[ ]:


Pairs = [['Hi, my name is (.*)',['Hey','Hi bestiee!!']],
         ['(.*)made you?',['I created myself']],
         ['(.*)your name?',['Hey','Hi bestiee!!']]]


# In[ ]:


chat = Chat(Pairs,reflections)


# In[ ]:


chat.converse()


# In[ ]:




