import math
from matplotlib import pyplot as plt

b_green=[]
b_red=[]
b_yellow=[]

def make_pairs():
    pair=[]
    if len(b_green)!=len(b_red):
        print("Wrong number of buoys")
        return []
    for r_buoy in b_red:
        length=0
        for g_buoy in b_green:
            rg_length=math.sqrt((r_buoy[0]-g_buoy[0])**2+(r_buoy[1]-g_buoy[1])**2)
            if length==0 and rg_length<=3:
                pair.append([r_buoy.copy(),g_buoy.copy()])
                length=rg_length
            elif length!=0 and length>rg_length:
                pair[len(pair)-1]=[r_buoy.copy(),g_buoy.copy()]
                length=rg_length
    return pair
def show_pairs(pair, path):
    for p in pair:
        plt.scatter(p[0][0], p[0][1], color=p[0][2])
        plt.scatter(p[1][0], p[1][1], color=p[1][2])
        plt.plot([p[0][0],p[1][0]],[p[0][1],p[1][1]],linestyle='-', linewidth=1)
        x=[]
        y=[]
        for p in path:
            x.append(p[0])
            y.append(p[1])
        plt.plot(x,y,linestyle='-', linewidth=2)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def create_path(pair):
    path=[]
    for p in pair:
        x = (p[0][0] - p[1][0])/2 + p[1][0]
        y = (p[0][1] - p[1][1])/2 + p[1][1]
        path.append([x,y])
    starting_point=input("Starting point (x:y):")
    start_x=float(starting_point.split(":")[0])
    start_y=float(starting_point.split(":")[1])
    final_path=[[start_x,start_y]]
    while len(path)>0:
        i=0
        for p in path:
            length=[]
            print()
            length.append(math.sqrt((final_path[len(final_path)-1][0]-p[0])**2+(final_path[len(final_path)-1][1]-p[1])**2))
        final_path.append(path[length.index(min(length))])
        path.pop(length.index(min(length)))
    return final_path
        

def main(obstacles):
    for obstacle in obstacles:
        color = obstacle[2]
        match color:
            case "green":
                b_green.append(obstacle.copy())
            case "red":
                b_red.append(obstacle.copy())
            case "yellow":
                b_yellow.append(obstacle.copy())
    
    b_pairs=make_pairs()
    path = create_path(b_pairs)
    print(path)
    show_pairs(b_pairs, path)
