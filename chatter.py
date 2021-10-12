#!/usr/bin/ptyhon3

# Juan Duque <3428@holbertonschool.com>

"""Declaration of the libraries"""

from math import perm
import sys
from typing import IO
import limits
import random
import os
import socket
import subprocess
import json
import base64
import uuid


"""Import libraries property with class of colors"""
bcol = __import__('colors').bcol


"""New instance  of the person"""


class Persona:

    def __init__(self):
        self.id = ""

        self.name = ""
        self.user = ""
        self.mail = ""
        self.message = ""
        self.passw = ""

    def print_user(self, user, mail, name):
        print(bcol.RED + "\tYour id user is : {}".format(self.id) + bcol.NOCOLOR)
        print(bcol.RED + "\tYour user is : {}".format(user) + bcol.NOCOLOR)
        print(bcol.RED + "\tYour mail is : {}".format(mail) + bcol.NOCOLOR)
        print(bcol.RED + "\tYour name is : {}".format(name) + bcol.NOCOLOR)

    def print_user2(self, user, mail, name):
        print(bcol.RED + "\t\t\t\t\tYour id user is : {}".format(self.id) + bcol.NOCOLOR)
        print(bcol.RED + "\t\t\t\t\tYour user is : {}".format(user) + bcol.NOCOLOR)
        print(bcol.RED + "\t\t\t\t\tYour mail is : {}".format(mail) + bcol.NOCOLOR)
        print(bcol.RED + "\t\t\t\t\tYour name is : {}".format(name) + bcol.NOCOLOR)

    def send_(self, user, message, mail):
        msg = Message()
        msg.ip = "192.168.1.1"
        msg.message = message
        msg.to = mail
        """os.system("clear")
        banner()
        print(bcol.GREEN + " \n\t\t[!] Se envio el mensaje\n\n" + bcol.NOCOLOR)
        os.system("sleep 0.5")
        os.system("clear")
        banner()"""

    def rcv(self, user, message, mail):
        print(bcol.BLUE + "\n\n\t\tHaz recibido un mensage" + bcol.YELLOW +
              "  [!] " + bcol.NOCOLOR)
        print(bcol.YELLOW + bcol.BOLD + "\n\t\t\t\t\t De " +
              bcol.NOCOLOR + "{}".format(user))
        print(bcol.YELLOW + bcol.BOLD + "\t\t\t\t\t <== Message\n" +
              bcol.NOCOLOR + bcol.GREEN + "\t\t\t\t\t {}".format(message) + bcol.NOCOLOR)

    def rcv2(self, user, message, mail):
        print(bcol.YELLOW + "\n\n\t[!] " + bcol.BLUE +
              " Haz recibido un mensage" + bcol.NOCOLOR)
        print(bcol.YELLOW + bcol.BOLD + "\t\nDe " +
              bcol.NOCOLOR + "{}".format(user))
        print(bcol.YELLOW + bcol.BOLD + "Message ==> \n" +
              bcol.NOCOLOR + bcol.BLUE + "\t{}".format(message) + bcol.NOCOLOR)


"""Create new objet call server"""


class new_server:

    def __init__(self) -> None:
        self.name = ""
        self.port = None
        self.domain = ""
        pass

    def new_server(self, name, domain, port):
        print(bcol.BOLD + bcol.GREEN + "[!] " + bcol.NOCOLOR + bcol.YELLOW +
              "New Server i have create" + bcol.NOCOLOR)
        print(bcol.RED + "\tYour server name is : " +
              bcol.NOCOLOR + " {}".format(name))
        print(bcol.RED + "\tYour server domain is : " +
              bcol.NOCOLOR + " {}".format(domain))
        print(bcol.RED + "\tYour server port listening : " +
              bcol.NOCOLOR + " {}\n".format(port) + bcol.NOCOLOR)


class Message():
    id_con = ""
    server = ""
    usr_1 = ""
    usr_2 = ""

    def __init__(self):
        self.message = ""
        self.to = ""
        self.ip = ""

    def rcv_(self, usr_1_rcv, usr_2):
        self.usr_1_rcv = usr_1_rcv


