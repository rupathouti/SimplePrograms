import json

point = json.loads('{"x":10,"y":10}')

print(point)

print("x = {}".format(point.get("x")))
print("y = {}".format(point.get("y")))
