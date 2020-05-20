from colorama import init
from colorama import Fore, Style
from colors import colors

init()


class JuicyTag:
    """ Main class """
    other = ""

    def __init__(self, project, creator, color_inside="CYAN", color_frame="CYAN", date=None, email=None, ):

        # Let's make it juicy
        print(Style.BRIGHT)
        if (len(project) <= 30) and (len(creator) <= 40) and (color_inside.upper() in colors) \
                and (color_frame.upper() in colors):
            self.project = project
            self.creator = creator
            self.color_inside = color_inside
            self.color_frame = color_frame
            self.date = date
            self.email = email

            if self.color_inside.upper() == "RED":
                color_inside = Fore.RED
            elif self.color_inside.upper() == "MAGENTA":
                color_inside = Fore.MAGENTA
            elif self.color_inside.upper() == "BLUE":
                color_inside = Fore.BLUE
            elif self.color_inside.upper() == "YELLOW":
                color_inside = Fore.YELLOW
            elif self.color_inside.upper() == "GREEN":
                color_inside = Fore.GREEN
            elif self.color_inside.upper() == "CYAN":
                color_inside = Fore.CYAN
            elif self.color_inside.upper() == "BLACK":
                color_inside = Fore.BLACK
            elif self.color_inside.upper() == "WHITE":
                color_inside = Fore.WHITE

            if self.color_frame.upper() == "RED":
                color_frame = Fore.RED
            elif self.color_frame.upper() == "MAGENTA":
                color_frame = Fore.MAGENTA
            elif self.color_frame.upper() == "BLUE":
                color_frame = Fore.BLUE
            elif self.color_frame.upper() == "YELLOW":
                color_frame = Fore.YELLOW
            elif self.color_frame.upper() == "GREEN":
                color_frame = Fore.GREEN
            elif self.color_frame.upper() == "CYAN":
                color_frame = Fore.CYAN
            elif self.color_frame.upper() == "BLACK":
                color_frame = Fore.BLACK
            elif self.color_frame.upper() == "WHITE":
                color_frame = Fore.WHITE

            frame_length: int = 16 if len(self.creator) <= 10 else 25

            # Printing the tag
            print(color_frame + "* " * frame_length)
            print(color_frame + "*     " + color_inside + self.project + color_frame +
                  ' ' * (frame_length * 2 - 8 - len(self.project)) + '*')
            if len(self.creator) <= 20:
                print(color_frame + "*     " + color_inside + f"Created by {self.creator}" + color_frame +
                      ' ' * (frame_length * 2 - 19 - len(self.creator)) + '*')
            else:
                print(color_frame + "*     " + color_inside + "          Created by" + color_frame +
                      "                      *\n" + color_frame + '*' +
                      color_inside + f"     {self.creator}" + ' ' * (frame_length*2 - 8 - len(self.creator)) +
                      color_frame + '*')

            if self.email is not None:
                print(color_frame + "*     " + color_inside + self.email + color_frame +
                      ' ' * (frame_length * 2 - 8 - len(self.email)) + '*')
            if self.date is not None:
                print(color_frame + "*     " + color_inside + self.date + color_frame +
                      ' ' * (frame_length * 2 - 8 - len(self.date)) + '*')
            print(color_frame + "* " * frame_length)
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


test = JuicyTag("Juicy Tag b1.0", "Chernishov Daniil", "cyan", "red", "May 20 2020")
test1 = JuicyTag("Juicy Tag b1.0", "Chernishoff", 'magenta', "yellow")
