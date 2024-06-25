from customtkinter import *

class Conversor:
    def __init__(self):
        self.valor = 0

    # Converte os cm em m, km ou vice-versa
    def cm_m_km(self, medida_1, medida_2, valor):
        self.valor = valor
        match (medida_1, medida_2):
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
                return self.valor

    def mg_g_kg(self, medida_1, medida_2, valor):
         self.valor = valor
         match (medida_1, medida_2):
             case ('mg', 'g'):
              return self.valor / 1000
             case ('mg', 'kg'):
                 return self.valor / 1000000
             case ('g', 'mg'):
                 return self.valor * 1000
             case ('g', 'kg'):
                 return self.valor / 1000
             case ('kg', 'mg'):
                 return self.valor * 1000000
             case ('kg', 'g'):
                 return self.valor * 1000
             case _:
                 print("Conversão não definida.")
                 return None
    # Método estático para ser usado como comando no botão
    @staticmethod
    def converter():
        valor = float(caixa_valor.get())
        medida_1 = lista_converter_de.get()
        medida_2 = lista_converter_para.get()
        resultado = instancia.cm_m_km(medida_1, medida_2, valor)
       

        if medida_2 == 'cm':
            texto_resultado.configure(text=f"Resultado: {resultado} Centímetro(s)")
        elif medida_2 == 'm':
            texto_resultado.configure(text=f"Resultado: {resultado} metro(s)")
        elif medida_2 == 'km':
            texto_resultado.configure(text=f"Resultado: {resultado} Quilômetros")

# Instância da classe Conversor
instancia = Conversor()

# CTk para criar a janela principal
janela = CTk()
janela.title("Conversor")
janela.geometry("500x300")

# Caixa para entrada dos valores
CTkLabel(janela, text="Valor:").place(x=20, y=20)
caixa_valor = CTkEntry(janela, placeholder_text="Digite um número:", width=200)
caixa_valor.place(x=140, y=20)

# Botão para converter
botao_converter = CTkButton(janela, text="Converter", command=Conversor.converter)
botao_converter.place(x=350, y=20)

# Lista com as medidas, converter de (tamanho/comprimento):
CTkLabel(janela, text="De:").place(x=20, y=70)
lista_converter_de = CTkComboBox(janela, values=['cm', 'm', 'km'], width=200)
lista_converter_de.place(x=140, y=70)

# Lista com as medidas, converter para:
CTkLabel(janela, text="Para:").place(x=20, y=120)
lista_converter_para = CTkComboBox(janela, values=['cm', 'm', 'km'], width=200)
lista_converter_para.place(x=140, y=120)

# TXT Resultado
texto_resultado = CTkLabel(janela, text="Resultado:")
texto_resultado.place(x=20, y=170)

janela.mainloop()
