file = open('input.txt')
content = file.read()
lines = content.splitlines()
forms = []
num_rooms = int(lines[0])
first_line = 1
#  main for cycle
for room in range(0, num_rooms):
    info = lines[first_line].split(" ")
    num_maschines = int(info[2])
    cables = {}

    for line_num in range(first_line + 1, first_line + num_maschines + 1):
        maschine_info = lines[line_num].split(" ")
        #
        print(maschine_info)
        #

        #  getting info
        cable_xy = (int(maschine_info[0]), int(maschine_info[1]))
        cable_type = maschine_info[2]

        #  trying parity
        if cable_type not in cables:
            cables[cable_type] = cable_xy
        else:

            #  line general form calculation

            # xa = cables[cable_type][0]
            # xb = cables[cable_type][1]
            # ya = cable_xy[0]
            # yb = cable_xy[1]
            # c = (yb - xb) * xa \
            #     - (ya - xa) * xb
            # general_line = ((xb - yb),
            #                 (ya - xa),
            #                 c)

            c = (cable_xy[1] - cables[cable_type][1]) * cables[cable_type][0]\
                - (cable_xy[0] - cables[cable_type][0]) * cables[cable_type][1]
            general_line = ((cables[cable_type][1] - cable_xy[1]),
                            (cable_xy[0] - cables[cable_type][0]),
                            c)
            #
            print(general_line)
            #
            cables.pop(cable_type)
        #
        print(cables)
        #
    first_line += num_maschines + 1

    if len(cables) != 0:
        print("ajajaj")
    else:
        print("pujde to")
