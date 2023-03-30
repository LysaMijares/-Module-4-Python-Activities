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
    print(relationship_status('@bongolpoc', '@chums', social_graph))


relationship()
