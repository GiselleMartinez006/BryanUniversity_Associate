# In the tuple.py file, write a program according to following specifications
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']

print(friends_list)
# From the above fill a list(friend_list) properly with the names of all the friends. One per “slot”
# You may need to enter same command several times
# Use print() statements to work your way through the exercise.


friends_list= []
for x in csv.split(","): 
    for y in [*x]:   
        if y is ':' :
            x = x.split(':')
            for m in x :
                for z in [*m]: 
                    if z is ';' :
                        x.pop()
                        for n in m.split(";"):
                            x.append(n)
    if type(x) == list: 
        print(x, "33 list") 
        for w in x: 
            friends_list.append(w)
    else:
        friends_list.append(x)
    print(friends_list) 

