import tkinter as tk
import pandas as pd
from datetime import datetime, date


class Pessoa:
    # essa é a data atual, a mesma depende do sistema da sua máquina para estar correta
    data_hoje = datetime.today().date()

    def __init__(self, nome, dia, mes, ano):
        self.nome = nome
        self._data_nasc = date(ano, mes, dia)

        # se esse dia ja estiver passado neste ano, vai somar ano atual + 1
        self._dia_do_aniversario = date(datetime.today().year, mes, dia)
        if self._dia_do_aniversario < self.data_hoje:
            self._dia_do_aniversario = date(datetime.today().year+1, mes, dia)

# DIZ QUANTOS DIAS SE PASSOU DESDE ESSA DATA
    def dias_vivo(self):
        self.dias = self.data_hoje - self._data_nasc
        return self.dias

# DIZ QUANTOS ANOS SE PASSOU DESDE ESSA DATA
    def idade(self):
        dias_vivos = self.dias_vivo().days
        self.idade_atual = dias_vivos // 365
        return f'{self.idade_atual} anos'

# FUNÇÃO PARA CALCULAR DIAS QUE FALTAM ATE O PRÓXIMO ANO A SER COMPLETADO
    def dias_aniversario(self):
        self.faltam = self._dia_do_aniversario - self.data_hoje
        return self.faltam.days

# DIZ QUANTOS MESES SE PASSARAM DESDE ESSA DATA
    def meses_vivo(self):
        self.meses = self.dias_vivo().days // 30
        return self.meses

# DIZ QUANTAS SEMANAS SE PASSARAM DESDE ESSA DATA
    def semanas_vivo(self):
        self.semanas = self.dias_vivo().days // 7
        return self.semanas

# DIZ QUANTAS HORAS SE PASSARAM DESDE ESSA DATA
    def horas_vivo(self):
        self.horas = self.dias_vivo().days * 24
        return self.horas


dicio = {
    'NOME': [],
    'DATA': [],
    'RESULTADO': [],
}
nome_arquivo = []


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

# CRIAÇÃO DOS WIDGETS PARA MANIPULAÇÃO DOS DADOS
    def create_widgets(self):
        self.nome_label = tk.Label(self, text="Nome")
        self.nome_label.pack()

        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        self.dia_label = tk.Label(self, text="Dia")
        self.dia_label.pack()

        self.dia_entry = tk.Entry(self)
        self.dia_entry.pack()

        self.mes_label = tk.Label(self, text="Mês")
        self.mes_label.pack()

        self.mes_entry = tk.Entry(self)
        self.mes_entry.pack()

        self.ano_label = tk.Label(self, text="Ano")
        self.ano_label.pack()

        self.ano_entry = tk.Entry(self)
        self.ano_entry.pack()

        self.text_cond = tk.Label(self, text="""Qual informação você deseja?
(1 - Anos, 2 - Meses, 3 - Semanas, 4 - Dias, 5 - Horas)""")
        self.text_cond.pack()

        self.text_cond_entry = tk.Entry(self)
        self.text_cond_entry.pack()

        self.arquivo_label = tk.Label(
            self, text="Qual o nome do arquivo que voce deseja criar, quando fechar a página?")
        self.arquivo_label.pack()

        self.arquivo_entry = tk.Entry(self)
        self.arquivo_entry.pack()

        self.button = tk.Button(self)
        self.button["text"] = "Calcular"
        self.button["command"] = self.calculate
        self.button.pack()

        self.resultado = tk.Label(self, text='RESULTADO:')
        self.resultado.pack()
        self.final = tk.Label(self, text='')


# FUNÇÃO QUE SERÁ REALIZADA APÓS CLICAR NO BOTÃO CALCULAR


    def calculate(self):
        nome = self.nome_entry.get()
        dia = int(self.dia_entry.get())
        mes = int(self.mes_entry.get())
        ano = int(self.ano_entry.get())
        condic = int(self.text_cond_entry.get())
        dicio['NOME'].append(nome)
        dicio['DATA'].append(f'{dia}-{mes}-{ano}')
        nome_arquivo.append(self.arquivo_entry.get())


# CHAMADA DA CLASSE PESSOA E CONDICIONAIS PARA EXIBUÇÃO DE VALOR
        pessoa = Pessoa(nome, dia, mes, ano)

        if condic == 1:
            self.final.destroy()

            self.final = tk.Label(self, text=f'{pessoa.idade()}')
            self.final.pack()
            print(f'{pessoa.idade()}')
            dicio['RESULTADO'].append(self.final.cget('text'))
        elif condic == 2:
            self.final.destroy()

            self.final = tk.Label(self, text=f'{pessoa.meses_vivo()} meses')
            self.final.pack()
            print(f'{pessoa.meses_vivo()} meses')
            dicio['RESULTADO'].append(self.final.cget('text'))
        elif condic == 3:
            self.final.destroy()

            self.final = tk.Label(
                self, text=f'{pessoa.semanas_vivo()} semanas')
            self.final.pack()
            print(f'{pessoa.semanas_vivo()} semanas')
            dicio['RESULTADO'].append(self.final.cget('text'))
        elif condic == 4:
            self.final.destroy()

            self.final = tk.Label(self, text=f'{pessoa.dias_vivo().days} dias')
            self.final.pack()
            print(f'{pessoa.dias_vivo().days} dias')
            dicio['RESULTADO'].append(self.final.cget('text'))
        elif condic == 5:
            self.final.destroy()

            self.final = tk.Label(self, text=f'{pessoa.horas_vivo()} horas')
            self.final.pack()
            print(f'{pessoa.horas_vivo()} horas')
            dicio['RESULTADO'].append(self.final.cget('text'))
        else:
            print(f'{condic} não é um valor válido')


root = tk.Tk()
app = Application(master=root)
app.mainloop()


df = pd.DataFrame(dicio)
print(df)

df.to_csv(f'{nome_arquivo[-1]}.csv')
