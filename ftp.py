# recuerden cambiar tu-ip por su ip real ejemplo 192.168.0.1
# tambien cambien tu-usuario por el usuario de su laptop o computadora
# tambien para que les funcione tienen que activar el Port Forwarding en la administracion de su Router
# tambien hay que instalar la libreria necesaria con el siguiente comando 'pip install pyftpdlib'
# para mas ayuda manda msg por instagram} ezemtz.2222

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Crea un autorizador dummy para gestionar los usuarios y sus contraseñas
    authorizer = DummyAuthorizer()

    # Agrega un usuario y contraseña con todos los permisos
    authorizer.add_user("admin", "password", "C:/Users/tu-usuario/Desktop/", perm="elradfmw")

    # Crea el manejador del servidor FTP
    handler = FTPHandler
    handler.authorizer = authorizer

    # Establece la dirección IP y el puerto del servidor FTP
    address = ("tu-ip", 2121)

    # Crea el servidor FTP con el manejador y la dirección especificada
    server = FTPServer(address, handler)

    # Inicia el servidor FTP
    server.serve_forever()

if __name__ == "__main__":
    main()
