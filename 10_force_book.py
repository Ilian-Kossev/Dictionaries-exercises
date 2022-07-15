force_side_register = {}
command = input()
while not command == 'Lumpawaroo':
    if '|' in command:
        force_side, force_user = command.split(' | ')
        if force_side not in force_side_register:
            for item in force_side_register.values():
                if force_user in item:
                    command = input()
                    break
            force_side_register[force_side] = []
        force_side_register[force_side].append(force_user)
    else:
        force_user, force_side = command.split(' -> ')
        force_user_not_present_in_force_side = True
        join_member = False
        for item in force_side_register.values():
            if force_user in item:
                force_user_not_present_in_force_side = False
                item.remove(force_user)
                force_side_register[force_side].append(force_user)
                join_member = True
                break
        if force_user_not_present_in_force_side:
            force_side_register[force_side].append(force_user)
            join_member = True
        if force_side not in force_side_register and force_user_not_present_in_force_side:
            force_side_register[force_side] = []
            force_side_register[force_side].append(force_user)
            join_member = True
        if join_member:
            print(f'{force_user} joins the {force_side} side!')
    command = input()

sorted_register = dict(sorted(force_side_register.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in sorted_register.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        value.sort()
    for item in value:
        print(f'! {item}')

