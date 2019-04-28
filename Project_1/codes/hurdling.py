
###### do not change anything in this file! ######

import random, time, pickle
from sys import argv

size = 25
input_size = 12
chance_of_obstacles = 0.2
canvas = [[0]*size,[0]*size]
ball_position = 2
ball_in_air = -1
lose = False
ball_in_air_time = 2
JUMP = 1  # ball operation
RUN = 0   # ball operation
NOTHING = 0
BALL = 1
OBASTACLE = 2
FAIL = 3
MAGIC_NUM = 0.233

def initialize():
    global canvas, ball_in_air, lose
    canvas = [[0]*size,[0]*size]
    canvas[1][ball_position] = BALL
    ball_in_air = -1
    lose = False

def save_dna(file_name, dna):
    with open(file_name, "wb") as fp:   # Pickling
        pickle.dump(dna, fp)
    fp.close()

def load_dna(file_name):
    with open(file_name, "rb") as fp:   # Unpickling
        return pickle.load(fp)

def preprocess(canvas):
    p = 0
    for i in range(size):
        if canvas[1][size - i - 1] == OBASTACLE:
            p += 2**i
    return p

def draw(canvas):
    # draw the first line
    line = ""
    for i in range(size):
        c=canvas[0][i]
        if(c == BALL):
            line = line + "o"
        else:
            line = line + " "
    print(line)
    # draw the second line
    line = ""
    for i in range(size):
        c=canvas[1][i]
        if(c == BALL):
            line = line + "o"
        elif(c == OBASTACLE):
            line = line + "L"
        elif(c == FAIL):
            line = line + "X"
        else:
            line = line + " "
    print(line)
    line = ""
    for i in range(size):
        line += "-"
    print(line)
    print("  ")
        

def ball_change(canvas, action):
    global lose
    if(action == JUMP):
        canvas[0][ball_position] = BALL
        canvas[1][ball_position] = NOTHING
    else:
        canvas[0][ball_position] = NOTHING
        if(canvas[1][ball_position] == OBASTACLE):
            lose = True
            canvas[1][ball_position] = FAIL
        else:
            canvas[1][ball_position] = BALL

def ball_AI(canvas, dna):
    y = 0
    for i in range(input_size):
        y += dna[i]*canvas[1][i]
    if(y > MAGIC_NUM):
        return JUMP
    else:
        return RUN

def move_on(canvas):
    global lose
    global ball_in_air
    global chance_of_obstacles
    canvas[0] = canvas[0][1:size] + [NOTHING]
    canvas[1] = canvas[1][1:size] + [NOTHING]
    if(ball_in_air >= 0): 
        canvas[0][ball_position] = BALL
        canvas[0][ball_position - 1] = NOTHING
    else:
        if(canvas[1][ball_position] == OBASTACLE):
            lose = True
            canvas[1][ball_position] = FAIL
        else:
            canvas[1][ball_position] = BALL
        canvas[1][ball_position - 1] = NOTHING
    i = random.randint(0,100)
    if(i/100 < chance_of_obstacles):
        chance_of_obstacles = 0
        canvas[1][size - 1] = OBASTACLE
    else:
        chance_of_obstacles += 0.05



# T is the maximum iteration, 
# in_training is a bool value that says whether you don't want to print animation
def game_start(T, in_training, dna):    
    global ball_in_air
    global lose
    t=0
    while(t<T and not lose):
        t+=1
        move_on(canvas)
        if(ball_in_air > 0):
            ball_in_air -= 1
        elif(ball_in_air == 0):
            ball_in_air -= 1
            ball_change(canvas, RUN)
        else:
            action = ball_AI(canvas, dna)
            if(action == JUMP):
                ball_in_air = ball_in_air_time
                ball_change(canvas, JUMP)
        if(not in_training):
            draw(canvas)
            time.sleep(0.25)
    if(not in_training):
        if(lose):
            print("  YOU LOSE!!!")
        else:
            print("  ARRIVED!!!")
    return t
    

if __name__ == "__main__":
    initialize()
    dna_path = argv[1]
    dna = load_dna(dna_path)
    game_start(300, False, dna)

        
        

