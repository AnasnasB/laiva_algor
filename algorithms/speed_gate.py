import math
import time



position = [0, 0]  # Robot's current position (x, y)
gates = [(1, 1), (1, -1)]  # Coordinates of gate entry points
marker_buoy = (5, 0)  # Coordinates of the marker buoy

def move_to(target):
    print(f"Moving to target: {target}")
    while not is_at_target(target):
        update_position(target)
        time.sleep(0.1)  
    print(f"Reached target: {target}")

def is_at_target(target): #chacks if at target
    return math.dist(position, target) < 0.1

def update_position(target):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    position[0] += 0.1 * math.cos(direction)
    position[1] += 0.1 * math.sin(direction)
    print(f"Now at: {position}")

def navigate_through_gates():  #goes threw gates
    middle = middle_path(gates)
    move_to(middle)

def circle_marker_buoy():
        radius = 1.0  # Circle radius
        num_points = 20 
        angle_step = 2 * math.pi / num_points

        for i in range(num_points + 1):
            angle = i * angle_step
            x = marker_buoy[0] + radius * math.cos(angle)
            y = marker_buoy[1] + radius * math.sin(angle)
            move_to((x, y))

        print("Completed circling buoy.")

def middle_path(gates):
        middle = ((gates[0][0] + gates[1][0])/2, (gates[0][1] + gates[1][1])/2)
        return middle

def speed_gate():
        print("Starting...")
        navigate_through_gates()
        circle_marker_buoy()
        navigate_through_gates()
        print("We did it!")

speed_gate()

