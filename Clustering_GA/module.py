import random

class Student:
    '''
        Represents a point in m-dimension
    '''
    
    def __init__(self,_marks):
        self.marks = list(_marks)
        self.avg = 1.0*sum(_marks)/len(_marks)
        self.group = -1

    def getDistance(self, node):
        assert type(node) == Student, "Class type doesn't match"
        assert len(self.marks) == len(node.marks), "Subject count doesn't match"
        
        m = len(self.marks)
        dis = 0
        for i in range(m):
            dis += (self.marks[i] - node.marks[i])**2
        return dis

    def getDistanceByAvg(self, node):
        assert type(node) == Student, "Class type doesn't match"

        return (self.avg - node.avg)**2


class Leaders:
    
    def __init__(self):
        self.rep = tuple()
        self.fitness = -1

    def offspring(self, par2):

        child = Leaders()
        for i in range(len(par2.rep)):
            prob = random.random()

            if prob < 0.45:
                    child.rep += (self.rep[i],)
            elif prob < 0.90:
                    child.rep += (par2.rep[i],)
            else:
                    child.rep += (Leaders.mutation(),)

        return child	# Fitness value not calculated yet!

    @staticmethod
    def mutation():
        seed = 100*random.random()
        delta = 0.01 * random.randint(0,1)
        return min(100.0,seed+delta)


    def electRep(self,points,k):
        n = len(points)
        representative = []
        for i in range(k):
            genesisNode = points[random.randint(0,n-1)]
            representative.append(genesisNode.avg)
        
        self.rep = tuple(representative)
        self.calcFitness(points)

    def calcFitness(self,points):
        fitness = 0
        
        for point in points:
            minDistance = -1
            for rep in self.rep:
                dis = (rep - point.avg)**2
                if minDistance == -1 or dis < minDistance:
                    minDistance = dis
            fitness += minDistance
            
        self.fitness = fitness
        return fitness
