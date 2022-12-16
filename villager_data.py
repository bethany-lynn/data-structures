"""Functions to parse a file containing villager data."""
# import sys


def all_species(filename):

    unique_species = set()
    data = open(filename) #initializing the file
    for line in data: #looping through every line in the file
            trimmed_line = line.rstrip() #gets rid of the spaces 
            tokenized_line = trimmed_line.split("|") #break it up with 
            species = tokenized_line[1] 
            unique_species.add(species)
    print(unique_species)
    return unique_species

# all_species("villagers.csv")
# 
# 
# 
def get_villagers_by_species(filename, search_string="All"):

    villagers = []
    data = open(filename)
    for line in data:
        trimmed_line = line.rstrip()
        tokenized_line = trimmed_line.split("|")
        names, species = tokenized_line[:2]
        # species = tokenized_line[2]
        if search_string in ("All", species):
            villagers.append(names)
        
    # print(villagers)    
    return sorted(villagers)
# print(get_villagers_by_species("villagers.csv", "Tiger"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby [3]

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    # villagers_name = []
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    data = open(filename)

    for line in data:
        trimmed_line = line.rstrip()
        tokenized_line = trimmed_line.split("|")
        name = tokenized_line[0]
        hobby = tokenized_line[3]
        
        if hobby == "Fitness":
            fitness.append(name)

        elif hobby == "Nature":
            nature.append(name)

        elif hobby == "Education":
            education.append(name)

        elif hobby == "Music":
            music.append(name)

        elif hobby == "Fashion":
            fashion.append(name)

        elif hobby == "Play":
            play.append(name)


    return [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
    ]

# print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    data = open(filename)
    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))


    return all_data

print(all_data("villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
