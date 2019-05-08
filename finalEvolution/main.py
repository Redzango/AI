import creature
import random

#ask for itterations and anything else
itr=int(input("How many itterations?"))
creatures = []

f=open("sizeVSspeed.dat","w+")
b=open("cooperVShost.dat","w+")
c=open("speedVSend.dat","w+")

#create the population of creatures
for i in range(100):
    #creatures.append((creature.Creature(1,1,1,1,1,1),0))
    creatures.append((creature.Creature(random.randrange(5)+1,random.randrange(5)+1,random.randrange(5)+1,random.randrange(5)+1,random.randrange(5)+1),0))

#itterate to find max values for the Fittness Funtion
for i in range(itr):
    for j in range(len(creatures)):
        critter=creatures[j][0]
        creatures[j]=(critter,creature.scoreCreature(critter,creatures))
        f.write("%f %f\n" % (critter.getSize(), critter.getSpeed()))
        b.write("%f %f\n" % (critter.getCooperative(), critter.getHostile()))
        c.write("%f %f\n" % (critter.getSpeed(), critter.getEndurance()))
    f.write("\n")
    b.write("\n")
    c.write("\n")
    creatures = sorted(creatures, key=lambda tup: tup[1])
    creatures.reverse()
    creatures = creature.cullAndMutate(creatures)

f.close()
b.close()
c.close()

