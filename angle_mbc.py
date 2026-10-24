import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))
print(str(round(angle)) + chr(176))
