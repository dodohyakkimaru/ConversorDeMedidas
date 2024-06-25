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

    # Converte os mg em g, kg ou vice-versa
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
                return self.valor

    # Converte as unidades de tempo simplificadas
    def s_m_h_d(self, medida_1, medida_2, valor):
        self.valor = valor
        match (medida_1, medida_2):
            case ('s', 'min'):
                return self.valor / 60
            case ('s', 'h'):
                return self.valor / 3600
            case ('s', 'd'):
                return self.valor / 86400
            case ('min', 's'):
                return self.valor * 60
            case ('min', 'h'):
                return self.valor / 60
            case ('min', 'd'):
                return self.valor / 1440
            case ('h', 's'):
                return self.valor * 3600
            case ('h', 'min'):
                return self.valor * 60
            case ('h', 'd'):
                return self.valor / 24
            case ('d', 's'):
                return self.valor * 86400
            case ('d', 'min'):
                return self.valor * 1440
            case ('d', 'h'):
                return self.valor * 24
            case _:
                return self.valor

    @staticmethod
    def converter():
        # Verifica se o campo de valor está vazio
        if not caixa_valor.get():
            texto_resultado.configure(text="Por favor, insira um valor.")

        valor = float(caixa_valor.get())
        medida_1 = lista_converter_de.get()
        medida_2 = lista_converter_para.get()

        # Lista das unidades de medidas
        lista_medidas = {'Comprimento': [
            'cm', 'm', 'km'], 'Massa': ['mg', 'g', 'kg'], 'Tempo': ['s', 'min', 'h', 'd']}

        # Verifica se as medidas são de comprimento ou massa
        if medida_1 in lista_medidas['Comprimento'] and medida_2 in lista_medidas['Comprimento']:
            resultado = instancia.cm_m_km(medida_1, medida_2, valor)
        elif medida_1 in lista_medidas['Massa'] and medida_2 in lista_medidas['Massa']:
            resultado = instancia.mg_g_kg(medida_1, medida_2, valor)
        elif medida_1 in lista_medidas['Tempo'] and medida_2 in lista_medidas['Tempo']:
            resultado = instancia.s_m_h_d(medida_1, medida_2, valor)
        else:
            # Mostra mensagem de erro para conversão não suportada
            texto_resultado.configure(text="Conversão não suportada.")

        # Atualiza o texto do resultado com base na medida de saída selecionada
        match medida_2:
            case 'cm':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado}  centímetro(s)")
            case 'm':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado}  metro(s)")
            case 'km':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado}  quilômetro(s)")
            case 'mg':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado}  miligrama(s)")
            case 'g':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado}  grama(s)")
            case 'kg':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado} quilograma(s)")
            case 's':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado} segundo(s)")
            case 'min':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado} minuto(s)")
            case 'h':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado} hora(s)")
            case 'd':
                texto_resultado.configure(text=f"A conversão é igual a: \n{
                                          resultado} dia(s)")


# Instância da classe Conversor
instancia = Conversor()

# CTk para criar a janela principal
janela = CTk()
janela.title("Conversor")

janela.geometry("500x300")
janela.resizable(width=False, height=False)


lista_medidas = ['---Comprimento---', 'cm', 'm', 'km', '---Massa---',
                 'mg', 'g', 'kg', '---Tempo---', 's', 'min', 'h', 'd']
# Caixa para entrada dos valores
CTkLabel(janela, text="").place(x=20, y=20)
caixa_valor = CTkEntry(janela, font=("Bahnschrift", 14), placeholder_text="Digite um valor:")
caixa_valor.place(x=180, y=20)

# Botão para converter
botao_converter = CTkButton(
    janela, font=("Bahnschrift", 14), text="Converter", command=Conversor.converter)
botao_converter.place(x=180, y=180)

# Lista com as medidas, converter de:
CTkLabel(janela, font=("Bahnschrift", 14), text="De:").place(x=120, y=70)
lista_converter_de = CTkComboBox(
    janela, values=lista_medidas, state="readonly")
lista_converter_de.place(x=180, y=70)

# Lista com as medidas, converter para:
CTkLabel(janela, font=("Bahnschrift", 14), text="Para:").place(x=120, y=120)
lista_converter_para = CTkComboBox(
    janela, font=("Bahnschrift", 14), values=lista_medidas, state="readonly")
lista_converter_para.place(x=180, y=120)

# Mensagem de resultado
texto_resultado = CTkLabel(janela, text="")
texto_resultado.place(relx=0.5, rely=0.8, anchor="center")

janela.mainloop()