
# coding: utf-8

# In[275]:


k = [ 0x428a2f98 ,0x71374491 ,0xb5c0fbcf ,0xe9b5dba5 ,0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 
0xd807aa98 ,0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7 ,0xc19bf174, 
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa ,0x5cb0a9dc ,0x76f988da, 
0x983e5152 ,0xa831c66d ,0xb00327c8 ,0xbf597fc7, 0xc6e00bf3 ,0xd5a79147, 0x06ca6351 ,0x14292967, 
0x27b70a85 ,0x2e1b2138 ,0x4d2c6dfc ,0x53380d13 ,0x650a7354 ,0x766a0abb ,0x81c2c92e ,0x92722c85 ,
0xa2bfe8a1 ,0xa81a664b, 0xc24b8b70 ,0xc76c51a3 ,0xd192e819 ,0xd6990624 ,0xf40e3585 ,0x106aa070 ,
0x19a4c116 ,0x1e376c08 ,0x2748774c ,0x34b0bcb5 ,0x391c0cb3 ,0x4ed8aa4a ,0x5b9cca4f ,0x682e6ff3 ,
0x748f82ee ,0x78a5636f ,0x84c87814 ,0x8cc70208 ,0x90befffa ,0xa4506ceb ,0xbef9a3f7, 0xc67178f2 ]


# In[276]:


h_01 = 0x6a09e667


# In[277]:


h_02 = 0xbb67ae85


# In[278]:


h_03 = 0x3c6ef372


# In[279]:


h_04 = 0xa54ff53a


# In[280]:


h_05 = 0x510e527f


# In[281]:


h_06 = 0x9b05688c


# In[282]:


h_07 = 0x1f83d9ab


# In[283]:


h_08 = 0x5be0cd19


# In[284]:


mes = ''.join(['0'+str(bin(ord(i)))[2:] for i in input('Enter your message: ')])


# In[285]:


pad_mes = mes + '1'


# In[286]:


zero = 448 - (len(mes)+1)


# In[287]:


for i in range (zero):
    pad_mes = pad_mes + '0'


# In[288]:


length = bin(len(mes))


# In[289]:


pad_mes


# In[290]:


for i in range (64-len((length[2:]))):
    pad_mes += '0'


# In[291]:


pad_mes += length[2:]


# In[292]:


pad_mes 


# In[293]:


m =[]


# In[294]:


for i in range (16):
    m.append(pad_mes[(32*i):(32*(i+1))])


# In[295]:


for i in range(len(m)):
    m[i] = int(m[i],2)


# In[296]:


m


# In[297]:


def Ch (x,y,z):  #input x,y,z must be decimal form
    return ((x&y)^((~x)&z))


# In[298]:


def Maj (x,y,z):
    return ((x&y)^(x&z)^(y&z))


# In[299]:


def S(num, time):
    store = str(bin(num))[2:]
    for i in range (32-len(store)):
        store = '0'+store
    front = store[:len(store)-time]
    back = store[len(store)-time:]
    result = back + front
    return (int(result,2))


# In[300]:


def SIG_0 (x):
    return ((S(x,2)^S(x,13)^S(x,22)))


# In[301]:


def SIG_1(x):
    return(S(x,6)^S(x,11)^S(x,25))


# In[302]:


def sig_0(x):
    return(S(x,7)^S(x,18)^(int(x)>>3))


# In[303]:


def sig_1(x):
    return (S(x,17)^S(x,19)^(x>>10))


# In[304]:


w = []
w[:64]=[0]*64


# In[311]:


h = [h_01,h_02,h_03,h_04,h_05,h_06,h_07,h_08]
a = h[0]
b = h[1]
c = h[2]
d = h[3]
e = h[4]
f = h[5]
g = h[6]
H = h[7]
print(hex(a))
for i in range (64):
    if (i<=15):
        w[i]=m[i]
        t1 = (H + SIG_1(e)+Ch(e,f,g)+k[i]+w[i])%(2**32)
        t2 = (SIG_0(a)+Maj(a,b,c))%(2**32)
        H = g
        g = f
        f = e
        e = (d+t1)%(2**32)
        d = c
        c = b
        b = a
        a = (t1+t2)%(2**32)
    else:
        w[i]=(sig_1(w[i-2])+w[i-7]+sig_0(w[i-15])+w[i-16])%(2**32)
        t1 = (H + SIG_1(e)+Ch(e,f,g)+k[i]+w[i])%(2**32)
        t2 = (SIG_0(a)+Maj(a,b,c))%(2**32)
        H = g
        g = f
        f = e
        e = (d+t1)%(2**32)
        d = c
        c = b
        b = a
        a = (t1+t2)%(2**32)    
    print(hex(a),hex(b),i)
h = [(a+h[0])%(2**32),(b + h[1])%(2**32), (c + h[2])%(2**32),(d + h[3])%(2**32), (e + h[4])%(2**32),(f + h[5])%(2**32),(g + h[6])%(2**32),(H + h[7])%(2**32)]


# In[306]:


z=[]
z[:len(h)] = [0]*len(h)
for i in range(len(h)):
    z[i]=hex(h[i])


# In[307]:


z

