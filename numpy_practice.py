'''import numpy as np 
l= [10,20,30,40,50]
a=np.array(l)
print(a)'''

'''import numpy as np 
l=[10,20.20,10,10,10]
a =np.array(l)
print(a)
type(a)
'''

'''import numpy as np 
l=[10,'g', 20 ,30,40,50]
a=np.array(l)
print(a)'''

'''
import numpy as np 
l=[[10,20,30],[50,35,22],[60,44,67]]
a=np.array(l)
print(a)'''

'''import numpy as np 
a = np.arange(1,8)
print(a)'''


'''import numpy as np 
l=np.arange(10,22).reshape(3,4)
print(l)'''


'''import numpy as np 
l=np.zeros((2,2))
print(l)'''

''''import numpy as np 
l=[[60,20,30],[20,22,11]]
a=np.array(l)

x=a.ndim
y=a.shape
w=a.dtype
z=a.itemsize
print(x)
print(y)
print(w)
print(z)'''




#indexing and slciing 



'''import numpy as np 
l=[10,20,30,40,50]
a=np.array(l)
print(a[1])
print(a[-1])
print(a[-2])
print(a[-4])'''

'''import numpy as np 
l=[10,20,30,40,50,60,70]
a=np.array(l)
print(a[1:5])
print(a[1:5:2])
print(a[1:3])'''


import numpy as np 
l=[10,20,33,49,54,22,122,65,77,10,40,60,60]
a=np.array(l)
print(a[0:6:1])
print(a[3:6:3])
print(a[3:6:2])