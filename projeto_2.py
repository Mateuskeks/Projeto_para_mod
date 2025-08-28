import tkinter as tk
from tkinter import messagebox
import hjson 

telinha = f'''
+++++++++++++
   __  __  
    --       
+++++++++++++
'''


def criar_janela_bloco():
    
    def criar_bloco():

        print('chamou')
        
        nome = nome_bloco.get().strip()
        descricao = descri_bloco.get().strip()
        tamanho = tam_bloco.get().strip()
        vida = vida_bloco.get().strip()
        nome_arquivo = nome_arquivo_entry.get().strip()
        
        if not nome or not descricao or not tamanho.isdigit() or not vida.isdigit() or not nome_arquivo:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
            return
        if not nome_arquivo.endswith(".hjson"):
            nome_arquivo += ".hjson"

        dados = {
            "type": "Wall",
            "name": nome,
            "localizedName": f"{descricao}",
            "description": descricao,
            "category": "defense",
            "category": "defense",
            "size": int(tamanho),
            "health": int(vida),
            "requirements": ["copper/10"],
            "buildCostMultiplier": 1.0
        }
        print(dados)
        try:
            with open(nome_arquivo,'w') as arq:

                hjson.dump(dados,arq,ensure_ascii=False)
            messagebox.showinfo("Sucesso", f"Arquivo '{nome_arquivo}' salvo com sucesso.")

        except Exception as e:
            messagebox.showerror("Erro ao salvar",str(e))        
    #criar janela
    bloco = tk.Tk()
    bloco.title('Criar arquivo')
    
    #texto opçoes
    texto_1 = tk.Label(bloco,text="Aqui estao as opçoes e suas funçoes")


    #nome da torre
    texto_2 = tk.Label(bloco,text='Digite o nome do Seu bloco')
    nome_bloco = tk.Entry(bloco,width=30)

    #descriçao do bloco
    texto_3 = tk.Label(bloco,text='Descriçao do bloco')
    descri_bloco = tk.Entry(bloco,width=30)

    #tamanho
    texto_4 = tk.Label(bloco,text='Tamanha, 1=1x1 , 2=2x2')
    tam_bloco = tk.Entry(bloco,width=5)   

    #vida do bloco
    texto_5 = tk.Label(bloco,text='Vida do bloco')
    vida_bloco = tk.Entry(bloco,width=7)    

    #Nome do arquivo
    texto_6 = tk.Label(bloco,text='Nome do arquivo (.hjson)')
    nome_arquivo_entry = tk.Entry(bloco,width=30)

    voltar_pri = tk.Button(bloco,text='Voltar para pagina principal',command=janela_pri)


    criar_item = tk.Button(bloco,text='Criar',command=criar_bloco)

    #Posiçao dos elementos
     #opçoes e ex
    texto_1.grid(column=0,row=0, columnspan=2, pady=10)
     #nome bloco
    texto_2.grid(column=0,row=1, sticky='w', padx=5, pady=5)
    nome_bloco.grid(column=1,row=1, padx=5, pady=5)
    
    texto_3.grid(column=0,row=2, sticky='w', padx=5, pady=5)
    descri_bloco.grid(column=1,row=2, padx=5, pady=5)
    
    texto_4.grid(column=0,row=3, sticky='w', padx=5, pady=5)
    tam_bloco.grid(column=1,row=3, padx=5, pady=5)
    
    texto_5.grid(column=0,row=4, sticky='w', padx=5, pady=5)
    vida_bloco.grid(column=1,row=4, padx=5, pady=5)

    texto_6.grid(column=0, row=5,stick='w',padx=5,pady=5)
    nome_arquivo_entry.grid(column=1,row=5,padx=5,pady=5)

    criar_item.grid(column=0,row=6, columnspan=2, pady=10)
    voltar_pri.grid(column=1,row=6,columnspan=2,padx=130,pady=20)
    bloco.mainloop()



def janela_pri():
    def tipo():

        try:
            tip = int(entrada.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")
            return

        if tip == 1:
            janela.destroy()
            criar_janela_bloco()
        else:
            messagebox.showinfo("Info", "Tipo de bloco ainda não implementado.")

        
    janela = tk.Tk()
    janela.title('Janela Principal')
    criar_janela_bloco.destroy()

    escolha_texto = tk.Label(janela,text='Digite o numero para criar o tipo de bloco')
    tela = tk.Label(janela,text=telinha)
    entrada = tk.Entry(janela)
    
    enviar = tk.Button(janela,text='Enviar o tipo',command=tipo)

    escolha_texto.grid(column=0,row=0)
    entrada.grid(column=0,row=1)
    enviar.grid(column=0,row=2)
    tela.grid(column=0,row=3)

    janela.mainloop()

janela_pri()