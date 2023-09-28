file = open('input.txt')
content = file.read()
lines = content.splitlines()
num_rooms = int(lines[0])
first_line = 1
#  main for cycle
for room in range(0, num_rooms):
    info = lines[first_line].split(" ")
    num_maschines = int(info[2])
    h, w = (int(info[0]), int(info[1]))
    cables = {}
    forms = []
    intersection = 0

    for line_num in range(first_line + 1, first_line + num_maschines + 1):
        maschine_info = lines[line_num].split(" ")
        #
        print(maschine_info)
        #

        #  getting info
        cable_yx = (int(maschine_info[1]), int(maschine_info[0]))
        cable_type = maschine_info[2]

        #  trying parity
        if cable_type not in cables:
            cables[cable_type] = cable_yx
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

            c = (cable_yx[0] - cables[cable_type][0]) * cables[cable_type][1] \
                - (cable_yx[1] - cables[cable_type][1]) * cables[cable_type][0]
            general_line = ((cables[cable_type][0] - cable_yx[0]),
                            (cable_yx[1] - cables[cable_type][1]),
                            c)
            #
            #  print(general_line)
            #
            forms.append(general_line)
            cables.pop(cable_type)
        #
        print(cables)
        #
    first_line += num_maschines + 1
    #
    print(forms)
    #

    for i in range(len(forms)):
        for j in range(i + 1, len(forms)):

            #  compare(forms[i], forms[j])
            try:
                #####
                y = (forms[j][0] * forms[i][2] - forms[i][0] * forms[j][2]) / \
                    (forms[j][0] * forms[i][1] - forms[i][0] * forms[j][1])
                x = (- forms[i][1] * y - forms[i][2]) / (forms[i][0])
                if 0 <= x <= w and 0 <= y <= h:
                    intersection += 1
                else:
                    continue
            except ZeroDivisionError:
                continue

    if len(cables) != 0 or intersection > 0:
        print("ajajaj")
    else:
        print("pujde to")
