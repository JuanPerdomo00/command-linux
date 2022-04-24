# proyecto preguntar comando de linux y mostrar su utilidad
# este proyecto se me ocurrio gracias a un video de Pelado Nerd
# este sofware trabaja bajo la GNU GENERAL PUBLIC LICENSE version 3
#
# Copyright (c) 2022 Jakepy Perdomo <j4kyjak3@protonmail.com>.
# creado por: JuanPerdomo00 <jakepy>

from main import Color



# 1
pwd = f"""
    {Color.azul}[*] {Color.rojo}pwd: {Color.blanco}Usa el comando pwd para encontrar la ruta del directorio (carpeta) 
    de trabajo actual en el que te encuentras. 
    El comando devolverá una ruta absoluta (completa), 
    que es básicamente una ruta de todos los directorios que comienzan con una barra diagonal (/) 
    Un ejemplo de una ruta absoluta es /home/nombredeusuario. {Color.reset}
"""

# 2
cd = f"""
    {Color.azul}[*] {Color.rojo}cd: {Color.blanco}Para navegar por los archivos y directorios de Linux, usa el comando cd. 
    Te pedirá la ruta completa o el nombre del directorio, 
    dependiendo del directorio de trabajo actual en el que te encuentres.

    cd .. (con dos puntos) para ir un directorio hacia arriba
    cd    para ir directamente a la carpeta de inicio
    cd -  (con un guión) para ir al directorio anterior {Color.reset}
"""
# 3
ls = f"""
    {Color.azul}[*] {Color.rojo}ls: {Color.blanco}se usa para ver el contenido de un directorio. Por defecto,
    este comando mostrará el contenido de tu directorio de trabajo actual.
    Si deseas ver el contenido de otros directorios, escribe ls y luego la ruta
    al comando ls se le pueden poner parametros ej:

    {Color.verde}ls -a  {Color.blanco}muestra archivos o directorios ocultos
    {Color.verde}ls -l  {Color.blanco}lo muestra en una lista
    {Color.verde}ls -h  {Color.blanco}muesta el peso del archivo en una forma que entienda el humano
    {Color.verde}ls -R  {Color.blanco}también listará todos los archivos en los subdirectorios {Color.reset}
"""

# 4
cat = f"""
    {Color.azul}[*] {Color.rojo}cat:  {Color.blanco}(abreviatura de concatenate, en inglés) es uno de los comandos más utilizados en Linux. 
    Se utiliza para listar el contenido de un archivo en la salida estándar (sdout). 
    Para ejecutar este comando, escribe cat seguido del nombre del archivo y su extensión. 
    Por ejemplo: cat archivo.txt.

    cat > nombredearchivo crea un nuevo archivo.
    cat nombredearchivo1 nombredearchivo2>nombredearchivo3 une dos archivos (1 y 2) y 
    almacena la salida de ellos en un nuevo archivo (3) {Color.reset}
"""

# 5
cp = f"""
    {Color.azul}[*] {Color.rojo}cp: {Color.blanco}Usa el comando cp para copiar archivos del directorio actual a un directorio diferente.
    Por ejemplo, 
    el comando cp escenario.jpg /home/nombredeusuario/imagenes 
    crearía una copia de escenario.jpg (desde tu directorio actual) en el directorio de Imagenes.{Color.reset}
"""

# 6
mv = f"""
    {Color.azul}[*] {Color.rojo}mv: {Color.blanco}El uso principal del comando mv es mover archivos, 
        aunque también se puede usar para cambiar el nombre de los archivos.
        Los argumentos en mv son similares al comando cp. Debes escribir mv, 
        el nombre del archivo y el directorio destino. 
        Por ejemplo: mv archivo.txt /home/nombredeusuario/Documentos.
        Para cambiar el nombre de los archivos, el comando de Linux es mv nombreviejo.ext nombrenuevo.ext {Color.reset}
"""

# 7
mkdir = f"""
    {Color.azul}[*] {Color.rojo}mkdir: {Color.blanco}Usa el comando mkdir para crear un nuevo directorio: 
    si escribes mkdir Musica, creará un directorio llamado Musica.

    También hay comandos adicionales de mkdir:

    Para generar un nuevo directorio dentro de otro directorio, 
    usa este comando básico de Linux mkdir Musica/Nuevoarchivo
    Usa la opción p (padres) para crear un directorio entre dos directorios existentes.
    Por ejemplo, mkdir -p Musica/2020/Nuevoarchivo creará el nuevo archivo «2020». {Color.reset}
"""

# 8
rmdir = f"""
    {Color.azul}[*] {Color.rojo}rmdir: {Color.blanco}Si necesitas eliminar un directorio, usa el comando rmdir. 
    Sin embargo, rmdir solo te permite eliminar directorios vacíos. {Color.reset}
"""

# 9
rm = f"""
    {Color.azul}[*] {Color.rojo}rm: {Color.blanco}El comando rm se usa para eliminar directorios y el contenido dentro de ellos. 
    Si solo deseas eliminar el directorio, como alternativa a rmdir, usa rm -r.

    {Color.rojo}[!] Nota: Ten mucho cuidado con este comando y verifica en qué directorio te encuentras. 
    Este comando elimina todo y no se puede deshacer.[!] {Color.reset}
"""

