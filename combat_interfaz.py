import tkinter as tk
from combat import buscar_y_hacer_clic_en_npc  # Importar la función desde combat.py
import subprocess  # Para abrir main.py

def retornar_al_main(ventana):
    """Cierra la interfaz actual y abre main.py"""
    ventana.destroy()  # Cierra la ventana actual
    subprocess.Popen(['python', 'main.py'])  # Abre la interfaz principal de main.py

def main():
    """Crea la interfaz de Auto Combat"""
    
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Auto Combat")
    ventana.geometry("400x400")  # Ajustar el tamaño de la ventana
    
    # Título principal
    titulo = tk.Label(ventana, text="Auto Combat", font=("Arial", 16))
    titulo.pack(pady=10)  # Espaciado superior
    
    # Etiqueta de "Seleccione una opción"
    label_seleccione = tk.Label(ventana, text="Seleccione una opción", font=("Arial", 12))
    label_seleccione.pack(pady=10)  # Espaciado superior
    
    # Botón "Kill Chicken" para realizar la prueba
    boton_kill_chicken = tk.Button(ventana, text="Kill Chicken", command=lambda: buscar_y_hacer_clic_en_npc([ 
        'captura/chicken_1.png',
        'captura/chicken_2.png',
        'captura/chicken_3.png',
        'captura/chicken_4.png',
        'captura/chicken_5.png',
        'captura/chicken_6.png'
    ]), bg="lightcoral", font=("Arial", 12))
    boton_kill_chicken.pack(pady=10)  
    
    # Contenedor para los botones Retornar y Salir
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(side="bottom", pady=20)  # Posiciona los botones en la parte inferior
    
    # Botón "Retornar" para volver al main
    boton_retornar = tk.Button(frame_botones, text="Retornar", command=lambda: retornar_al_main(ventana), bg="lightblue", font=("Arial", 12))
    boton_retornar.pack(side="left", padx=10)  # Botón a la izquierda con espacio entre ellos
    
    # Botón "Salir" para cerrar todo el programa
    boton_salir = tk.Button(frame_botones, text="Salir", command=ventana.destroy, bg="red", font=("Arial", 12))
    boton_salir.pack(side="right", padx=10)  # Botón a la derecha con espacio entre ellos
    
    # Inicia el loop principal de la interfaz
    ventana.mainloop()

# Ejecutar la aplicación principal
if __name__ == "__main__":
    main()
