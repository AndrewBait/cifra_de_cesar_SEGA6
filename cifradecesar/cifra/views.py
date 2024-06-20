from django.views.generic import TemplateView
from django.shortcuts import render

class CifraView(TemplateView):
    template_name = 'cifra/cifra.html'

    def post(self, request, *args, **kwargs):
        mensagem = request.POST.get('mensagem', '')
        deslocamento = int(request.POST.get('deslocamento', 0))
        operacao = request.POST.get('operacao', 'cifrar')

        if operacao == 'cifrar':
            resultado = self.cifra_cesar(mensagem, deslocamento)
        else:
            resultado = self.cifra_cesar(mensagem, -deslocamento)

        return render(request, self.template_name, {
            'resultado': resultado,
            'mensagem': mensagem,
            'deslocamento': deslocamento,
            'operacao': operacao,
        })

    def cifra_cesar(self, mensagem, deslocamento):
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        resultado = ''

        for letra in mensagem.upper():
            if letra in alfabeto:
                nova_posicao = (alfabeto.index(letra) + deslocamento) % 26
                resultado += alfabeto[nova_posicao]
            else:
                resultado += letra
        return resultado






















































# def cifra_cesar(mensagem, deslocamento):
#     alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     resultado = ''
    
#     for letra in mensagem.upper():
#         if letra in alfabeto:
#             nova_posicao = (alfabeto.index(letra) + deslocamento) % 26
#             resultado += alfabeto[nova_posicao]
#         else:
#             resultado += letra
#     return resultado

# mensagem = "A Cesar o que e de César. Todos os caminhos levam a Roma."
# deslocamento = 7
# mensagem_cifrada = cifra_cesar(mensagem, deslocamento)
# mensagem_cifrada