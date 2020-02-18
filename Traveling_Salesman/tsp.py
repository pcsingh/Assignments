import random
""" Travelling Salesman Problem"""

class TSP(object):

    def getDistance(self,P1,P2): 
        """
            Generates distance between 2 points
        """
        self.P1 = P1
        self.P2 = P2
        distance = ((self.P1[0]-self.P2[0])**2 + (self.P1[1]-self.P2[1])**2)**(1/2)
        return distance

    def generateCoordinates(self):
        """
            This function generates random coordinates for cities

        Returns
        -------
        list
            Returns x and y coordinates in the list.

        """
        x = random.randint(0,101)
        y = random.randint(0,101)
        return [x,y]

    def calculateDist(self,s,n): 
        """
            Calculates the total distance in a state, eg [0,1,2,3]
        """
        self.calD = s
        self.nu = n
        dist = 0
        total = 0
        for i in range(self.nu):
            xi = self.calD[i]
            yj = self.calD[i+1]
            dist = self.getDistance(self.coord[xi],self.coord[yj])
            total+=dist    
        return total

    def hue(self,chosenList,cityList): 
        """
            Generates the total heuristic plus path cost and sends it out
        """
        toCheck = cityList[:]
        SPL = chosenList[:]
        dl = 999999999
        fCost =[]
        l=[]
            
        for i in chosenList:
                toCheck.remove(i)
            
        for e in toCheck:
            l.clear()
            l.append(e)
            rest = cityList[:]
            totalDist = 0
            
            while len(rest) > 0:
                dl=99999
                for i in l:
                    if i in rest:
                        rest.remove(i)
                
                for n in l:
                    for m in rest:
                        d = self.getDistance(self.coord[n],self.coord[m])
                        if d<dl:
                            dl = d
                            c = m
                
                if c not in l:
                    l.append(c)
                    
                totalDist += d
            
            g = self.getDistance(self.coord[e],self.coord[SPL[-1]])
            k = self.getDistance(self.coord['0'],self.coord[e])
            f = g+totalDist+k
            
            fCost.append((f,e))
            
        fCost.sort()
        
        return (fCost[0][1])

    def solver(self):
        """
            Main function that solves the TSP and output

        Returns
        -------
        None.

        """
        
        cities = int(input("How many cities do you want to generate: "))
        
        self.coord ={}
        cityList = []
        chosenList = ['0']
        self.cities = cities
        
        for i in range(self.cities):
            a = str(i)
            l = self.generateCoordinates()
            self.coord[a] = l
            cityList.append(a)
        
        # currentState = cityList[:]
                
        for i in range(len(cityList)-1):        
            x = self.hue(chosenList,cityList)
            chosenList.append(x)
        
    
        final = chosenList+['0']
        il = cityList +['0']
        
        fd = self.calculateDist(final,len(final)-1)
        id = self.calculateDist(il,len(il)-1)
        
        print("\nCoordinates:")
        for each in self.coord.items():
            print('City {} has coordinate {}'.format(each[0], each[1]))
        
        print("\nInitial state to travel: ",il,"\n")
        print("Initial distance was %.2f km. \n" %id)
        print("Final state (optimized) to travel: ",final,"\n" )
        print("Optimized distance is %.2f km. \n" %fd)

def main():
    tsp = TSP() 
    tsp.solver()

if __name__ == "__main__":
    main()