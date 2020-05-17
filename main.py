from colorama import init
from colorama import Fore, Back, Style
from colors import colors

init()


class JuicyTag:
    """ Main class"""
    # Default settings
    project = ""
    creator = ""
    email = "None"
    color_inside = "CYAN"
    color_frame = "CYAN"
    date = ""
    other = ""

    def __init__(self, project, creator, color_inside=color_inside,
                 color_frame=color_frame, date=None, email=None,):
        # Let's make it juicy
        print(Style.BRIGHT)
        if (len(creator) <= 50) and (color_inside.upper() in colors) and (color_frame.upper() in colors):
            self.creator = creator
            self.color_inside = color_inside
            self.color_frame = color_frame
            self.date = date
            self.email = email

            if color_inside.upper() == "RED":
                color_inside = Fore.RED
            elif color_inside.upper() == "MAGENTA":
                color_inside = Fore.MAGENTA
            elif color_inside.upper() == "BLUE":
                color_inside = Fore.BLUE
            elif color_inside.upper() == "YELLOW":
                color_inside = Fore.YELLOW
            elif color_inside.upper() == "GREEN":
                color_inside = Fore.GREEN
            elif color_inside.upper() == "CYAN":
                color_inside = Fore.CYAN
            elif color_inside.upper() == "BLACK":
                color_inside = Fore.BLACK
            elif color_inside.upper() == "WHITE":
                color_inside = Fore.WHITE

            if color_frame.upper() == "RED":
                color_frame = Fore.RED
            elif color_frame.upper() == "MAGENTA":
                color_frame = Fore.MAGENTA
            elif color_frame.upper() == "BLUE":
                color_frame = Fore.BLUE
            elif color_frame.upper() == "YELLOW":
                color_frame = Fore.YELLOW
            elif color_frame.upper() == "GREEN":
                color_frame = Fore.GREEN
            elif color_frame.upper() == "CYAN":
                color_frame = Fore.CYAN
            elif color_frame.upper() == "BLACK":
                color_frame = Fore.BLACK
            elif color_frame.upper() == "WHITE":
                color_frame = Fore.WHITE

           #  longest_object = max(key=len)

            print(color_frame + "* "*(len(self.creator) + 15))
            print(color_frame + "*     " + str(((21 + len(self.creator))
                                               // len(project))) + project + "     *")
            print(color_frame + "*     Created by " + self.creator + "     *")
            print('*     the1337pocan@mail.ru')
            print('*     May 16 2020')

            print(Style.RESET_ALL)

        else:
            raise ValueError

    def add_creator(self, added_creator):
        pass

    def add_other(self, new_other):
        self.other = new_other
        print(f"Other: {self.other}")

    def random_tag(self):
        pass


class Info:
    """
    Displays information about author
    """
    def __init__(self):
        print("Made for fun!")


test = JuicyTag("WTW Bot3", "Chernishov Daniil", "rEd","rEd")

test1 = JuicyTag("Something", "vova", 'cYAn',"CyaN")



