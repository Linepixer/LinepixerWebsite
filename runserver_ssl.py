import os
from django.core.management import execute_from_command_line
from django.core.servers.basehttp import get_internal_wsgi_application
import ssl
from wsgiref.simple_server import make_server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# Configurar el contexto SSL con la librería estándar de Python
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='api/ssl/cert.crt', keyfile='api/ssl/key.key')

# Aplicación Django
application = get_internal_wsgi_application()

# Crear servidor WSGI
httpd = make_server('localhost', 8000, application)

# Aplicar SSL al servidor
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

# Iniciar el servidor en HTTPS
print("Servidor HTTPS corriendo en https://localhost:8000/")
httpd.serve_forever()