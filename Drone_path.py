import math
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

T_start = 0
T_end = 100

flight_time = T_end - T_start

# Primary drone's path
primary_drone = { 
    'waypoints': [
        {'x':  0, 'y':  0, 'z':  0, 't': round(flight_time*1/5,1)},  
        {'x': 10, 'y': 10, 'z': 10, 't': round(flight_time*2/5,1)},  
        {'x': 20, 'y': 20, 'z': 20, 't': round(flight_time*3/5,1)},  
        {'x': 30, 'y': 30, 'z': 30, 't': round(flight_time*4/5,1)},  
        {'x': 40, 'y': 40, 'z': 40, 't': round(flight_time*5/5,1)} 
    ]

}

#Secondary Drone's path
simulated_flights = [
    {
        'drone_number' : '1',
        'waypoints': [
            {'x':  2, 'y': 42, 'z':  2, 't': round(flight_time*1/5,1)}, 
            {'x': 12, 'y': 32, 'z': 12, 't': round(flight_time*2/5,1)},  
            {'x': 22, 'y': 22, 'z': 22, 't': round(flight_time*3/5,1)}, 
            {'x': 32, 'y': 12, 'z': 32, 't': round(flight_time*4/5,1)},  
            {'x': 42, 'y':  2, 'z': 42, 't': round(flight_time*5/5,1)} 
        ]
    },
    {
        'drone_number' : '2',
        'waypoints': [
            {'x': 10, 'y': 10, 'z': 50, 't': round(flight_time*1/5,1)},
            {'x': 20, 'y': 20, 'z': 40, 't': round(flight_time*2/5,1)}, 
            {'x': 30, 'y': 30, 'z': 30, 't': round(flight_time*3/5,1)},  
            {'x': 40, 'y': 40, 'z': 20, 't': round(flight_time*4/5,1)},  
            {'x': 50, 'y': 50, 'z': 10, 't': round(flight_time*5/5,1)}  
        ]
    }
] 










# # Primary drone's path
# primary_drone = { 
#     'waypoints': [
#         {'x': 6, 'y': 5, 'z': 11, 't': 0},
#         {'x': 7, 'y': 6, 'z': 12, 't': 11},
#         {'x': 8, 'y': 8, 'z': 13, 't': 22},
#         {'x': 10, 'y': 10, 'z': 14, 't': 33},
#         {'x': 11, 'y': 12, 'z': 15, 't': 44},
#         {'x': 13, 'y': 14, 'z': 16, 't': 56},
#         {'x': 14, 'y': 16, 'z': 18, 't': 67},
#         {'x': 16, 'y': 18, 'z': 19, 't': 78},
#         {'x': 17, 'y': 20, 'z': 20, 't': 89},
#         {'x': 18, 'y': 22, 'z': 21, 't': 100}     
#     ]

# }

# #Secondary Drone's path
# simulated_flights = [
#     {
#         'drone_number' : '1',
#         'waypoints': [
#             {'x': 15, 'y': 1, 'z': 15, 't': 0},
#             {'x': 16, 'y': 2, 'z': 16, 't': 11},
#             {'x': 18, 'y': 4, 'z': 17, 't': 22},
#             {'x': 20, 'y': 6, 'z': 18, 't': 33},
#             {'x': 22, 'y': 7, 'z': 19, 't': 44},
#             {'x': 24, 'y': 9, 'z': 21, 't': 56},
#             {'x': 26, 'y': 11, 'z': 22, 't': 67},
#             {'x': 28, 'y': 12, 'z': 23, 't': 78},
#             {'x': 30, 'y': 14, 'z': 24, 't': 89},
#             {'x': 32, 'y': 16, 'z': 26, 't': 100}
#         ]
#     },
#     {
#         'drone_number' : '2',
#         'waypoints': [
#             {'x': 0, 'y': 19, 'z': 20, 't': 0},
#             {'x': 2, 'y': 20, 'z': 22, 't': 11},
#             {'x': 4, 'y': 22, 'z': 25, 't': 22},
#             {'x': 6, 'y': 24, 'z': 28, 't': 33},
#             {'x': 9, 'y': 26, 'z': 31, 't': 44},
#             {'x': 11, 'y': 28, 'z': 33, 't': 56},
#             {'x': 13, 'y': 30, 'z': 36, 't': 67},
#             {'x': 15, 'y': 31, 'z': 39, 't': 78},
#             {'x': 18, 'y': 33, 'z': 42, 't': 89},
#             {'x': 20, 'y': 35, 'z': 44, 't': 100}
#         ]
#     },
#     {
#         'drone_number' : '3',
#         'waypoints': [
#             {'x': 10, 'y': 11, 'z': 13, 't': 0},
#             {'x': 10, 'y': 11, 'z': 13, 't': 11},
#             {'x': 10, 'y': 11, 'z': 13, 't': 22},
#             {'x': 11, 'y': 11, 'z': 13, 't': 33},
#             {'x': 11, 'y': 12, 'z': 14, 't': 44},
#             {'x': 11, 'y': 12, 'z': 14, 't': 56},
#             {'x': 12, 'y': 12, 'z': 14, 't': 67},
#             {'x': 12, 'y': 13, 'z': 15, 't': 78},
#             {'x': 12, 'y': 13, 'z': 15, 't': 89},
#             {'x': 13, 'y': 13, 'z': 15, 't': 100}
#         ]
#     }
# ]