server = new_server()
server.domain = "prueba1.com"
server.name = socket.gethostname()
server.port = 5050


def banner():
    print(" ____     __                __    __                   ")
    print(bcol.BLUE + "/\  _`\  /\ \              /\ \__/\ \__                ")
    print(bcol.RED + "\ \ \/\_\\\ \ \___      __  \ \ ,_\ \ ,_\    __   _ __  ")
    print(bcol.YELLOW + " \ \ \/ _/_\ \  _ ` / '__`\ \ \ \/\ \ \/  /'__`\/\`'__\\")
    print(bcol.RED + "  \ \ \L\ \\\ \ \ \ \/\ \L\.\_\ \ \_\ \ \_/\  __/\ \ \/ ")
    print(bcol.BLUE + "   \ \____/ \ \_\ \_\ \__/.\_\\\ \__\\\ \__\ \____\\\ \_\ ")
    print(bcol.RED + "    \/___/   \/_/\/_/\/__/\/_/ \/__/ \/__/\/____/ \/_/ ")
    print(bcol.NOCOLOR + "                                                       ")


"""Create new GUI for chat with friend"""


def new_serv():

    loading = read_json()
    new_server_data(loading)

    server.new_server(server.name, server.domain, server.port)


def new_chat():

    usr1 = Persona()
    usr2 = Persona()
    db = read_json()
    print(bcol.YELLOW + "[!]" + bcol.GREEN +
          "Ingresa Estos datos para iniciar el chat" + bcol.NOCOLOR)
    user = input("Ingresa tu usuario: ")
    friend = input("Ingresa el nombre de tu amigo: ")

    usr1.id = db["users"][user]['ID']
    usr1.user = bcol.BLUE + db["users"][user]['usr'] + bcol.NOCOLOR
    usr1.name = bcol.BLUE + db["users"][user]['name'] + bcol.NOCOLOR
    usr1.mail = bcol.BLUE + db["users"][user]['mail'] + bcol.NOCOLOR

    print("")
    print(bcol.BOLD + "\t{} ".format(usr1.user))
    print(bcol.NOCOLOR)

    usr1.print_user(usr1.user, usr1.mail, usr1.name)

    usr2.id = db["users"][friend]['ID']
    usr2.user = bcol.BLUE + db["users"][friend]['usr'] + bcol.NOCOLOR
    usr2.name = bcol.BLUE + db["users"][friend]['name'] + bcol.NOCOLOR
    usr2.mail = bcol.BLUE + db["users"][friend]['mail'] + bcol.NOCOLOR

    print("")
    print(bcol.BOLD + "\t\t\t\t\t\t\t{} ".format(usr2.user))
    print(bcol.NOCOLOR)
    usr2.print_user2(usr2.user, usr2.mail, usr2.name)

    while(1):
        print(bcol.BLUE)
        usr1.message = input("\t\n>>1 : ")
        usr1.send_(usr1.user, usr1.message, usr2.mail)
        usr2.rcv(usr1.user, usr1.message, usr1.mail)
        print(bcol.NOCOLOR)

        print(bcol.GREEN)
        usr2.message = input("\t\t\t>>>>2 : ")
        usr2.send_(usr2.user, usr2.message, usr1.mail)
        usr1.rcv2(usr2.user, usr2.message, usr2.mail)
        print(bcol.NOCOLOR)


"""Esta funcion sera utilizada
        para leer el archivo json"""


def read_json():
    f = open("db.json", )
    r = f.read()
    loading = json.loads(r)
    f.close()
    return loading


""" Writing new data in """


def _write(loading):
    file = open("db.json", "w")
    file.write(loading)
    file.close()


"""Charger all data in database file json"""


