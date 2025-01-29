import math
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

DISTANCE_BETWEEN_BUOYS = 2
PREDOCKING_DISTANCE_TO_RED_BUOY = 0.5
TRAJECTORY_POINTS = 50

b_green=[]
b_red=[]

def make_pair():
    if (len(b_green) != 1) or (len(b_red) != 1):
        print("Wrong number of buoys!")
        return []
    # Paarbauda, vai distance starp bojaam tiesham ir 2 metri, kaa tas ir aprakstiits noteikumos
    distance = round(math.sqrt((b_red[0][0]-b_green[0][0])**2+(b_red[0][1]-b_green[0][1])**2), 0)
    if distance != DISTANCE_BETWEEN_BUOYS:
        print("Distance between buoys is not", DISTANCE_BETWEEN_BUOYS)
        print("Actual distance:",distance)
        return []
    pair = [b_green[0], b_red[0]]

    return pair

def reach_position(pair):
    # Merkya defineeshana
    docked_x = (pair[1][0]-pair[0][0])/2+pair[0][0]
    docked_y = (pair[1][1]-pair[0][1])/2+pair[0][1]
    prepath = []
    prepath.append([docked_x, docked_y])
    # Starta defineeshana
    starting_point = input("Starting point <x:y>: ")
    start_x = float(starting_point.split(":")[0])
    start_y = float(starting_point.split(":")[1])
    path = []
    path.append([start_x, start_y])
    
    # Atrast pirmspedeejo punktu (perpendikulars sarkanai bojai ar disatnci <PREDOCKING_DISTANCE_TO_RED_BUOY>)
    vx, vy = pair[1][0]-pair[0][0], pair[1][1]-pair[0][1]
    p_x1, p_y1 = -vy, vx
    p_x2, p_y2 = vy, -vx 

    norm = math.sqrt(p_x1**2 + p_y1**2)
    p_x1, p_y1 = (p_x1/norm)*PREDOCKING_DISTANCE_TO_RED_BUOY, (p_y1/norm)*PREDOCKING_DISTANCE_TO_RED_BUOY
    p_x2, p_y2 = (p_x2/norm)*PREDOCKING_DISTANCE_TO_RED_BUOY, (p_y2/norm)*PREDOCKING_DISTANCE_TO_RED_BUOY

    predock_x1, predock_y1 = pair[1][0] + p_x1, pair[1][1] + p_y1
    predock_x2, predock_y2 = pair[1][0] + p_x2, pair[1][1] + p_y2

    # Atrast tuvaako starta punktam

    distance1 = math.sqrt((start_x-predock_x1)**2+(start_y-predock_y1)**2)
    distance2 = math.sqrt((start_x-predock_x2)**2+(start_y-predock_y2)**2)
    if distance1 < distance2:
        predock_x, predock_y = predock_x1, predock_y1
    else:
        predock_x, predock_y = predock_x2, predock_y2
    
    path.append([predock_x, predock_y])
    path.append(prepath[0])

    return path

def smooth_path(path):
    x = np.array([path[0][0], path[1][0], path[2][0]])
    y = np.array([path[0][1], path[1][1], path[2][1]])

    cs = CubicSpline(x, y, bc_type='natural')

    x_smooth = np.linspace(min(x), max(x), TRAJECTORY_POINTS)
    #y_smooth = cs(x_smooth)

    s_path = []

    for i in x_smooth:
        s_path.append([i, cs(i)])
    return s_path

def show(pair, path, s_path):
    plt.scatter(pair[0][0], pair[0][1], color=pair[0][2])
    plt.scatter(pair[1][0], pair[1][1], color=pair[1][2])
    plt.plot([pair[0][0],pair[1][0]],[pair[0][1],pair[1][1]],linestyle='-', linewidth=1)
    x=[]
    y=[]
    for p in path:
        x.append(p[0])
        y.append(p[1])
    
    s_x = [point[0] for point in s_path]
    s_y = [point[1] for point in s_path]
    plt.plot(s_x, s_y, '--', color='orange', linewidth=2, label="Path")
    plt.plot(x,y,linestyle='-', linewidth=2)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.show()


def main(obstacles):
    for obstacle in obstacles:
        color = obstacle[2]
        match color:
            case "green":
                b_green.append(obstacle.copy())
            case "red":
                b_red.append(obstacle.copy())
    pair = make_pair()
    prepath = reach_position(pair)
    path = smooth_path(prepath)
    show(pair, prepath, path)