# # Primary drone's path
# primary_drone = { 
#     'waypoints': [
#         {'x': 19, 'y': 2, 'z': 7, 't': 0},
#         {'x': 20, 'y': 3, 'z': 8, 't': 11},
#         {'x': 22, 'y': 5, 'z': 10, 't': 22},
#         {'x': 23, 'y': 6, 'z': 12, 't': 33},
#         {'x': 25, 'y': 8, 'z': 14, 't': 44},
#         {'x': 26, 'y': 10, 'z': 16, 't': 56},
#         {'x': 28, 'y': 11, 'z': 18, 't': 67},
#         {'x': 29, 'y': 13, 'z': 19, 't': 78},
#         {'x': 31, 'y': 14, 'z': 21, 't': 89},
#         {'x': 32, 'y': 16, 'z': 23, 't': 100}      
#     ]

# }

# #Secondary Drone's path
# simulated_flights = [
#     {
#         'drone_number' : '1',
#         'waypoints': [
#             {'x': 7, 'y': 8, 'z': 13, 't': 0},
#             {'x': 9, 'y': 9, 'z': 14, 't': 11},
#             {'x': 12, 'y': 10, 'z': 15, 't': 22},
#             {'x': 15, 'y': 11, 'z': 16, 't': 33},
#             {'x': 18, 'y': 12, 'z': 17, 't': 44},
#             {'x': 20, 'y': 14, 'z': 18, 't': 56},
#             {'x': 23, 'y': 15, 'z': 19, 't': 67},
#             {'x': 26, 'y': 16, 'z': 20, 't': 78},
#             {'x': 29, 'y': 17, 'z': 21, 't': 89},
#             {'x': 31, 'y': 18, 'z': 22, 't': 100}
#         ]
#     },
#     {
#         'drone_number' : '2',
#         'waypoints': [
#             {'x': 0, 'y': 17, 'z': 14, 't': 0},
#             {'x': 2, 'y': 18, 'z': 15, 't': 11},
#             {'x': 5, 'y': 20, 'z': 17, 't': 22},
#             {'x': 7, 'y': 22, 'z': 19, 't': 33},
#             {'x': 10, 'y': 24, 'z': 21, 't': 44},
#             {'x': 12, 'y': 26, 'z': 23, 't': 56},
#             {'x': 15, 'y': 28, 'z': 25, 't': 67},
#             {'x': 17, 'y': 30, 'z': 27, 't': 78},
#             {'x': 20, 'y': 32, 'z': 29, 't': 89},
#             {'x': 22, 'y': 33, 'z': 31, 't': 100} 
#         ]
#     },
# ]










# # Primary drone's path
# primary_drone = { 
#     'waypoints': [
#         {'x': 3, 'y': 42, 'z': 8, 't': 0},
#         {'x': 6, 'y': 45, 'z': 11, 't': 10},
#         {'x': 9, 'y': 48, 'z': 14, 't': 20},
#         {'x': 12, 'y': 51, 'z': 17, 't': 30},
#         {'x': 15, 'y': 54, 'z': 20, 't': 40},
#         {'x': 18, 'y': 57, 'z': 23, 't': 50},
#         {'x': 21, 'y': 60, 'z': 26, 't': 60},
#         {'x': 24, 'y': 63, 'z': 29, 't': 70},
#         {'x': 27, 'y': 66, 'z': 32, 't': 80},
#         {'x': 30, 'y': 69, 'z': 35, 't': 100}
#     ]

# }

