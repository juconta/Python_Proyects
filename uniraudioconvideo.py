"""
========================================================
UNIR AUDIO CON VIDEO USANDO MOVIEPY
========================================================

Descripción:
Este script toma un archivo de video (.mp4) y un archivo
de audio (.mp3), los combina y genera un nuevo video
con el audio incorporado.

Requisitos:
- Python instalado
- Librería MoviePy
- FFmpeg configurado en el sistema

Instalación de MoviePy:
    pip install moviepy==1.0.3

Ejecución:
    python unir_audio_video.py

Autor: Juan
========================================================
"""

# ======================================================
# IMPORTACIÓN DE LIBRERÍAS
# ======================================================

"""
Importamos las clases necesarias de MoviePy:

- VideoFileClip:
    Permite cargar y manipular videos.

- AudioFileClip:
    Permite cargar y manipular archivos de audio.
"""

from moviepy import VideoFileClip, AudioFileClip


# ======================================================
# DEFINICIÓN DE RUTAS DE ARCHIVOS
# ======================================================

"""
Definimos los nombres de los archivos:

- video_path:
    Ruta del video original.

- audio_path:
    Ruta del audio que se agregará al video.

- salida_path:
    Nombre del archivo final generado.
"""

video_path = "clase.mp4"
audio_path = "clase.mp3"
salida_path = "Clase_completo.mp4"


# ======================================================
# CARGA DEL VIDEO
# ======================================================

"""
Cargamos el archivo de video utilizando VideoFileClip.
"""

video = VideoFileClip(video_path)


# ======================================================
# CARGA DEL AUDIO
# ======================================================

"""
Cargamos el archivo de audio utilizando AudioFileClip.
"""

audio = AudioFileClip(audio_path)


# ======================================================
# UNIÓN DEL AUDIO CON EL VIDEO
# ======================================================

"""
Asignamos el audio cargado al video original.

El método with_audio() agrega el audio al video sin reemplazarlo.
"""

video_final = video.with_audio(audio)


# ======================================================
# EXPORTACIÓN DEL VIDEO FINAL
# ======================================================

"""
Guardamos el nuevo video en formato MP4.

Parámetros utilizados:

- codec="libx264"
    Codec de video ampliamente compatible.

- audio_codec="aac"
    Codec de audio recomendado para MP4.
"""

video_final.write_videofile(
    salida_path,
    codec="libx264",
    audio_codec="aac"
)


# ======================================================
# MENSAJE FINAL
# ======================================================

"""
Mostramos un mensaje indicando que el proceso
finalizó correctamente.
"""

print("✅ Video generado correctamente:", salida_path)