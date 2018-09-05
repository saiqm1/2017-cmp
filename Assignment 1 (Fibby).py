
# coding: utf-8

# In[5]:



def fibby(n):

  if n == 0:
        return 0
  elif n == 1:
        return 1
  else:
        return fibby(n-1) + fibby(n-2)


z=[fibby(n) for n in range(int(input("type a value for x: ")), int(input("type a value for y: ")))]
print (z, 'Muzamil Saiq')

