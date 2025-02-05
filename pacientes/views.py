from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from .models import Paciente  # Certifique-se de que o modelo está correto
from validate_docbr import CPF


def pacientes(request):
    if request.method == "GET":
        # Obter a lista de todos os pacientes
        paciente_list = Paciente.objects.all()
        return render(request, 'pacientes.html', {'pacientes': paciente_list})

    elif request.method == "POST":
        # Capturar os dados do formulário
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        telefone = request.POST.get('telefone')
        data_nasc = request.POST.get('data_nasc')
        sexo = request.POST.get('sexo')
        data_entrada = request.POST.get('data_entrada')
        status = request.POST.get('status')

        # Validação de CPF
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf):
            return JsonResponse({'error': 'CPF inválido'}, status=400)

        # Verificar se o paciente já existe
        if Paciente.objects.filter(cpf=cpf).exists():
            return JsonResponse({'error': 'Paciente já existe'}, status=400)

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

        return JsonResponse({'message': 'Paciente cadastrado com sucesso!'}, status=201)


def adicionar_paciente(request):
    if request.method == "GET":
        return render(request, 'adicionar_paciente.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        telefone = request.POST.get('telefone')
        data_nasc = request.POST.get('data_nasc')
        sexo = request.POST.get('sexo')
        data_entrada = request.POST.get('data_entrada')
        status = request.POST.get('status')

        # Validação de CPF
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf):
            return JsonResponse({'error': 'CPF inválido'}, status=400)

        # Verificar se o paciente já existe
        if Paciente.objects.filter(cpf=cpf).exists():
            return JsonResponse({'error': 'Paciente já existe'}, status=400)

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

        return JsonResponse({'message': 'Paciente cadastrado com sucesso!'}, status=201)


def att_paciente(request):
    if request.method == "GET":
        # Busca todos os pacientes cadastrados
        pacientes = Paciente.objects.all()
        return render(request, 'att_paciente.html', {'pacientes': pacientes})
    elif request.method == "POST":
        # Atualiza informações do paciente
        id_paciente = request.POST.get('id_paciente')
        paciente = get_object_or_404(Paciente, id=id_paciente)

        # Retorna dados do paciente selecionado
        paciente_json = {
            'id': paciente.id,
            'nome': paciente.nome,
            'sobrenome': paciente.sobrenome,
            'cpf': paciente.cpf,
            'endereco': paciente.endereco,
            'bairro': paciente.bairro,
            'telefone': paciente.telefone,
            'data_nasc': paciente.data_nasc.strftime('%Y-%m-%d') if paciente.data_nasc else None,
            'sexo': paciente.sexo,
            'data_entrada': paciente.data_entrada.strftime('%Y-%m-%d') if paciente.data_entrada else None,
            'status': paciente.status,
        }

        return JsonResponse(paciente_json)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)


def relatorios(request):
    # Contar pacientes por status
    status_counts = (
        Paciente.objects.values('status')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Contar pacientes que recebem cada tipo de cesta
    cesta_counts = {
        'cereais': Paciente.objects.filter(cereais=True).count(),
        'frutas': Paciente.objects.filter(frutas=True).count(),
        'nutren': Paciente.objects.filter(nutren=True).count(),
        'fraldas': Paciente.objects.filter(fraldas=True).count(),
    }

    # Total de pacientes cadastrados
    total_pacientes = Paciente.objects.count()

    context = {
        'status_counts': status_counts,
        'cesta_counts': cesta_counts,
        'total_pacientes': total_pacientes,
    }

    return render(request, 'relatorios.html', context)


def historico(request):
    return render(request, 'historico.html')
