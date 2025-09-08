import tkinter as tk

from tkinter import messagebox

import hjson

telinha = f'''
Tipo 1 : Bloco; Uma parede para defesa \n\n
Tipo 2 : Torre; Uma torre, voçe pode escolher algumas modificaçoes a mais \n\n
Tipo 3 : Crafter; Um bloco que Craft itens , obs: o nome do item de entrada \n\n tem que ser identico a o do arquivo EX: Argon.hjson , entao tem que ser um item com nome Argon \n\n
Tipo 4 : Transporte; Aqui o mais mesmo e colocar as sprites do meio de transporte \n\n 
Tipo 5 : Item; Aqui voçe escolhe o tipo de item e suas info, se ele explode ou nao etc.
'''

def criar_janela_item():

    #Criaçao da janela
    item = tk.Tk()
    item.title("Item")


    #Fim da janela
    item.mainloop()
    #--------------------------------------------------------------- Fim

def criar_janela_bloco():
    def volta():
        #Funçao para chamar a janela principal
        bloco.destroy()
        janela_pri()
        #--------------------------------------------------------------- Fim
    
    def criar_bloco():
        #Funçao para transformar as info em arquivo

        #Coletar informaçoes dos entry
        nome = nome_bloco.get().strip()
        descricao = descri_bloco.get().strip()
        tamanho = tam_bloco.get().strip()
        vida = vida_bloco.get().strip()
        descoberto = descoberto_bloco.get().strip()
        nome_arquivo = nome_arquivo_entry.get().strip()
        reque = reque_bloco.get().split(',')
        
        #Verificaçao para verse todos os campos estao completos
        if not nome or not descricao or not tamanho.isdigit() or not vida.isdigit() or not nome_arquivo:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
            return
        if not nome_arquivo.endswith(".hjson"):
            nome_arquivo += ".hjson"
     
        #Salvar o arquivo em hjson
        try:
            with open(nome_arquivo,'w') as arq:
                arq.write(f'name: "{nome}"\n')
                arq.write(f'type: "Wall"\n')
                arq.write(f'description: "{descricao}"\n')
                arq.write(f'health: {vida}\n')
                arq.write(f'size {tamanho}\n')
                lista_requisitos = reque_bloco.get().split(',')
                arq.write('requirements: [\n')
                for req in lista_requisitos:
                    arq.write(f'  {req.strip()}\n')
                arq.write(f']\n')
                arq.write(f'category: "defense"\n')
                arq.write(f'research: "{descoberto}"')

                # hjson.dump(dados,arq,ensure_ascii=False)
            messagebox.showinfo("Sucesso", f"Arquivo '{nome_arquivo}' salvo com sucesso.")

        except Exception as e:
            messagebox.showerror("Erro ao salvar",str(e)) 
        #--------------------------------------------------------------- Fim

   
    #------------------ criar janela
    bloco = tk.Tk()
    bloco.title('Criar arquivo')
    #------------------

    #------------------ Opcoes, Entradas
    #Opcoes
    texto_func = tk.Label(bloco,text="Aqui estao as opçoes e suas funçoes")

    #nome da torre
    texto_nome = tk.Label(bloco,text='Digite o nome do Seu bloco')
    nome_bloco = tk.Entry(bloco,width=30)

    #descriçao do bloco
    texto_descri = tk.Label(bloco,text='Descriçao do bloco')
    descri_bloco = tk.Entry(bloco,width=30)

    #tamanho
    texto_tam = tk.Label(bloco,text='Tamanha, 1=1x1 , 2=2x2')
    tam_bloco = tk.Entry(bloco,width=5)   

    #vida do bloco
    texto_vida = tk.Label(bloco,text='Vida do bloco')
    vida_bloco = tk.Entry(bloco,width=7)    

    #Oq precisa pra criar item
    texto_reque = tk.Label(bloco,text='Itens para criar o item , digite como \n no exemplo | copper/12 , lead/12 | digite o nome do arquivo do \n  item e a quantidade separada por barra(,) e os itens necessarios por virgula(,)')
    reque_bloco = tk.Entry(bloco,width=50)

    #O item vai ser desbloqueado a pos qual item?
    texto_descoberto = tk.Label(bloco,text='Desbloquear a pos qual item')
    descoberto_bloco = tk.Entry(bloco,width=7)

    #Nome do arquivo
    texto_arq = tk.Label(bloco,text='Nome do arquivo (.hjson)')
    nome_arquivo_entry = tk.Entry(bloco,width=30)
    #------------------

    #------------------ Botoes
    #Botao de voltar para pagina
    voltar_pri = tk.Button(bloco,text='Voltar para pagina principal',command=volta)

    #Botao criar arquivo
    criar_item = tk.Button(bloco,text='Criar',command=criar_bloco)
    #------------------

    
    #------------------ Posiçao dos elementos
    #Posicionar opcoes , entradas

    texto_func.grid(column=0,row=0, columnspan=2, pady=10)

    #nome bloco
    texto_nome.grid(column=0,row=1, sticky='w', padx=5, pady=5)
    nome_bloco.grid(column=1,row=1, padx=5, pady=5)
    
    #descriçao bloco
    texto_descri.grid(column=0,row=2, sticky='w', padx=5, pady=5)
    descri_bloco.grid(column=1,row=2, padx=5, pady=5)
    
    #tamanho bloco
    texto_tam.grid(column=0,row=3, sticky='w', padx=5, pady=5)
    tam_bloco.grid(column=1,row=3, padx=5, pady=5)
    
    #vida bloco
    texto_vida.grid(column=0,row=4, sticky='w', padx=5, pady=5)
    vida_bloco.grid(column=1,row=4, padx=5, pady=5)

    #descoberto bloco
    texto_descoberto.grid(column=0,row=5,sticky='w',padx=5,pady=5)
    descoberto_bloco.grid(column=1,row=5,padx=5,pady=5)

    #reque bloco
    texto_reque.grid(column=0,row=6,sticky='w',padx=5,pady=5)
    reque_bloco.grid(column=1,row=6,padx=5,pady=5)

    #arquivo bloco
    texto_arq.grid(column=0, row=7,stick='w',padx=5,pady=5)
    nome_arquivo_entry.grid(column=1,row=7,padx=5,pady=5)

    #Botao voltar e criar
    criar_item.grid(column=0,row=8, columnspan=2, pady=10)
    voltar_pri.grid(column=1,row=8,columnspan=2,padx=130,pady=20)
    #------------------
  
    #Fim do janela
    bloco.mainloop()
    #--------------------------------------------------------------- Fim