def new_usr_data(loading):
    print(bcol.GREEN + "[*]" + bcol.YELLOW +
          " Creando nuevo usuario" + bcol.NOCOLOR)
    usr = input("\tIngresa tu nuevo usuario: ")
    confirm_user(usr)

    loading["users"][usr] = {"ID": "", "usr": "",
                             "name": "", "mail": "", "passw": ""}
    appen_data(usr, loading)
    dum = json.dumps(loading, indent=4)
    _write(dum)
    return 0


def new_server_data(loading):
    print(bcol.GREEN + "[*]" + bcol.YELLOW +
          " Creando nuevo Servicio" + bcol.NOCOLOR)
    usr = socket.gethostname()
    confirm_server(usr)

    loading["Servers"][usr] = {
        "ID": "",
        "HASH_SESSION": "",
        "IP": "",
        "PORT_LISTENING": "",
        "ZONA": "",
        "NAME_USR": "",
        "NAME_SERVER": "",
        "DOMAIN": "",
        "USRS_CONECTED": {
                "users": {
                    "IP": "",
                    "USR": "",
                    "FRIEND": "",
                    "HASH_SESSION": ""
                },
            "State_con": {
                    "Status": 0
                    }
        }}

    appen_data_Server(usr, loading)
    dum = json.dumps(loading, indent=4)
    _write(dum)
    return 0


""" Insert values in table data of users"""


def appen_data(user, loading):
    loading["users"][user]['ID'] = random.randint(0, 10000)
    print(bcol.BLUE)
    loading["users"][user]['usr'] = user
    loading["users"][user]['name'] = input("ingresa tu nombre: ")
    loading["users"][user]['mail'] = input("ingresa tu mail: ")
    loading["users"][user]['passw'] = input("ingresa tu password: ")
    print(bcol.NOCOLOR)
    return loading


def appen_data_Server(user, loading):

    loading["Servers"][user]['ID'] = random.randint(0, 10000)
    print(bcol.BLUE)
    loading["Servers"][user]['HASH_SESSION'] = uuid.uuid4().hex
    loading["Servers"][user]['NAME_USR'] = server.name
    loading["Servers"][user]['IP'] = socket.gethostbyname(user)
    loading["Servers"][user]['ZONA'] = ""
    loading["Servers"][user]['NAME_SERVER'] = socket.gethostname()
    loading["Servers"][user]['PORT_LISTENING'] = server.port
    loading["Servers"][user]['DOMAIN'] = server.domain
    print(bcol.NOCOLOR)
    return loading


""" Esta funcion creara un nuevo usuario si
    se necesitara"""


def new_user():
    loading = read_json()
    new_usr_data(loading)


""" Esta funcion se encargara de leer nuestro archivo
    Que contiene la data que se crea al momento de
    Crear el usuario """


def confirm_user(usuario):
    fd = read_json()
    load = json.dumps(fd)
    print("El usuario es: {}".format(usuario))
    print(str(usuario) in load)

    if usuario in load is True:
        print("El usuario Existe")


def confirm_server(usuario):
    fd = read_json()
    load = json.dumps(fd)
    print("El usuario es: {}".format(usuario))
    print(str(usuario) in load)

    if usuario in load is True:
        print("El Server Existe")


"""Esta funcion Establece la salida de
    Error al iniciar nuestro KEYBOARDINTERRUPT
    con Ctrl_C"""


def _errnos_1():
    os.system("clear")
    print(bcol.YELLOW + "Conexion Interrumpida" + bcol.NOCOLOR)
    print(bcol.YELLOW + "\t\n [!]" + bcol.RED +
          " Saliendo del Programa .... " + bcol.NOCOLOR + bcol.NOCOLOR)
    sys.exit(1)


if __name__ == "__main__":

    """ Este es nuestro try exceptions
    Que nos ayuda con el manejo de errores
    y maneja el keyboard interrup Ctrl_C"""

    try:
        """ Funciones Listas
        raise KeyboardInterrupt
         """
        banner()
        new_serv()
        new_user()
        new_chat()

    except KeyboardInterrupt:
        _errnos_1()
