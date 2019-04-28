
###### settings, do not change ########
import hurdling as hd
import random, math
SIZE = hd.input_size
cache=[0]*SIZE
MAXIMUM_T = 300
FITNESS_TRY = 8
MUTATION_RATE = 0.0  # variable declaration
MUTATION_RATIO = 0.0    # variable declaration

##### some core functions for evolutionary algorithms ####
####  do not change unless you have confidence to improve them ####

def initialize_population(number):
    P = []
    for i in range(number):
        dna = [0]*SIZE
        for i in range(SIZE):
            dna[i] = random.random()
        P.append((dna, fitness(dna)))
    P.sort(key = lambda x: x[1])
    return P

def mutate(dna):
    for (i, a) in enumerate(dna):
        r = random.random()
        if(r < MUTATION_RATE):
            dna[i] += MUTATION_RATIO * (random.random() - 0.5)

def fitness_pair():
    c = random.random()
    c = math.sin(c*math.pi/2)*SIZE
    return int(c)
    

def crossover(P):
    POPULATION_SIZE = len(P)
    dad = random.randint(0, POPULATION_SIZE-1)
    mom = random.randint(0, POPULATION_SIZE-1)
    #dad = fitness_pair()
    #mom = fitness_pair()
    dna_dad = P[dad][0]
    dna_mom = P[mom][0]
    cut = random.randint(0, SIZE - 1)
    dna_child = dna_mom.copy()
    dna_child[0:cut] = dna_dad[0:cut]
    return dna_child

def fitness(dna):
    f = []
    for i in range(FITNESS_TRY):
        hd.initialize()
        distance = hd.game_start(MAXIMUM_T, True, dna)
        f.append(distance)
    return sum(f)/FITNESS_TRY

def select(P, dna):
    l = len(P)
    f = fitness(dna)
    if(f <= P[0][1]):
        return
    for i in range(1, l):
        f_p = P[i][1]
        if(f <= f_p):
            P[i-1] = (dna, f)
            return
    P[l-1] = (dna, f)



########## your code below #############

POPULATION_SIZE = 0    # 你需要自己尝试不同的设置来选择最好的参数
GENERATION_NUM = 0   # 你需要自己尝试不同的设置来选择最好的参数
MUTATION_RATE = 0.0  # 你需要自己尝试不同的设置来选择最好的参数
MUTATION_RATIO = 0.0    # 你需要自己尝试不同的设置来选择最好的参数

# 你需要修改并补全这个函数
# 把最终最好的dna和其对应的fitness返回
def evolutionary_train():
    best_dna = [0]*SIZE
    best_fitness = 0        
    return (best_dna, best_fitness)


(dna, f) = evolutionary_train() # 训练
print("fitness is "+str(f))     # 你会看到目前最好的dna大概能走多少格，一百多格算比较好的结果
hd.save_dna("dna_file", dna)    # 这个dna会被存到当前文件夹下