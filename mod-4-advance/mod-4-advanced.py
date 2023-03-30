'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def relationship_status(from_member, to_member, social_graph):
        if from_member == to_member:
            return f"{from_member} is the same as {to_member}"

        if to_member in social_graph.get(from_member, []):
            if from_member in social_graph.get(to_member, []):
                return f"{from_member} follows {to_member}"
            else:
                return f"{from_member} and {to_member} are friends."

        elif from_member in social_graph.get(to_member, []):
            return f"{to_member} is followed by {from_member}"

        else:
            return f"{from_member} and {to_member} does not have relationship on this app"

    def relationship():
        social_graph = {
            "@bongolpoc": {"first_name": "Joselito",
                           "last_name": "Olpoc",
                           "following": [
                           ]
                           },
            "@joaquin": {"first_name": "Joaquin",
                         "last_name": "Gonzales",
                         "following": [
                             "@chums", "@jobenilagan"
                         ]
                         },
            "@chums": {"first_name": "Matthew",
                       "last_name": "Uy",
                       "following": [
                           "@bongolpoc", "@miketan", "@rudyang", "@joeilagan"
                       ]
                       },
            "@jobenilagan": {"first_name": "Joben",
                             "last_name": "Ilagan",
                             "following": [
                                 "@eeebeee", "@joeilagan", "@chums", "@joaquin"
                             ]
                             },
            "@joeilagan": {"first_name": "Joe",
                           "last_name": "Ilagan",
                           "following": [
                               "@eeebeee", "@jobenilagan", "@chums"
                           ]
                           },
            "@eeebeee": {"first_name": "Elizabeth",
                         "last_name": "Ilagan",
                         "following": [
                             "@jobenilagan", "@joeilagan"
                         ]
                         },
        }
        # prints the relationship status in the social_graph dict
        print(relationship_status('@bongolpoc', '@chums', social_graph))

    relationship()


def tic_tac_toe(board):
    '''Tic Tac Toe.
    15 points.
    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # string of the board 0-15 for 4x4
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # 4 by 4 board print using list
    def tic_tac_toe(board):
        print(f"{board[0]} | {board[1]} | {board[2]} | {board[3]} ")
        print("---------------")
        print(f"{board[4]} | {board[5]} | {board[6]} | {board[7]} ")
        print("---------------")
        print(f"{board[8]} | {board[9]} | {board[10]} | {board[11]} ")
        print("---------------")
        print(f"{board[12]} | {board[13]} | {board[14]} | {board[15]} ")

    # Checks the arguments whether the game is finished or not
    def is_game_over(board):
        # Check rows
        for i in range(0, 16, 4):
            if board[i] == board[i + 1] == board[i + 2] == board[i + 3] and board[i] != ' ':
                return True

        # Check columns
        for i in range(4):
            if board[i] == board[i + 4] == board[i + 8] == board[i + 12] and board[i] != ' ':
                return True

        # Check diagonals
        if board[0] == board[4] == board[8] and board[i + 12] != ' ':
            return True
        elif board[2] == board[4] == board[8] == board[12] and board[15] != ' ':
            return True

        # Check for tie
        if ' ' not in board:
            return True

        # Game is not over yet; returns to the game
        return False

    # Define the main game loop
    player = 'X'
    while not is_game_over(board):
        # Prints the game board
        tic_tac_toe(board)

        # Ask the player for their move
        move = int(input(f"Player {player}, enter your move (1-16): ")) - 1

        # Check if the move is valid
        if board[move] != ' ':
            print("Invalid move, try again")
            continue

        # Update the game board
        board[move] = player

        # Switch to the other player
        player = 'O' if player == 'X' else 'X'

    # Print the final game board
    print(tic_tac_toe(board))

    # Check who won or if it's a tie
    if ' ' not in board:
        print("NO WINNER")

    else:
        print(f"Player {player} won!")


def eta(first_stop, second_stop, route_map):
    '''ETA.
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
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
