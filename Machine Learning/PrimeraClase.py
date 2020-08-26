#JOHN EDWARD OSPINA LADINO
#1010113894

import numpy as np
data = np.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10], '\n')


print(data.shape)


x = data[:,0]
y = data[:,1]


print(x, '\n')
print(y, '\n')


print(x.ndim, '\n')
print(y.ndim, '\n')

print(x.shape, '\n')
print(y.shape)

print(np.sum(np.isnan(y)))


print(x.shape,'\n')
print(y.shape,'\n')


x=x[~np.isnan(y)]
y=y[~np.isnan(y)]


print(x.shape,'\n')
print(x.shape,'\n')