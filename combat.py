import pyautogui  # Para capturar y realizar clics
import pygetwindow as gw  # Para listar ventanas
import time  # Para pausar entre clics
import random  # Para generar tiempos de espera aleatorios

detener_accion = False  # Variable global para controlar el bucle

def detener_bucle():
    """Detiene el bucle de clics"""
    global detener_accion
    detener_accion = True

def realizar_clics_en_imagenes_en_todas_ventanas(imagenes):
    """Realiza clics en las imágenes dadas en todas las ventanas activas de RuneLite."""
    
    global detener_accion
    detener_accion = False  # Reiniciar la variable para cada ejecución
    
    ventanas = gw.getAllTitles()  # Obtener todas las ventanas activas
    ventanas_juego = [ventana for ventana in ventanas if 'RuneLite' in ventana]  # Filtrar ventanas que contienen 'RuneLite'
    
    if not ventanas_juego:
        print("No se encontraron ventanas de RuneLite activas.")
        return
    
    while not detener_accion:
        for ventana_nombre in ventanas_juego:
            print(f"Cambiando a la ventana: {ventana_nombre}")
            ventana = gw.getWindowsWithTitle(ventana_nombre)[0]  # Obtiene la ventana por su título
            ventana.activate()  # Activa la ventana para que reciba las acciones
            
            for imagen in imagenes:
                print(f"Buscando la imagen: {imagen}")
                ubicacion = pyautogui.locateCenterOnScreen(imagen, confidence=0.8)
                if ubicacion is not None:
                    print(f"Imagen encontrada en {ubicacion}, haciendo clic...")
                    pyautogui.click(ubicacion)
                    tiempo_espera = random.uniform(10, 12)  # Esperar entre 10 y 12 segundos
                    print(f"Esperando {tiempo_espera:.2f} segundos antes de la siguiente acción...")
                    time.sleep(tiempo_espera)
                else:
                    print(f"No se encontró la imagen: {imagen} en la ventana: {ventana_nombre}")
        
    print("Acciones completadas en todas las ventanas.")


def buscar_y_hacer_clic_en_npc():
    """Busca una lista de imágenes de NPCs y hace clic en la primera que encuentre."""
    
    global detener_accion
    detener_accion = False  # Reiniciar la variable para cada ejecución
    
    lista_imagenes_npc = [
        'captura/chicken_1.png',
        'captura/chicken_2.png',
        'captura/chicken_3.png',
        'captura/chicken_4.png',
        'captura/chicken_5.png',
        'captura/chicken_6.png'
    ]
    
    while not detener_accion:
        for imagen in lista_imagenes_npc:
            print(f"Buscando la imagen del NPC: {imagen}")
            ubicacion = pyautogui.locateCenterOnScreen(imagen, confidence=0.8)
            if ubicacion is not None:
                print(f"NPC encontrado en {ubicacion}, haciendo clic...")
                pyautogui.click(ubicacion)
                tiempo_espera = random.uniform(10, 12)  # Esperar entre 10 y 12 segundos
                print(f"Esperando {tiempo_espera:.2f} segundos antes de la siguiente acción...")
                time.sleep(tiempo_espera)
                break  # Sale del bucle de imágenes y continúa el bucle general
        else:
            print("No se encontró ningún NPC de la lista.")
    
    print("Acciones completadas para la lista de NPCs.")
