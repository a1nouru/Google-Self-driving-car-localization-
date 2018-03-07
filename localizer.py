# Contributed by Nouru Muneza
#resulting probability distribution.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green'] #simple possible positions in the world. 
measurements = ['red', 'green']
pHit = 0.6 #probability of location being meet
pMiss = 0.2 #probability of location missed
pExact = 0.8 ##probability of exact location 
pOvershoot = 0.1 #Undershooting probability of a certain location. 
pUndershoot = 0.1 #Overshooting probability of a certain location. 

def sense(p, Z): #sensing the location of the robocar
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U): #Moving certain steps 
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)] #calculating the next 1 step position in list
        s = s + pOvershoot * p[(i-U-1) % len(p)] #calculating next probability of overShoot as robocar moves
        s = s + pUndershoot * p[(i-U+1) % len(p)] #calculating next probability of underShoot as robocar moves
        q.append(s)
    return q

for i in range(1000): # Locatization probability of a robocar moving 1000 times. 
    p = move(p,1)

print p
