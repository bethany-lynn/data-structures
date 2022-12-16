"""Functions to parse a file containing villager data."""
# import sys
# name | species | personality | hobby | motto

def all_species(filename):
    """ return a set of unique species in the file"""

    unique_species = set() #creates a set named unique_species - needs to be set so we dont get repeated species
    data = open(filename) #initializing the file - filename could be called anything i choose
    
    for line in data: #looping through every line in the file
            tokens = line.split("|") #
            unique_species.add(tokens[1])
    unique_species = list(unique_species) # -- turns set into list
    print(type(unique_species)) #prints out what type of data structure unique_species is
    return sorted(unique_species)

print(all_species("villagers.csv")) #has to be a string
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
