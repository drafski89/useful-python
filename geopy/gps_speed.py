# Purpose:  Calculates the speed between two points 
#           Takes two time stamps and two values in decimals of lat and long

from geopy.distance import vincenty

# This is a stationary test point
position1 = (32.1297027,-110.9944952)
position2 = (32.1297026,-110.9944952)
timestamp1 = 1478901884093
timestamp2 = 1478901885115

# This is a moving test point
# position1 = (32.1300215,-110.9944801)
# position2 = (32.1300997,-110.9944727)
# timestamp1 = 1478901917141
# timestamp2 = 1478901918153

# Find the time between the two time stamps
delta_time_ms = timestamp2 - timestamp1
delta_time_seconds = delta_time_ms/1000.0

# Use the vincenty method to calculate the distance
distance = vincenty(position1, position2).meters

# Print the distance between the two points
print "{:.4f} Meters from Geopy".format(distance)

# Find the speed by distance/time
speed = distance/delta_time_seconds

# Print the time and the speed
# Not velocity because we have not processed the direction of motion
print "{:.4f} Seconds".format(delta_time_seconds)
print "{:.4f} Meters Per Second\n".format(speed)