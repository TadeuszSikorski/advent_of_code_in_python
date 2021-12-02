def _create_floors(brackets):
    floor, floors = 0, []

    for bracket in brackets:
        if bracket == "(":
            floor += 1
            floors.append(floor)
        
        if bracket == ")":
            floor -= 1
            floors.append(floor)
            
    return floors


def check_floor(brackets):
    return _create_floors(brackets)[-1]


def check_position(brackets, floor):
    floors = _create_floors(brackets)
    
    return floors.index(floor) + 1
