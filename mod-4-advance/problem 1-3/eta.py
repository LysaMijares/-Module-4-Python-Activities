def eta(first_stop, second_stop, route_map):
    # Find the legs that connect the first stop and the second stop
    legs = [(k, v) for k, v in route_map.items() if first_stop in k and second_stop in k]

    # If there is no direct leg between the stops, calculate the travel time
    # as the sum of the travel times from the first stop to the intersection
    # and from the intersection to the second stop
    if not legs:
        intersections = [k for k in route_map.keys() if first_stop in k or second_stop in k]
        if len(intersections) != 2:
            raise ValueError("Route is not fully connected")
        first_intersection = intersections[0] if first_stop in intersections[0] else intersections[1]
        travel_time = travel_time(first_stop, first_intersection, route_map) + travel_time(first_intersection,
                                                                                           second_stop, route_map)
    else:
        travel_time = legs[0][1]["travel_time_mins"]

    return travel_time


# def result_eta carries the leg dict from route_map and proceeds to the program
def result_eta():
    # dictionary of the route_map
    legs = {
        ("upd", "admu"): {
            "travel_time_mins": 10
        },
        ("admu", "dlsu"): {
            "travel_time_mins": 35
        },
        ("dlsu", "upd"): {
            "travel_time_mins": 55
        }
    }
    # defines the route_map to legs
    route_map = legs
    print("Welcome to the ETA Calculator!\nBuckle up!")
    first_stop = input("\nEnter the first stop: ")
    second_stop = input("Enter the second stop: ")
    # prints the ETA
    print("here is the Estimated Time of Arrival:", eta(first_stop, second_stop, route_map))


result_eta()
