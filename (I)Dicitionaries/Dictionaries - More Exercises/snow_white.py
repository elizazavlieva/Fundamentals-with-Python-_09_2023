dwarf_info = {}
color_count = {}
while True:
    command = input()
    if command == 'Once upon a time':
        break
    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)
    dwarf = (name, hat_color)
    if dwarf in dwarf_info:
        if physics > dwarf_info[dwarf]:
            dwarf_info[dwarf] = physics
    else:
        dwarf_info[dwarf] = physics

    if hat_color in color_count:
        color_count[hat_color] += 1
    else:
        color_count[hat_color] = 1


sorted_dwarfs = sorted(dwarf_info.items(), key=lambda x: (-x[1], -color_count[x[0][1]]))

for (name, hat_color), physics in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")