def janela_pri():
    #Funçao de Fechar o progama
    #------------------
    def fechar_pri():
        janela.destroy()
    #------------------

    #Escolher tipo de Item
    #------------------
    def tipo():

        try:
            tip = int(entrada.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")
            return

        if tip == 1:
            janela.destroy()
            criar_janela_bloco()
        elif tip == 5:
            janela.destroy()
            criar_janela_item()
        else:
            messagebox.showinfo("Info", "Tipo de bloco ainda não implementado.")
        #------------------

    #janela
    #------------------
    janela = tk.Tk()
    janela.title('Janela Principal')
    #------------------

    #Texto e Entrada
    #------------------
    escolha_texto = tk.Label(janela,text='Digite o numero para criar o tipo de bloco')
    tela = tk.Label(janela,text=telinha)

    entrada = tk.Entry(janela)

    enviar = tk.Button(janela,text='Enviar o tipo',command=tipo)

    sair = tk.Button(janela,text="Fechar",command=fechar_pri)
    #------------------

    #Posicionar itens
    #------------------
    sair.grid(column=0,row=4)
    escolha_texto.grid(column=0,row=0)
    entrada.grid(column=0,row=1)
    enviar.grid(column=0,row=2)
    tela.grid(column=0,row=3)
    #------------------

    janela.mainloop()

janela_pri()