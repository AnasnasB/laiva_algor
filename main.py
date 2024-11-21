from algorithms import collision_avoidance
from algorithms import obstacle_channel
from algorithms import speed_gate
from algorithms import visual_docking
from matplotlib import pyplot as plt
obstacles=[]

def add_obstacle(x,y,color):
    if color in ["red","green","yellow"]:
        obstacles.append([x,y,color])
        print ("Added obstacle at",x,y,color)
    else:
        print("Wrong color")

def show_obstacles():
    for i in obstacles:
        plt.scatter(i[0], i[1], color=i[2])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def delete_obstacles():
    for i in range (len(obstacles)):
        print (i,obstacles[i])
    print ("Which buoy should be removed?")
    command=input()
    obstacles.pop(int(command))
    print ("Buoy",command,"removed")

def print_commands():
    print("✨List of commands✨")
    print("help                                              -- prints list of command")
    print("obstacle x1:y1:color x2:y2:color x3:y3:color ...  -- adds buoys, color - red, green or yellow, ")
    print("show                                              -- shows buoys")
    print("delete                                            -- delete buoy")
    print("exit                                              -- finishes the program")

print_commands()
exit=True
while exit==True:
    command=input()
    command_array=command.split(" ")
    match command_array[0]:
        case "obstacle":
            for i in range(1,len(command_array)):
                add_obstacle(float(command_array[i].split(":")[0]), float(command_array[i].split(":")[1]), command_array[i].split(":")[2])
        case "show":
            show_obstacles()
        case "exit":
            exit=False
        case "delete":
            delete_obstacles()
        case _:
            print("No such command found")
