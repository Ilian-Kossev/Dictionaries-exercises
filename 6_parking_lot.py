def register_car(collection: dict, user: str, numb: str):
    if user not in collection:
        collection[user] = numb
        print(f'{user} registered {numb} successfully')
    else:
        print(f'ERROR: already registered with plate number {numb}')


def unregister_car(collection: dict, user: str):
    if user not in collection:
        print(f'ERROR: user {user} not found')
    else:
        print(f'{user} unregistered successfully')
        del collection[user]


number = int(input())
car_register = {}
for num in range(number):
    command = input()
    command_data = command.split()
    action = command_data[0]
    username = command_data[1]
    if action == 'register':
        plate_number = command_data[2]
        register_car(car_register, username, plate_number)
    else:
        unregister_car(car_register, username)
for key, value in car_register.items():
    print(f'{key} => {value}')


