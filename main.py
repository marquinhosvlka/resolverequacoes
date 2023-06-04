import math
import kivy
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Opção para selecionar o tipo de equação
        self.opcao_label = Label(text='Selecione o tipo de equação:')
        self.opcao_input = TextInput(hint_text='1 para primeiro grau, 2 para segundo grau')

        # Entradas para os coeficientes das equações
        self.input_a = TextInput(hint_text='Digite o coeficiente a')
        self.input_b = TextInput(hint_text='Digite o coeficiente b')
        self.input_c = TextInput(hint_text='Digite o coeficiente c')

        # Botões para resolver a equação e plotar o gráfico
        btn_resolver = Button(text='Resolver', on_press=self.resolver_equacao)
        btn_plotar = Button(text='Plotar Gráfico', on_press=self.plotar_grafico)

        # Resultado da equação
        self.resultado_label = Label(text='')

        layout.add_widget(self.opcao_label)
        layout.add_widget(self.opcao_input)
        layout.add_widget(self.input_a)
        layout.add_widget(self.input_b)
        layout.add_widget(self.input_c)
        layout.add_widget(btn_resolver)
        layout.add_widget(btn_plotar)
        layout.add_widget(self.resultado_label)

        return layout

    def resolver_equacao(self, instance):
        opcao = self.opcao_input.text
        a = float(self.input_a.text)
        b = float(self.input_b.text)
        c = float(self.input_c.text)

        if opcao == '1':
            resultado = self.resolver_equacao_primeiro_grau(a, b)
        elif opcao == '2':
            resultado = self.resolver_equacao_segundo_grau(a, b, c)
        else:
            resultado = 'Opção inválida'

        self.resultado_label.text = f'Resultado: {resultado}'

    def plotar_grafico(self, instance):
        opcao = self.opcao_input.text
        a = float(self.input_a.text)
        b = float(self.input_b.text)
        c = float(self.input_c.text)

        if opcao == '1':
            self.plotar_grafico_primeiro_grau(a, b)
        elif opcao == '2':
            self.plotar_grafico_segundo_grau(a, b, c)
        else:
            self.resultado_label.text = 'Opção inválida'

    def resolver_equacao_primeiro_grau(self, a, b):
        if a == 0:
            if b == 0:
                return "Infinitas soluções"
            else:
                return "Sem solução"
        else:
            x = -b / a
            return x

    def resolver_equacao_segundo_grau(self, a, b, c):
        if a == 0:
            return "Não é uma equação de segundo grau"

        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "Sem solução real"
        elif delta == 0:
            x = -b / (2 * a)
            return x
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return x1, x2

    def plotar_grafico_primeiro_grau(self, a, b):
        x = range(-20, 21)
        y = [a * xi + b for xi in x]

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico da Equação de 1º Grau')
        plt.grid(True)

        # Definir escala dos eixos
        plt.xlim(-20, 20)
        plt.ylim(-20, 20)

        plt.show()

    def plotar_grafico_segundo_grau(self, a, b, c):
        x = range(-20, 21)
        y = [a * xi ** 2 + b * xi + c for xi in x]

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico da Equação de 2º Grau')
        plt.grid(True)

        # Definir escala dos eixos
        raizes = self.resolver_equacao_segundo_grau(a, b, c)
        if isinstance(raizes, tuple):
            raiz_min = min(raizes)
            raiz_max = max(raizes)
            plt.xlim(raiz_min - 1, raiz_max + 1)
        else:
            plt.xlim(-20, 20)

        plt.ylim(-20, 20)

        plt.show()


if __name__ == '__main__':
    MeuApp().run()
