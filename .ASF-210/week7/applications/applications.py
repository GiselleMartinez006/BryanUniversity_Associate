from matplotlib import pyplot as plt


# from random import seed



# seed(1)


states1= ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL"]
states2= ["IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT"]
states3= ["NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI"]
states4= ["SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]


half1 = [189149, 15155, 241165, 108640, 920212, 100185, 69127, 24392, 17074, 794624, 355025, 4549, 14834]
half2 = [61785, 393797, 172730, 121994, 79333, 101494, 181443, 6466, 143387, 154218, 185934, 142311,118587]
half3 = [177319, 29966, 66545, 97479, 10641, 232997, 43826, 500677, 269021, 39907, 92, 205347, 119152]
half4 = [43228, 152, 207618, 64798, 32312, 173491, 42253, 254220, 911874, 1353, 108803 ]


print(len(half1), len(states1))
print(len(half2), len(states2))
print(len(half3), len(states3))
print(len(half4), len(states4))
plt.bar(states1,half1)
plt.show()
plt.bar(states2,half2)
plt.show()
plt.bar(states3,half3)
plt.show()
plt.bar(states4,half4)

plt.show()

