def passing_cars(number):
    count = 0
    east_cars = []
    west_cars = []

    index = 0
    for number in number:
        if number == 0:
            east_cars.append(index)
        else:
            west_cars.append(index)
        index += 1

    index = 0
    for east_car in east_cars:

        for west_car in west_cars[index:]:
            if west_car > east_car:
                break
            index += 1

        count += len(west_cars[index:])

    return count


def fast_passing_cars(number):
    count = 0
    east_cars = []
    west_cars = []

    index = 0
    length = 0
    for number in number:
        if number == 0:
            east_cars.append((index, length))
        else:
            west_cars.append(index)
            length += 1
        index += 1

    total_length = len(west_cars)
    for east_car in east_cars:
        count += total_length - east_car[1]

    if count > 1000000000:
        return -1
    return count