# 10
touch = f"""
    {Color.azul}[*] {Color.rojo}touch: {Color.blanco}El comando touch te permite crear un nuevo archivo en blanco a través de la línea de comando de Linux.
    Como ejemplo, ingresa touch /home/nombredeusuario/Documentos/Web.html
    para crear un archivo HTML titulado Web en el directorio Documentos. {Color.reset}
"""


# 11
locate = f"""
    {Color.azul}[*] {Color.rojo}locate: {Color.blanco}Puedes usar este comando para localizar un archivo,
    al igual que el comando de búsqueda en Windows. Además, 
    el uso del argumento -i junto con este comando hará que no distinga entre mayúsculas y minúsculas, 
    por lo que puedes buscar un archivo incluso si no recuerdas su nombre exacto.

    Para buscar un archivo que contenga dos o más palabras, usa un asterisco (*). Por ejemplo, 
    el comando locate -i escuela*nota buscará cualquier archivo que contenga la palabra «escuela» y «nota», 
    ya sea en mayúsculas o minúsculas.{Color.reset}
"""

# 12
find = f"""
    {Color.azul}[*] {Color.rojo}find: {Color.blanco}Similar al comando locate, usando find también buscas archivos y directorios. 
    La diferencia es que usas el comando find para ubicar archivos dentro de un directorio dado.
    Como ejemplo, el comando find /home/ -name notas.txt buscará un archivo llamado notas.txt 
    dentro del directorio de inicio y sus subdirectorios.

    Otras variaciones al usar find son:

    Para buscar archivos en el directorio actual:{Color.verde} find . -name notas.txt
    {Color.blanco}Para buscar directorios: {Color.verde}find / -type d -name notes.txt {Color.reset}
"""


# 13
grep = f"""
    {Color.azul}[*] {Color.rojo}grep: {Color.blanco}Otro comando básico de Linux que sin duda es útil para el uso diario es grep. 
    Te permite buscar a través de todo el texto en un archivo dado.

    Para ilustrar, grep azul notepad.txt buscará la palabra azul en el archivo del bloc de notas. 
    Las líneas que contienen la palabra buscada se mostrarán.{Color.reset}
"""

# 14
sudo = f"""
    {Color.azul}[*] {Color.rojo}sudo: {Color.blanco}Abreviatura de «SuperUser Do» (SuperUsuario hace), este comando te permite realizar tareas 
    que requieren permisos administrativos o raíz. Sin embargo, no es aconsejable usar este comando para el uso diario, 
    ya que podría ser fácil que ocurra un error si haces algo mal.{Color.reset}
"""

# 15
tar = f"""
    {Color.azul}[*] {Color.rojo}tar: {Color.blanco}El comando tar es el comando más utilizado para guardar múltiples archivos en un tarball, 
    un formato de archivo de Linux común que es similar al formato zip, con compresión opcional.

    Este comando es bastante complejo con una larga lista de funciones, como agregar nuevos archivos a un archivo existente, 
    enumerar el contenido de un archivo, extraer el contenido de un archivo y muchos más. {Color.reset}
"""

# 16
chmod = f"""
    {Color.azul}[*] {Color.rojo}chmod: {Color.blanco}chmod es otro comando de Linux, utilizado para cambiar los permisos de lectura, 
    escritura y ejecución de archivos y directorios. 

    Como este comando es bastante complicado, puedes leer el tutorial completo (en inglés) 
    aqui: {Color.magenta}https://www.computerhope.com/unix/uchmod.htm {Color.reset}
"""

# 17
ping = f"""
    {Color.azul}[*] {Color.rojo}ping: {Color.blanco}Usa el comando ping para verificar tu estado de conectividad a un servidor. 
    Por ejemplo, simplemente ingresando ping google.com, 
    el comando verificará si puedes conectarte a Google y también medirá el tiempo de respuesta.{Color.reset}
"""

# 18
wget = f"""
    {Color.azul}[*] {Color.rojo}wget: {Color.blanco}La línea de comandos de Linux es muy útil: incluso puedes descargar archivos de Internet con la ayuda del comando wget. 
    Para hacerlo, simplemente escribe wget seguido del enlace de descarga.{Color.reset}
"""

# 19
uname = f"""
    {Color.azul}[*] {Color.rojo}uname: {Color.blanco}El comando uname, abreviatura de Nombre de Unix, imprimirá información detallada sobre tu sistema Linux, 
    como el nombre de la máquina, el sistema operativo, el núcleo, etc.{Color.reset}
"""

# 20
top = f"""
    {Color.azul}[*] {Color.rojo}top: {Color.blanco}Como un terminal equivalente al Administrador de tareas en Windows,
    el comando top mostrará una lista de los procesos en ejecución y la cantidad de CPU que utiliza cada proceso.
    Es muy útil monitorear el uso de los recursos del sistema, especialmente para saber qué proceso debe terminarse porque consume demasiados recursos.{Color.reset}
"""
