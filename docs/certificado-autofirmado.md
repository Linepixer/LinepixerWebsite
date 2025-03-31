# PASO 1: Generar key.key
openssl genpkey -algorithm RSA -out key.key

# PASO 2: Crear archivo openssl.cnf con el siguiente contenido

[ req ]
default_bits        = 2048
distinguished_name  = req_distinguished_name
req_extensions      = v3_req
x509_extensions     = v3_req
prompt              = no

[ req_distinguished_name ]
countryName         = AR
stateOrProvinceName = Buenos Aires
localityName        = Bernal
organizationName    = Linepixer Developments
organizationalUnitName = Web Development Section
commonName          = Linepixer Website

[ v3_req ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = localhost
IP.1 = 127.0.0.1

# PASO 3: Generar la solicitud de firmado csr.csr con el archivo de configuracion openssl.cnf
openssl req -new -key key.key -out csr.csr -config openssl.cnf

# PASO 4: Firmar certificado con el csr.csr mas el archivo de configuracion del openssl.cnf
openssl x509 -req -in csr.csr -signkey key.key -out cert.crt -days 365 -sha256 -extensions v3_req -extfile openssl.cnf

# PASO 6: Colocar los archivos key.key y cert.crf en la ubicacion correcta
Mover los archivos mencionados a la posicion ~/Carpeta del proyecto/linepixerwebsite/ssl

# PASO 7: Limpiar archivos restantes
Los archivos crt.crt y openssl.cnf ya se pueden borrar

# PASO 5: Importar el certificado a windows

1. Abrir la herramienta "Administrar certificados de equipo" que se puede buscar en el menu inicio
2. A la izquierda, sobre la columna de carpetas buscar "Entidades de certificación raíz de confianza"
3. Dar Click derecho > Todas las tareas > Importar
4. Seguir los pasos del asistente para importar el certificado

# PASO 6: Listo, probar que el certificado funcione bien previo reiniciar el navegador