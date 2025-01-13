import user
import menu
import json
from prettytable import PrettyTable

if __name__ == '__main__':
    u = user.User()
    m = menu.Menu()
    m.get_menu(u.ID)