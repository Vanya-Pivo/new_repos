#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Введите слово')
text = input()
print('Введите параметр сдвига')
key = int(input())
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
zcaesar = ''
for x in text.upper():
    if x in alfabet:
        zcaesar += alfabet[(alfabet.find(x) + key) % len(alfabet)]
print(zcaesar)


# In[ ]:




