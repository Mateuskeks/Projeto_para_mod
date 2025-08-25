import tkinter as tk
import hjson

def bloco():
    
    def criar_bloco():
        print('chamou')
        nome = nome_bloco.get()
        descricao = descri_bloco.get()
        tamanho = tam_bloco.get()
        vida = vida_bloco.get()
        estrutura = f'''
        type: Wall
        name: {nome}
        description:{descricao}
        size:{tamanho}
        health:{vida}
        '''
        print(estrutura)
        
        nome_arquivo = str(input('Digite o nome do arquivo com .hjson no final'))

        # Define os dados como um dicionário
        dados = {
            "type": "B",
            "name": f'{nome}',
            "localizedName": f'"{descricao}"',
            "description": f'"{descricao}"',
            "category": 'defense',
            "size": f'{tamanho}',
            "requirements": [ "copper/10" ],
            "buildCostMultiplier": 1.0
        }

        # Salva em um arquivo .hjson
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            hjson.dump(dados, arquivo, ensure_ascii=False)

    
    #criar janela
    bloco = tk.Tk()
    bloco.title('Criar arquivo')
    
    #texto opçoes
    texto_1 = tk.Label(bloco,text="Aqui estao as opçoes e suas funçoes")


    #nome da torre
    texto_2 = tk.Label(bloco,text='Digite o nome do Seu bloco')
    nome_bloco = tk.Entry(bloco)
    #descriçao do bloco
    texto_3 = tk.Label(bloco,text='Descriçao do bloco')
    descri_bloco = tk.Entry(bloco)
    #tamanho
    texto_4 = tk.Label(bloco,text='Tamanha, 1=1x1 , 2=2x2')
    tam_bloco = tk.Entry(bloco)   
    #vida do bloco
    texto_5 = tk.Label(bloco,text='Vida do bloco')
    vida_bloco = tk.Entry(bloco)    

    criar_item = tk.Button(bloco,text='Criar',command=criar_bloco)

    #Posiçao dos elementos
     #opçoes e ex
    texto_1.grid(column=0,row=0)
     #nome bloco
    texto_2.grid(column=1,row=1)
    nome_bloco.grid(column=0,row=1)

    texto_3.grid(column=1,row=2)
    descri_bloco.grid(column=0,row=2)

    texto_4.grid(column=1,row=3)
    tam_bloco.grid(column=0,row=3)

    texto_5.grid(column=1,row=4)
    vida_bloco.grid(column=0,row=4)

    criar_item.grid(column=0,row=5)
    bloco.mainloop()
