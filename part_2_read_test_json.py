import test_data
import json

# Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    # Initialize a new GameLibrary
    game_library = []
    #game_library = test_data.GameLibrary()
    ### Begin Add Code Here ###
    class platform:
        def __init__(self, p):
            self.launch_year = p["launch year"]
            self.name = p["name"]
    class games:
        def __init__(self, g):
            self.title = g["title"]
            self.year = g["year"]
            self.platform = platform(g["platform"])
    # Loop through the json_data
    for i in range(len(json_data["games"])):
        game_library.append(games(json_data["games"][i]))
    return game_library

    # Create a new Game object from the json_data by reading
    #  title
    #  year
    #  platform (which requires reading name and launch_year)
    # Add that Game object to the game_library
def __str__(game_library):
    return_str = "Analyzing game library data:\n"
    game_count = 0
    for games in game_library:
        return_str += "Game " + str(game_count) + "\n"
        return_str += " Title: " + games.title + "\n"
        return_str += " Year: " + str(games.year) + "\n"
        return_str += " Platform = " + "\n"
        return_str += "     Name: " + games.platform.name + "\n"
        return_str += "     Launch Year: " + str(games.platform.launch_year) + "\n"
        game_count += 1
    return return_str
    ### End Add Code Here ###



# Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
# Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
# Use the json module to load the data from the file
    test_json_data = json.load(reader)
# Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library = make_game_library_from_json(test_json_data)
# Print out the resulting GameLibrary data using print()
return_str = __str__(game_library)
print(return_str)
### End Add Code Here ###
