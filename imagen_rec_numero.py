import cv2  # Para manipulación de imágenes
import pytesseract  # OCR (reconocimiento óptico de caracteres)
from PIL import Image  # Para manipular imágenes

# Configurar la ruta de tesseract si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extraer_numeros_desde_imagen(ruta_imagen):
    """Extrae los números de una imagen y devuelve los valores separados."""
    
    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen)
    
    # Preprocesar la imagen (escala de grises y binarización)
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    _, imagen_binaria = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY_INV)  # Binarización (blanco y negro)
    
    # Aumentar el tamaño de la imagen para que sea más fácil de leer para Tesseract
    imagen_ampliada = cv2.resize(imagen_binaria, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    # Opciones de configuración para Tesseract (aquí limitamos la búsqueda a números y barras "/")
    configuracion_tesseract = '--psm 6 -c tessedit_char_whitelist=0123456789/'
    
    # Extraer texto de la imagen
    texto_extraido = pytesseract.image_to_string(imagen_ampliada, config=configuracion_tesseract)
    texto_limpio = texto_extraido.strip()  # Eliminar espacios en blanco
    print(f"Texto extraído: {texto_limpio}")
    
    # Validar si el texto coincide con el formato esperado (por ejemplo, '2/3')
    if '/' in texto_limpio:
        try:
            vida_actual, vida_maxima = map(int, texto_limpio.split('/'))
            print(f"Vida actual: {vida_actual}, Vida máxima: {vida_maxima}")
            return vida_actual, vida_maxima
        except ValueError:
            print("No se pudo convertir los valores a números.")
            return None, None
    else:
        print("No se detectó la barra de vida correctamente.")
        return None, None
