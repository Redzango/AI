import random
#the class that defines a creature and its variables
class Creature:
    def __init__(self,speed,size,endurance,cooperative,hostile):
        self.speed=speed
        self.size=size
        self.endurance=endurance
        self.cooperative=cooperative
        self.hostile=hostile
    def getSpeed(self):
        return self.speed
    def getSize(self):
        return self.size
    def getEndurance(self):
        return self.endurance
    def getCooperative(self):
        return self.cooperative
    def getHostile(self):
        return self.hostile


#scores a creature on its atributes depending on mapsize, #of other creatures, food available
def scoreCreature(Creature,creatures):
    speed=Creature.getSpeed()
    size=Creature.getSize()
    endurance=Creature.getEndurance()
    cooperative=Creature.getCooperative()
    hostile=Creature.getHostile()
    #hAvg=0
    #diff=0
    #for critter,scor in creatures:
    #    cAvg+=critter.getCooperative()
    #    hAvg+=critter.getHostile()
    #cAvg=cAvg/100
    #hAvg=hAvg/100i
    #if(cooperative>cAvg and hostile>hAvg): diff=0
    #elif(hostile>hAvg): diff=hostile
    #elif(cooperative>cAvg): diff=cooperative

    score=speed*2+size*2-size*2*speed*2/endurance-cooperative*hostile+2*cooperative
    
    return score

#randomly raises or lowers the attributes of a creature
def mutate(critter):
        speed=critter.getSpeed()*(random.random()+0.5)
        size=critter.getSize()*(random.random()+0.5)
        endurance=critter.getEndurance()*(random.random()+0.5)
        cooperative=critter.getCooperative()*(random.random()+0.5)
        hostile=critter.getHostile()*(random.random()+0.5)

        return Creature(speed,size,endurance,cooperative,hostile)

#Crossing over - averages then slightly changes the values of two parent creatures
def breed(c1,c2):
        speed=(c1.getSpeed()+c2.getSpeed())*(random.uniform(0.9,1.1))/2.0
        size=(c1.getSize()+c2.getSize())*(random.uniform(0.9,1.1))/2.0
        endurance=(c1.getEndurance()+c2.getEndurance())*(random.uniform(0.9,1.1))/2.0
        cooperative=(c1.getCooperative()+c2.getCooperative())*(random.uniform(0.9,1.1))/2.0
        hostile=(c1.getHostile()+c2.getHostile())*(random.uniform(0.9,1.1))/2.0
        return Creature(speed,size,endurance,cooperative,hostile)
    

#revome the bad, keep the ok, and breed the strong
def cullAndMutate(creatures):
    changed = []
    for i in range(100):
        critter,scor=creatures[i]
        if (i<20):
            oC = creatures[random.randrange(20)][0]
            changed.append((critter,0))
            if(random.random()>0.8): 
                changed.append((mutate(breed(critter,oC)),0))
            else:
                changed.append((breed(critter,oC),0))
        elif (i<80):
            changed.append((critter,0))
    return changed





