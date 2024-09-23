from math import cos, pi, sin

v = 10
alpha = 60*pi/180
time = [1, 2, 5]

for t in time:
    x = v*cos(alpha)*t
    y = v*sin(alpha)*t - 0.5*9.8*t**2
    
    print(x, y)