import tkinter as tk

class ToDoList:
    
    def __init__(self, valor_inicio):
        self.toDo = valor_inicio
        self.toDo.title('Hello Word')
        #Frame do NIVEL DE PRIORIDADE
        self.toDo.geometry("1140x500")
        frame_principal = tk.Frame(self.toDo)
        frame_principal.pack()
        label1 = tk.Label(frame_principal, text='NIVEL DE PRIORIDADE', bg='black', foreground="white", padx=70, pady=20)
        label1.pack()
        #Frame para as prioridade 1,2 e 3
        frame_prioridade = tk.Frame(self.toDo)
        frame_prioridade.pack(padx=100, pady=30)
        #Deixando os niveis de prioridade lado a lado
        label2 = tk.Label(frame_prioridade, text='FAZER PRIMEIRO', bg='black', foreground="white", padx=70, pady=20)
        label2.pack(side=tk.LEFT, padx=50)
        label3 = tk.Label(frame_prioridade, text='O QUANTO ANTES', bg='black', foreground="white", padx=70, pady=20)
        label3.pack(side=tk.LEFT, padx=50)
        label4 = tk.Label(frame_prioridade, text='QUANDO POSSIVEL', bg='black', foreground="white", padx=70, pady=20)
        label4.pack(side=tk.LEFT, padx=50)
        #Frames de inserir as tabelas prioridade
        frame_texto = tk.Frame(self.toDo)
        frame_texto.pack()
        #Inserir os valores
        
        
root = tk.Tk()
ToDoList(root)
root.mainloop()