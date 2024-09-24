N = int(input("N: "))

u = []
v = []

for i in range(N):
        u_component = int(input(f"u[{i+1}]: "))
        u.append(u_component)
        
for i in range(N):
        v_component = int(input(f"v[{i+1}]: "))
        v.append(v_component)

def plus(u, v):
    vect = []
    for component in range(N):
        vect.append(u[component] + v[component])
    return vect

def dot(u, v):
    number = 0
    for component in range(N):
        number += u[component] * v[component]
    return number

def times(u, v):
    vect = []
    for component in range(N):
        vect.append(u[component] + v[component])
    return vect

print("u+v = ", plus(u, v))
print("u.v = ", dot(u, v2))