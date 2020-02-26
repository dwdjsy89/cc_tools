
import json
#import daweiw2_cc1

#Part 3
#Load your custom JSON file


json_file_name = "data/daweiw2_cc1.json"
with open(json_file_name, "r") as reader:
    json_data = json.load(reader)

#Convert JSON data to CCLevelPack

class OptionalFields:
    def __init__(self,Op):
        self.field_3 = Op["field_3"]
        self.field_6 = Op["field_6"]
        self.field_7 = Op["field_7"]
        self.field_10 = Op["field_10"]

from cc_tools.cc_classes import CCField

class CCMapTitleField(CCField):
    def __init__(self, title):
        if __debug__:
            if len(title) >= 64: raise AssertionError("Map Title must be 63 characters or fewer. Current title is '"+title+"'("+str(len(title))+")")
        self.title = title
        self.type_val = 3

class CCEncodedPasswordField(CCField):
    def __init__(self, password):
        if __debug__:
            if len(password) > 9 or len(password) < 4:
                raise AssertionError("Encoded password must be from 4 to 9 characters in length. Password passed is '"+str(password)+"'")
        self.password = password
        self.type_val = 6

    def __str__(self):
        return_str = "    Encoded Password Field (type=6)\n"
        return_str += "      password = "+str(self.password)
        return return_str

class CCMapHintField(CCField):
    def __init__(self, hint):
        if __debug__:
            if len(hint) > 127 or len(hint) < 0:
                raise AssertionError("Hint must be from 0 to 127 characters in length. Hint passed is '"+hint+"'")
        self.hint = hint
        self.type_val = 7

class CCMonsterMovementField(CCField):
    def __init__(self, monsters):
        if __debug__:
            if len(monsters) > 128:
                raise AssertionError("Max monster count of 128 exceeded. Number of monsters passed = "+str(len(monsters)))
        self.monsters = monsters
        self.type_val = 10

class CCField:
    #def __init__(self, type_val, byte_val):
    def __init__(self, type_val):
        self.type_val = type_val
        #self.byte_val = byte_val


class CCLevel:
    '''
    def __init__(self, L):
        self.level_number = L["level_number"]
        self.time = L["time"]
        self.num_chips = L["num_chips"]
        self.upper_layer = L["upper_layer"]
        self.optional_fields = []
        self.lower_layer = []

    '''
    def __init__(self):
        self.level_number =-1
        self.time = -1
        self.num_chips = -1
        self.upper_layer = []
        self.lower_layer = []
        self.optional_fields = []

    def add_field1(self, field):
        self.optional_fields.append(CCLevel(json_data["CC Level Pack"][field]))

    def add_field(self, field):
        self.optional_fields.append(field)



class CCLevelPack:
    def __init__(self, L):
        self.levels = L
        self.level_count = len(self.levels)

'''
class CCLevelPack:
    def __init__(self):
        self.levels = []
'''

def make_CCLevels_from_json(json_data):
    game_level = []
    for i in range(len(json_data["CC Level Pack"])):
        game_level.append(CCLevel(json_data["CC Level Pack"][i]))
    return CCLevelPack(game_level)


cc_level_pack = make_CCLevels_from_json(json_data)
#Save converted data to DAT file
#new_level_pack=cc_level_pack

'''
class new_level:
    def add_field(self, field):
        self.optional_fields.append(field)

    def __init__(self, L):
        for json_field in L["optional_fields"]:
            field_type = json_field["field_type"]
            if field_type == "hint":
                new_hint_field = CCMapHintField(json_field["hint"])
                new_level.add_field(new_hint_field)
            elif field_type == "hint":
                new_title_field = CCMapTitleField(json_field["title"])
                new_level.add_field(new_title_field)
            elif field_type == "password":
                new_password_field=CCEncodedPasswordField(json_field["password"])
                new_level.add_field(new_password_field)
'''

for json_level in json_data["CC Level Pack"]:
    new_level=CCLevelPack()
    new_level.level_number=json_level["level_number"]
    new_level.num_chips=json_level["num_chips"]
    new_level.time=json_level["time"]
    new_level.upper_layer=json_level["upper_layer"]

    for json_field in json_level["optional_fields"]:
        field_type = json_field["field_type"]
        if field_type == "hint":
            new_hint_field = CCMapHintField(json_field["hint"])
            new_level.add_field(new_hint_field)
        elif field_type == "hint":
            new_title_field = CCMapTitleField(json_field["title"])
            new_level.add_field(new_title_field)
        elif field_type == "password":
            new_password_field = CCEncodedPasswordField(json_field["password"])
            new_level.add_field(new_password_field)









import cc_dat_utils
#cc_dat_utils.write_cc_level_pack_to_dat()
cc_dat_utils.write_cc_level_pack_to_dat(CCLevelPack, "data/daweiw2.dat")
#input_dat_file = 'data/pfgd_test.dat'
#cc_level_pack = cc_dat_utils.make_cc_level_pack_from_dat("data/pfgd_test.dat")
#cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack, "data/TEST.dat")
#cc_level_pack = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)
#print(cc_level_pack)

#cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack, "data/daweiw2.dat")
#cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack, "../TileWorld/data/daweiw2.dat")
