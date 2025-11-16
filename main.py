#from auth.py import *

#from crud.py import *

#from games.py import *

import auth
from menu import menu
import crud

game_over = False
flag_login = False
flag_menu = False
flag_crud = False

while not game_over: 
    while not flag_login:
        flag_login = auth.menu(flag_login)
    while not flag_menu:
        #menu() definir el archivo menu con funciones
        pass



