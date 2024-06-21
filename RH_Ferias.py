import tkinter as tk  
import os

# Cria a janela do aplicativo e da o nome do titulo da janela !!!
root = tk.Tk()
root.title('Gestão Férias RH')

# Define o caminho do ícone usando a pasta do projeto !!!
path_project = os.path.dirname(os.path.abspath(__file__))
path_icon = os.path.join(path_project, 'Images\minitab.ico')
root.iconbitmap(path_icon)

# Dimensões da janela do aplicativo definidas abaixo !!!
height_app = 550
width_app = 1000

# Resolução do sistema operacional que está operando !!!
height_screen = root.winfo_screenheight()
width_screen = root.winfo_screenwidth()

# Posicionamento da janela em relação a resolução do computador !!!
posx = width_screen/2-width_app/2
posy = height_screen/2-height_app/2

# Definindo Geometry da janela do app e não deixando redimensionável a janela pelo usuário !!!
root.geometry("%dx%d+%d+%d" % (width_app, height_app, posx, posy))
root.resizable(False,False)

root.mainloop()
