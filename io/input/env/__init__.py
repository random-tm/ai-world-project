# standard input option
def ask_for_standard_input():
    ai_option = ask_for_ai_gen()
    ai_gen = ask_for_lore_folder(ai_option, 1)
    folder_option = ask_for_file_path()
    lore_folder = nested_yes_or_no_option(folder_option, 2)
    persona_option = ask_for_persona()
    persona_type = nested_yes_or_no_option(persona_option, 3)
    # if the filepath isn't needed, we can get rid of it later.
    file_path_option = ask_for_file_path()
    file_path = nested_yes_or_no_option(file_path_option, 4)
    # if more options are required, we can add them later
    generate_story(ai_gen, lore_folder, persona_type, file_path)
    return


# if more input options are needed, we can add them later.

def nested_yes_or_no_option(option, stage):
    yesno = input('You have selected: ' + option + 'Is this correct? Y/N')
    if yesno == 'Y' or 'y':
        return option
    elif yesno == 'N' or 'n':
        if stage == 1:
            option = ask_for_ai_gen()
            option = nested_yes_or_no_option(option, 1)
            return option
        elif stage == 2:
            option = ask_for_lore_folder()
            option = nested_yes_or_no_option(option, 2)
            return option
        elif stage == 3:
            option = ask_for_persona()
            option = nested_yes_or_no_option(option, 3)
            return option
        elif stage == 4:
            option = ask_for_file_path()
            option = nested_yes_or_no_option(option, 4)
            return option
        else:
            return 'Somehow, you screwed up the program. Not sure how, but try running it again.'
    else:
        print('You have not selected a valid option! Please try again.')
        nested_yes_or_no_option(option, stage)


def ask_for_ai_gen(ai_option):
    # TODO Use ai_option
    ai_gen = input('Please input the ai generation you would like to have:')
    return ai_gen


def ask_for_lore_folder():
    lore_folder = input('Please input the filepath you would like to generate the lore files into:')
    return lore_folder


def ask_for_persona():
    persona = input('Please input the persona type you would like to have:')
    return persona


def ask_for_file_path():
    file_path = input('Please input the filepath of the individual file you would like to load:')
    return file_path


def generate_story(ai_gen, lore_folder, persona_type, file_path):
    # TODO Add in generate story function
    return 'Arguments given: ' + 'AI type: ' + ai_gen + ', lorefolder: ' + lore_folder + ', persona type: ' + persona_type + ', filepath: ' + file_path + '.' # noqa
