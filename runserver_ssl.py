import os
import ssl
from django.core.servers.basehttp import get_internal_wsgi_application
from wsgiref.simple_server import make_server
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler as WSGIStaticFilesHandler


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# Crear aplicación WSGI
application = get_internal_wsgi_application()

# Activar handler de archivos estáticos si estamos en modo desarrollo
if settings.DEBUG:
    application = WSGIStaticFilesHandler(application)

# Contexto SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='api/ssl/cert.crt', keyfile='api/ssl/key.key')

# Servidor WSGI con SSL
httpd = make_server('localhost', 8000, application)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Servidor HTTPS corriendo en https://localhost:8000/")
httpd.serve_forever()