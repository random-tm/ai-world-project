

def main():
    askforstandardinput()


#standard input option
def askforstandardinput():
    ai_option = askforaigen()
    ai_gen = nestedyesornooption(ai_option, 1)
    folder_option = askforlorefolder()
    lorefolder = nestedyesornooption(folder_option, 2)
    persona_option = askforpersona()
    persona_type = nestedyesornooption(persona_option, 3)
    #if the filepath isn't needed, we can get rid of it later.
    filepath_option = askforfilepath()
    filepath = nestedyesornooption(filepath_option, 4)
    #if more options are required, we can add them later
    generatestory(ai_gen, lorefolder, persona_type, filepath)
    return


#if more input options are needed, we can add them later.

def nestedyesornooption(option, stage):
    yesno = input('You have selected: ' + option + 'Is this correct? Y/N')
    if yesno == 'Y' or 'y':
        return option
    elif yesno == 'N' or 'n':
        if stage == 1:
            option = askforaigen()
            option = nestedyesornooption(option, 1)
            return option
        elif stage == 2:
            option = askforlorefolder()
            option = nestedyesornooption(option, 2)
            return option
        elif stage == 3:
            option = askforpersona()
            option = nestedyesornooption(option, 3)
            return option
        elif stage == 4:
            option = askforfilepath()
            option = nestedyesornooption(option, 4)
            return option
        else:
            return 'Somehow, you screwed up the program. Not sure how, but try running it again.'
    else:
        print('You have not selected a valid option! Please try again.')
        nestedyesornooption(option, stage)


def askforaigen():
    ai_gen = input('Please input the ai generation you would like to have:')
    return ai_gen


def askforlorefolder():
    lorefolder = input('Please input the filepath you would like to generate the lore files into:')
    return lorefolder


def askforpersona():
    persona = input('Please input the persona type you would like to have:')
    return persona


def askforfilepath():
    filepath = input('Please input the filepath of the individual file you would like to load:')
    return filepath


def generatestory(ai_gen, lorefolder, persona_type, filepath):
    #TODO Add in generate story function
    return 'Arguments given: ' + 'AI type: ' + ai_gen + ', lorefolder: ' + lorefolder + ', persona type: ' + persona_type + ', filepath: ' + filepath + '.' # noqa
