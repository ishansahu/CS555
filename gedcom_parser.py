#   Course: CS-555
#   Team 08
def parse(file_path):
    level = tag = argument = "Not Found"
    tag_map = { '0' : ['HEAD','NOTE','TRLR'], 
                '1' : ['BIRT','CHIL','DIV','HUSB','WIFE','MARR','NAME','SEX','DEAT','FAMC','FAMS'], 
                '2' : ['DATE']}
    try:
        with open(file_path) as ged_file:
            for line in ged_file:
                line = line.strip()
                print("-->{}".format(line))
                args = line.split(" ")
                number_of_args = len(args)
                if number_of_args == 3 and args[0] == '0' and args[2] in {'INDI','FAM'}:
                    level, tag, argument = args
                    valid_tags = 'Y'
                elif number_of_args >= 2:
                    level, tag = args[0],args[1]
                    argument = " ".join(args[2:])
                    valid_tags = 'Y' if level in tag_map and tag in tag_map[level] else 'N'
                else:
                    valid_tags ='N'
                    level, tag, argument = args

                print("<--{}|{}|{}|{}".format(level, tag, valid_tags, argument))
    except:
        print("File not found or can't be accessed")
parse('InputFiles/Project01.ged')
