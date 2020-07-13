''' Lets try to model an optical frequency comb '''
import matplotlib.pyplot as plt
import numpy as np

# # # Modelling 
f0 = 1e15
fr = 1e7
X = np.linspace(0,10/fr,1000)
#y = np.linspace(90,-10,1000)



def Sin(x, Freq):
    return np.sin(Freq*x)

y_O = []
for i in range(5):
    yo = Sin(X, (i+1)*fr+f0)
    y_O.append(yo)
##print('y_O',y_O)
y_M = []
for i in range(5):
    ym = Sin(X, (i+1)*fr)
    y_M.append(ym)

##print('y_M',y_M)
# # # Plotting
fig = plt.figure()
axo1 = plt.subplot2grid((7,2), (0,0), rowspan=1)
axo2 = plt.subplot2grid((7,2), (1,0), rowspan=1,sharex=axo1)
axo3 = plt.subplot2grid((7,2), (2,0), rowspan=1,sharex=axo1)
axo4 = plt.subplot2grid((7,2), (3,0), rowspan=1,sharex=axo1)
axo5 = plt.subplot2grid((7,2), (4,0), rowspan=1,sharex=axo1)
axO = plt.subplot2grid((7,2), (5,0), rowspan=2)

axm1 = plt.subplot2grid((7,2), (0,1), rowspan=1)
axm2 = plt.subplot2grid((7,2), (1,1), rowspan=1,sharex=axm1)
axm3 = plt.subplot2grid((7,2), (2,1), rowspan=1,sharex=axm1)
axm4 = plt.subplot2grid((7,2), (3,1), rowspan=1,sharex=axm1)
axm5 = plt.subplot2grid((7,2), (4,1), rowspan=1,sharex=axm1)
axM = plt.subplot2grid((7,2), (5,1), rowspan=2)

AXO = [axo1,axo2,axo3,axo4,axo5]
AXM = [axm1,axm2,axm3,axm4,axm5]

col = ['blue','green','yellow','red','brown']
for i in range(5):
    AXO[i].plot(X,y_O[i], color=col[i])
    AXM[i].plot(X,y_M[i])

## sum up the [i]s first

Oarray,Marray = np.array(y_O), np.array(y_M)

##print(Oarray)
Osum = np.sum(Oarray,0)
Msum = np.sum(Marray,0)
##print('sum',Osum)

axO.plot(X, Osum,color='k')
axM.plot(X, Msum,color='k')
plt.show()