import random
from module import Student, Leaders


def output(students, center):
        sid = 1
        for student in students:
            idx = 0
            dif = abs(student.avg - center.rep[0])
            for i in range(1,len(center.rep)):
                val = abs(student.avg - center.rep[i])
                if val < dif:
                    dif = val
                    idx = i

            print('Student %d belongs to group-%d'%(sid,idx+1))
            sid += 1

def getInput():
    n = int(input('Number of students : '))
    m= int(input('Number of subjects : '))
    k = int(input('Number of groups : '))      # Assuming k <= n
    assert n>0 and m>0 and k>0, 'Invalid Input'

    myClass = []
    
    for i in range(n):
        print('Marks obtained by student %d : '%(i+1))
        arr = list(map(int, input().split()))
        assert len(arr) == m,'Subject count not valid'
        assert min(arr)>=0 and max(arr) <=100, 'Marks range not valid'

        stud = Student(arr)
        myClass.append(stud)

    return (n,m,k,myClass)

def main():
    '''
            Gene :- Mean (Initially)
            Chromosome :- k-group (collection of genes)
            Population :- collection of Chromosomes
    '''

    POP_SIZE = 100
    MAX_GENX = 100
    n,m,k,students = getInput()
    population = []

    for x in range(POP_SIZE):
        individual = Leaders()
        individual.electRep(students,k)
        population.append(individual)

    genx = 1
    flag = 1
    while flag and genx <= MAX_GENX:
        population.sort(key = lambda x:x.fitness)
        if population[0].fitness == 0:
            flag = 0
            break

        carryAhead = int(0.1*POP_SIZE)
        future = population[:carryAhead]
        rem = POP_SIZE - carryAhead

        for i in range(rem):
            par1 = random.randint(0, 50)
            par2 = random.randint(0, 67)
            child = population[par1].offspring(population[par2])
            child.calcFitness(students)
            future.append(child)

        population = future
        genx+=1

    # Select parents
    # Do crossover
    # Do mutation
    # Repeat

    output(students,population[0])

main()