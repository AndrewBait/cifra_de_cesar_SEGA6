from django.views.generic import TemplateView
from django.shortcuts import render
import string
from collections import Counter

class CifraView(TemplateView):
    template_name = 'cifra/cifra.html'

    def post(self, request, *args, **kwargs):
        mensagem = request.POST.get('mensagem', '')
        deslocamento = request.POST.get('deslocamento', '')
        operacao = request.POST.get('operacao', 'cifrar')

        if operacao == 'cifrar':
            if deslocamento.isdigit():
                resultado = self.cifra_cesar(mensagem, int(deslocamento))
            else:
                resultado = 'Por favor, insira um deslocamento válido para cifrar a mensagem.'
        elif operacao == 'decifrar':
            if deslocamento.isdigit():
                resultado = self.cifra_cesar(mensagem, -int(deslocamento))
            else:
                resultado = 'Por favor, insira um deslocamento válido para decifrar a mensagem.'
        else:
            resultado = self.analise_frequencia(mensagem)

        return render(request, self.template_name, {
            'resultado': resultado,
            'mensagem': mensagem,
            'deslocamento': deslocamento,
            'operacao': operacao,
        })


    def cifra_cesar(self, mensagem, deslocamento):
        alfabeto = string.ascii_uppercase
        resultado = ''

        for letra in mensagem.upper():
            if letra in alfabeto:
                nova_posicao = (alfabeto.index(letra) + deslocamento) % 26
                resultado += alfabeto[nova_posicao]
            else:
                resultado += letra
        return resultado
        

    def analise_frequencia(self, mensagem):
        frequencia_esperada = 'AEOSRNIDMULCTPVGQBFHZJXYKW'
        mensagem_upper = mensagem.upper()
        mensagem_filtrada = ''.join(filter(str.isalpha, mensagem_upper))  # Remove caracteres não alfabéticos
        contador = Counter(mensagem_filtrada)

        if not contador:
            return 'Mensagem vazia ou sem caracteres alfabéticos.'

        # Letra mais frequente na mensagem cifrada
        letra_mais_frequente = contador.most_common(1)[0][0]

        # Supondo que a letra mais frequente corresponde a 'A' em português
        deslocamento = (string.ascii_uppercase.index(letra_mais_frequente) - string.ascii_uppercase.index('A')) % 26
        
        # Decifra a mensagem mantendo os espaços
        mensagem_decifrada = ''.join(
            self.cifra_cesar(char, -deslocamento) if char.isalpha() else char for char in mensagem_upper
        )
        
        return f'Deslocamento estimado: {deslocamento}\nMensagem decifrada: {mensagem_decifrada}'
