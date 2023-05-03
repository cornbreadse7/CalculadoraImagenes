import PySimpleGUI as sg
import sys
import cv2
import operaciones
import numpy as np
import webbrowser
import os


def main():
    sg.theme('DarkGray15')

    menu_def = [['Archivo', ['Abrir Imagenes','Abrir Imagen 1','Abrir Imagen 2', 'Guardar','Vaciar Imagenes','Vaciar Imagen 1','Vaciar Imagen 2', 'Salir']],
                ['Operaciones', ['Aritmeticas', ['Suma','Resta','Multiplicacion'], 'Logicas', ['AND','OR','XOR','NAND'],'Umbral (Imagen 1)']],
                ['Ayuda', ['Acerca de', 'Codigo Fuente']], ]

    layoutCol = [
        [sg.Image(filename='', key='-IMAGE1-')],
        [sg.Image(filename='', key='-IMAGE2-')],
        [sg.Image(filename='', key='-IMAGE3-')],
    ]

    layout = [
        [sg.Text('Operaciones con Imagenes en Python', size=(200, 1), justification='center')],
        [sg.Menu(menu_def)],
        [sg.Column([layoutCol[0]]),sg.Column([layoutCol[1]]),sg.Column([layoutCol[2]])]
    ]

    imagen1 = np.ones((450,450))
    imagen2 = np.ones((450,450))
    imagenr = np.ones((450,450))
    window = sg.Window('Operaciones con Imagenes en Python', layout, location=(800, 700))

    while True:
        event, values = window.read(timeout=20)

        if event == 'Salir' or event == sg.WIN_CLOSED:
            sg.popup('Gracias por usar el programa')
            break

        if event == 'Umbral (Imagen 1)':
            imagen1 = operaciones.umbral(imagen1)
            sg.popup('Umbral de Imagen 1')

        if event == 'Suma':
            imagenr = operaciones.suma(imagen1, imagen2)
            sg.popup('Suma de Imagenes')

        if event == 'Resta':
            imagenr = operaciones.resta(imagen1, imagen2)
            sg.popup('Resta de Imagenes')

        if event == 'Multiplicacion':
            imagenr = operaciones.multiplicacion(imagen1, imagen2)
            sg.popup('Multiplicacion de Imagenes')

        if event == 'AND':
            imagenr = operaciones.opAND(imagen1, imagen2)
            sg.popup('Operacion AND')
            

        if event == 'OR':
            imagenr = operaciones.opOR(imagen1, imagen2)
            sg.popup('Operacion OR')
            

        if event == 'XOR':
            imagenr = operaciones.opXOR(imagen1, imagen2)
            sg.popup('Operacion NOT')
            

        if event == 'NAND':
            imagenr = operaciones.opNAND(imagen1,imagen2)
            sg.popup('Operacion NAND')
            

        if event == 'Acerca de':
            sg.popup('Aplicacion de Filtro de Imagenes con Python', 'Version 1.3', 'Cornbreadse7')

        if event == 'Codigo Fuente':
            webbrowser.open('https://github.com/cornbreadse7/MiPrimerEditorenPython', new=1)

        if event == 'Vaciar Imagen 1':
            imagen1 = np.ones((500, 500))
            sg.popup('Imagen vaciada')

        if event == 'Vaciar Imagen 2':
            imagen2 = np.ones((500, 500))
            sg.popup('Imagen vaciada')

        if event == 'Vaciar Imagenes':
            imagen1 = np.ones((500, 500))
            imagen2 = np.ones((500, 500))
            sg.popup('Imagenes vaciadas')

        if event == 'Abrir Imagenes':
            imagenr = np.ones((450,450))
            filename = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Abrir Imagen 1 (PNG, JPG)')
            if not filename:
                sg.popup("Por favor, escoja una imagen")
            else:
                imagen1 = cv2.imread(filename)  # Validar que el nombre de archivo no este en blanco
                # imagen = cv2.imread("images/004.png",0)    
            filename = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Abrir Imagen 2 (PNG, JPG)')
            if not filename:
                sg.popup("Por favor, escoja una imagen")
            else:
                imagen2 = cv2.imread(filename)  # Validar que el nombre de archivo no este en blanco
                # imagen = cv2.imread("images/004.png",0)

        if event == 'Abrir Imagen 1':
            imagenr = np.ones((450,450))
            filename = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Abrir Imagen 1 (PNG, JPG)')
            if not filename:
                sg.popup("Por favor, escoja una imagen")
            else:
                imagen1 = cv2.imread(filename)  # Validar que el nombre de archivo no este en blanco
                # imagen = cv2.imread("images/004.png",0)

        if event == 'Abrir Imagen 2':
            imagenr = np.ones((450,450))
            filename = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Abrir Imagen 2 (PNG, JPG)')
            if not filename:
                sg.popup("Por favor, escoja una imagen")
            else:
                imagen2 = cv2.imread(filename)  # Validar que el nombre de archivo no este en blanco
                # imagen = cv2.imread("images/004.png",0)

        if event == 'Guardar':
            filename = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Guardar Fotografia (PNG) to save to', save_as=True)
            if not filename:
                sg.popup("Por favor, escoja una ruta")
            else:
                # ruta = sg.popup_get_folder(title='Guardar Fotografia', message="Carpeta destino")
                cv2.imwrite(filename, imagenr)

        imgbytes1 = cv2.imencode('.png', imagen1)[1].tobytes()
        window['-IMAGE1-'].update(data=imgbytes1)
        imgbytes2 = cv2.imencode('.png', imagen2)[1].tobytes()
        window['-IMAGE2-'].update(data=imgbytes2)
        imgbytesr = cv2.imencode('.png', imagenr)[1].tobytes()
        window['-IMAGE3-'].update(data=imgbytesr)


    window.close()


main()
