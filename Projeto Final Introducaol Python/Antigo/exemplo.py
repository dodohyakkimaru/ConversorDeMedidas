from tkinter import *
from tkinter import ttk

class Conversor:
    def __init__(self):
        self.unidade_medida = None
        self.unidade_para = None
        self.valor = 0

    def configurar_unidades(self, unidade_medida, unidade_para):
        self.unidade_medida = unidade_medida
        self.unidade_para = unidade_para

    def configurar_valor(self, valor):
        self.valor = valor

    def converter(self):
        match (self.unidade_medida, self.unidade_para):
            case ('cm', 'm'):
                return self.valor / 100
            case ('cm', 'km'):
                return self.valor / 100000
            case ('m', 'cm'):
                return self.valor * 100
            case ('m', 'km'):
                return self.valor / 1000
            case ('km', 'cm'):
                return self.valor * 100000
            case ('km', 'm'):
                return self.valor * 1000
            case _:
                return "Erro, conversão não suportada entre as medidas fornecidas!"

def converter_valor():
    try:
        valor = float(entrada_valor.get())
        unidade_origem = lista_converter_origem.get()
        unidade_destino = lista_converter_destino.get()
        conversor.configurar_unidades(unidade_origem, unidade_destino)
        conversor.configurar_valor(valor)
        resultado = conversor.converter()
        texto_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        texto_resultado.config(text="Por favor, insira um número válido.")
    except Exception as e:
        texto_resultado.config(text=str(e))

janela = Tk()
janela.title("Conversor")
janela.geometry("400x200")

un_medida = ['cm', 'm', 'km', 'g', 'kg', 'mg', 'segundos', 'minutos', 'horas', 'dias', 'semanas', 'meses', 'anos']

conversor = Conversor()

Label(janela, text="Valor:").pack()
entrada_valor = Entry(janela)
entrada_valor.pack()

Label(janela, text="De:").pack()
lista_converter_origem = ttk.Combobox(janela, values=un_medida)
lista_converter_origem.pack()

Label(janela, text="Para:").pack()
lista_converter_destino = ttk.Combobox(janela, values=un_medida)
lista_converter_destino.pack()

Button(janela, text="Converter", command=converter_valor).pack()

texto_resultado = Label(janela, text="")
texto_resultado.pack()

janela.mainloop()
