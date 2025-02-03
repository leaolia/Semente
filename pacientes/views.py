from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Paciente  # Certifique-se de que está correto
from validate_docbr import CPF
import re
from django.core import serializers
import json
from django.shortcuts import render


def pacientes(request):
    if request.method == "GET":
        paciente_list = Paciente.objects.all()
        return render(request, 'pacientes.html', {'pacientes': paciente_list})

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
    
def att_paciente(request):
    id_paciente = request.POST.get('id_paciente')
    paciente = Paciente.objects.filter(id=id_paciente)
    paciente_json = json.loads(serializers.serialize('json', paciente))[0]['fileds']
    print(paciente_json)
    return JsonResponse(paciente_json)
