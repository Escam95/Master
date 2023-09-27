file = open('input.txt')
content = file.read()
lines = content.splitlines()

num_rooms = int(lines[0])

#  main for cycle
for room in range(0, num_rooms):
    for line in lines:
        ...

connections = {}