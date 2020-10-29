# =============================================================================
# from matplotlib import pyplot as plt
# 
# 
# from random import seed
# from random import randint
# 
# 
# seed(1)
# 
# x = ["red", "green", "blue"]
# 
# y = [randint(0, 100),randint(0, 100),randint(0, 100) ]
# 
# plt.bar(x,y)
# 
# plt.show()
# 
# 
# 
# from numpy import sin
# 
# x= [x*0.1 for x in range(100)]
# 
# y = sin(x)
# 
# plt.plot(x,y)
# plt.show()
# =============================================================================

from mpmath import mp

mp.dps= (int(input("Let's play a pi game! Tell me a number and i'll give you pi to that decimal! "))+1)

print(mp.pi)