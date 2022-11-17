#Genetic Algorithm implementing fitness function from fuzzy logic to generate an initial population of Matrices M

from typing import List, Callable, Tuple
from random import choices,randint,randrange,random
from collections import namedtuple
import numpy as np

Genome = List[List[float]]  #A solution
fuzzy_cap = List[float]    #Fuzzy vector
stock_data = namedtuple('stock_data',['open','close','high','low']) #Training data from stock market
Population = List[Genome] #Generation
GenomeGenFunc = Callable[[],Genome]     #A function to generate a genome randomly
FitnessFunc = Callable[[Genome],int]    #A fitness function
PopulateFunc = Callable[[],Population]  #A populate Function
SelectionFunc = Callable[[Population,FitnessFunc],Tuple[Genome,Genome]]
CrossoverFunc = Callable[[Genome,Genome],Tuple[Genome,Genome]]
MutationFunc = Callable[[Genome],Genome]

#Generating a genome -> One Matrix solution
def generate_Genome(rows:int,length:int)->Genome:
    M = []
    for i in range(rows):
        M.append([np.random.rand() for i in range(length)])
    return M

#Generating a population of genomes
def populate(pop_size:int,rows:int,genome_length:int)->List[Genome]:
    return [generate_Genome(rows,genome_length) for i in range(pop_size)]

#Generate the fuzzy row of features A
def generate_fuzzy(stock_data:stock_data,curr_time:int)->fuzzy_cap:
    #Generating Fuzzy Value Vector
    A = []

    #NR4 Membership Function
    c = 0
    for i in range(curr_time-3,curr_time):
        range_prev = stock_data[i].high-stock_data[i].low
        range_curr = stock_data[8].high-stock_data[8].low
        if(range_prev>range_curr):
            c+=1
    A.append(c/3)

    #NR6 Membership Function
    c = 0
    for i in range(curr_time-5,curr_time):
        range_prev = stock_data[i].high-stock_data[i].low
        range_curr = stock_data[8].high-stock_data[8].low
        if(range_prev>range_curr):
            c+=1
    A.append(c/5)

    #NR7 Membership Function
    c = 0
    for i in range(curr_time-6,curr_time):
        range_prev = stock_data[i].high-stock_data[i].low
        range_curr = stock_data[8].high-stock_data[8].low
        if(range_prev>range_curr):
            c+=1
    A.append(c/6)

    #DOJI Membership Function
    x = abs((stock_data[curr_time].close-stock_data[curr_time].open)/(stock_data[curr_time].high-stock_data[curr_time].low))
    rho = 0.25
    doji = 1-x/rho if x<=rho else 0
    A.append(doji)

    #Up-Hook Day Membership Function
    delta = 0.5
    x = stock_data[curr_time].high-delta-stock_data[curr_time+1].open
    meu = 0 if x<-0.5 else 2*(x+0.5) if x>=-0.5 and x<0 else 1
    A.append(meu)

    return A

#Fitness function defined from fuzzy logic
def fitness(genome:Genome,data:stock_data)->int:
    A = generate_fuzzy(data,8)
    M = 20
    b = []
    for j in range(len(genome[0])):
        bj = []
        for i in range(len(genome)):
            bj.append(min(A[i],genome[i][j]))
        b.append(max(bj))

    num = 0
    den = 0

    lambda_cap = [i/4 for i in range(1,5)]
    for j in range(len(genome[0])):
        num+=b[j]*lambda_cap[j]
        den+=lambda_cap[j]
    U = (num/den-0.5)*M/(1-0.5)*data[8].close

    diff = 0
    diff+=data[8].close+U-data[9].close #Difference between predicted close price and actual close price
    
    return 1/diff

#Selection Pair of elite individuals to crossover
def selection_pair(population:Population,fitnessFunc:FitnessFunc)->Tuple[Genome,Genome]:
    return choices(
        population,
        weights = [fitnessFunc(genome) for genome in population],
        k = 2
    )

#Crossover function
def crossover(a: Genome, b: Genome)->Tuple[Genome,Genome]:
    # if(len(a)!=len(b)):
    #     raise ValueError("Genome a and b must be of the same length")

    # length = len(a)
    # if(length<2):
    #     return a,b

    for i in range(len(a)):
        length = len(a[0])
        x = randint(1,length-1)
        a[i],b[i] = a[i][0:x]+b[i][x:],b[i][0:x]+a[i][x:]

    return a,b

#Mutation function
def mutation(genome:Genome,num:int = 1)->Genome:
    for _ in range(num):
        for i in range(len(genome)):
            index = np.random.randint(1,len(genome[0]))
            genome[i][index] = random()

    return genome

#Running final evolution to generate elite solutions
def run_evolution(
    populate_func:PopulateFunc,
    fitness_func:FitnessFunc,
    fitness_limit:int,
    selection_func:SelectionFunc = selection_pair,
    crossover_func:CrossoverFunc = crossover,
    mutation_func:MutationFunc = mutation,
    generation_limit:int = 100
)->Tuple[Population,int]:

    population = populate_func()

    for i in range(generation_limit) :
        population = sorted(
            population,
            key=lambda genome: fitness_func(genome) ,
            reverse = True
        )

        if(fitness_func(population[0])>=fitness_limit):
            break

        next_generation = population[0:2]   #elitism

        for j in range(int(len(population)/2)):
            parents = selection_func(population,fitness_func)
            offspring_a,offspring_b = crossover_func(parents[0],parents[1])
            offspring_a = mutation(offspring_a)
            offspring_b = mutation(offspring_b)
            next_generation+=[offspring_a,offspring_b]

        population = next_generation

    population = sorted(
        population,
        key=lambda genome: fitness_func(genome) ,
        reverse = True
    )

    return population,i
