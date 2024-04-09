from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Crea un autorizador dummy para gestionar los usuarios y sus contraseñas
    authorizer = DummyAuthorizer()

    # Agrega un usuario con nombre 'admin' y contraseña 'password' con todos los permisos
    authorizer.add_user("admin", "password", "C:/Users/lidia rodriguez/Desktop/", perm="elradfmw")

    # Crea el manejador del servidor FTP
    handler = FTPHandler
    handler.authorizer = authorizer

    # Establece la dirección IP y el puerto del servidor FTP
    address = ("192.168.0.177", 2121)

    # Crea el servidor FTP con el manejador y la dirección especificada
    server = FTPServer(address, handler)

    # Inicia el servidor FTP
    server.serve_forever()

if __name__ == "__main__":
    main()