# #Secondary Drone's path
# simulated_flights = [
#     {
#         'drone_number' : '1',
#         'waypoints': [
#             {'x': 13, 'z': 42, 'y': 8, 't': 0},
#             {'x': 6, 'z': 35, 'y': 11, 't': 10},
#             {'x': 9, 'z': 48, 'y': 24, 't': 20},
#             {'x': 22, 'z': 31, 'y': 17, 't': 30},
#             {'x': 25, 'z': 54, 'y': 20, 't': 40},
#             {'x': 18, 'z': 57, 'y': 23, 't': 50},
#             {'x': 31, 'z': 60, 'y': 26, 't': 60},
#             {'x': 24, 'z': 63, 'y': 39, 't': 70},
#             {'x': 27, 'z': 56, 'y': 32, 't': 80},
#             {'x': 40, 'z': 59, 'y': 35, 't': 100}
#         ]
#     },
#     {
#         'drone_number' : '2',
#         'waypoints': [
#             {'y': 17, 'x': 38, 'z': 2, 't': 0},
#             {'y': 10, 'x': 31, 'z': 5, 't': 11},
#             {'y': 23, 'x': 44, 'z': 8, 't': 22},
#             {'y': 16, 'x': 47, 'z': 21, 't': 33},
#             {'y': 19, 'x': 30, 'z': 14, 't': 44},
#             {'y': 12, 'x': 53, 'z': 17, 't': 55},
#             {'y': 25, 'x': 56, 'z': 26, 't': 66},
#             {'y': 38, 'x': 59, 'z': 23, 't': 77},
#             {'y': 31, 'x': 52, 'z': 26, 't': 88},
#             {'y': 34, 'x': 55, 'z': 39, 't': 100}
#         ]
#     },
#     {
#         'drone_number' : '3',
#         'waypoints': [
#             {'z': 17, 'y': 18, 'x': 2, 't': 0},
#             {'z': 20, 'y': 21, 'x': 5, 't': 11},
#             {'z': 23, 'y': 24, 'x': 8, 't': 22},
#             {'z': 26, 'y': 37, 'x': 11, 't': 33},
#             {'z': 39, 'y': 40, 'x': 14, 't': 44},
#             {'z': 32, 'y': 53, 'x': 27, 't': 55},
#             {'z': 25, 'y': 56, 'x': 30, 't': 66},
#             {'z': 28, 'y': 59, 'x': 33, 't': 77},
#             {'z': 31, 'y': 62, 'x': 46, 't': 88},
#             {'z': 34, 'y': 65, 'x': 49, 't': 100}
#         ]
#     }
# ]







# Calculating the distance between two points by taking square root of sum of square of their coordinates 
def calculate_distance(point1, point2):  
    return math.sqrt((point2['x'] - point1['x'])**2 + (point2['y'] - point1['y'])**2 + (point2['z'] - point1['z'])**2)

# Checking spatal conflicts
def check_spatial_conflicts(primary_drone, simulated_flights):
    conflicts = []
    for simulated_flight in simulated_flights:
        sim_flight_number = simulated_flight['drone_number']
        for waypoint in primary_drone['waypoints']:
            for simulated_waypoint in simulated_flight['waypoints']:
                distance = calculate_distance(waypoint, simulated_waypoint)
                if distance < 4:  
                    conflicts.append({
                        'primary_waypoint': waypoint,
                        'simulated_waypoint': simulated_waypoint,
                        'distance': distance,
                        'drone_number': sim_flight_number
                    })
    return conflicts


#Checking temporal conflicts
def check_temporal_conflicts(primary_drone, simulated_flights):
    conflicts = []
    for simulated_flight in simulated_flights:
        sim_flight_number = simulated_flight['drone_number']
        for waypoint in primary_drone['waypoints']:
            for simulated_waypoint in simulated_flight['waypoints']:
                distance = calculate_distance(waypoint, simulated_waypoint)
                if (waypoint['t'] - simulated_waypoint['t']) < 5 and (simulated_waypoint['t'] - waypoint['t']) < 5 and distance < 4: 
                    conflicts.append({
                        'primary_waypoint': waypoint,
                        'simulated_waypoint': simulated_waypoint,
                        'distance': round(distance,2),
                        'time': int(waypoint['t']),
                        'drone_number': sim_flight_number   
                    })
    return conflicts



# storing final temporal conflicts (which also contain the spatial conflicts information)
temporal_conflicts = check_temporal_conflicts(primary_drone, simulated_flights)


# Printing the conflicts information in the console
if temporal_conflicts == []:
    print('The Primary mission is clear')
else:  
    print('Conflict is detected on these points')
    for conflict in temporal_conflicts:
        print(conflict)



# Visualization on matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

primary_waypoints = primary_drone['waypoints']
ax.plot([wp['x'] for wp in primary_waypoints], [wp['y'] for wp in primary_waypoints],
         [wp['z'] for wp in primary_waypoints], 'bo-', linewidth=4, label = "Primary Drone")

for i, wp in enumerate(primary_waypoints):
    ax.text(wp['x'], wp['y'], wp['z'], wp['t'],fontsize = 6)


colors = ['red', 'green', 'magenta','pink'] 
for i, simulated_flight in enumerate(simulated_flights):
    simulated_waypoints = simulated_flight['waypoints']
    ax.plot([wp['x'] for wp in simulated_waypoints], [wp['y'] for wp in simulated_waypoints],
             [wp['z'] for wp in simulated_waypoints], colors[i],label = " Simulated Drone " + simulated_flight['drone_number'])

    for j, wp in enumerate(simulated_waypoints):
        ax.text(wp['x'], wp['y'], wp['z'], wp['t'],fontsize = 6)

# Annonating the plot
ax.legend(ncol=6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Drone Mission')

if temporal_conflicts == []: 
    fig.text(0.51, 0.88,'Clear', ha='center', va='center', fontsize=8, color='green')
else:
    fig.text(0.51, 0.88,'CONFLICT DETECTED', ha='center', va='center', fontsize=8, color='red')

plt.show()