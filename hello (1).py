#!/usr/bin/env python
# coding: utf-8

# # Donate Anonymously
# ### Description:
# #### You can donate anonoymously even admin team won't know who donate.  Do not write "donation" in notes.
# #### Kpay : xxxxx
# #### Wave : xxxxxx
# #### CBpay : xxxx xxxx xxxx

# In[ ]:


Amount = int (input ("Amount: "))
print (Amount)
if Amount >= 500:
    print ("Our service is available.")
else:
    print ("Our service is not available.")


# ##### You can donate any amount.
# ##### Our service starts from at least from 500mmk.
# ##### Our service >> song or letter 
# ##### Write "song" "letter" in all small alphabets.

# In[1]:


X = input ("song or letter: ")
print (X)
if X == "song":
   Y = input ("Singer: ")
   print (Y)
   Z = input ("Song: ")
   print (Z)
elif X == "letter":
   L = input ("You can write the letter here: ")
   print (L)
else:
      print ("please check either your alphbets are small or spelling mistake.")


# In[ ]:


I = input ("Any suggestion to 'Donate Anonymously'? : ")
print (I)


# In[ ]:




