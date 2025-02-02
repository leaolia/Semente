from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente  # Certifique-se de que está correto
from validate_docbr import CPF

def pacientes(request):
    if request.method == "GET":
        return render(request, 'pacientes.html', {'data': datetime(day=22, month=3, year=2015, hour=10, microsecond=2)})

    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereço')
        bairro = request.POST.get('bairro')
        telefone = request.POST.get('telefone')
        data_nasc = request.POST.get('data_nasc')
        sexo = request.POST.get('sexo')
        data_entrada = request.POST.get('data_entrada')
        status = request.POST.get('status')
        cereais = request.POST.getlist('cereais')
        frutas = request.POST.getlist('frutas')
        nutren = request.POST.getlist('nutren')
        fraldas = request.POST.getlist('fraldas')

        # Validação de CPF
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf):
            return HttpResponse('CPF inválido')

        paciente = Paciente.objects.filter(cpf=cpf)

        if paciente.exists():
            return HttpResponse('Paciente já existe')

        # Criar paciente
        paciente = Paciente(
            nome=nome,
            sobrenome=sobrenome,
            cpf=cpf,
            endereco=endereco,
            bairro=bairro,
            telefone=telefone,
            data_nasc=data_nasc,
            sexo=sexo,
            data_entrada=data_entrada,
            status=status,
        )
        paciente.save()

        # Relacionar dados adicionais (se houver modelo correspondente)
        # Exemplo fictício de um modelo Cereais
        for cereal, fruta, nutr in zip(cereais, frutas, nutren):
            item =cereais(cereais=cereal, frutas=fruta, nutren=nutr, paciente=paciente)
            item.save()

        return HttpResponse('Paciente cadastrado com sucesso!')
