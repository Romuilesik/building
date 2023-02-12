class fasade:
    floor = 100
    concrete = 80

class wall(fasade):
    brigade = 30
    metal = 90

class house(wall):
    heat = 50
    light = 40

roma = fasade
roman = wall
romchik = house

print(roma.pol)