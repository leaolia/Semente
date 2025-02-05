from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from .models import Paciente, Cereais  # Certifique-se de que o modelo está correto
from validate_docbr import CPF
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login

def is_admin(user):
    return user.groups.filter(name='Administrador').exists()

def is_user(user):
    return user.groups.filter(name='Usuário').exists()

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')


    return render(request, 'registration/login.html')


    return render(request, 'registration/login.html')


def pacientes(request):
    pacientes = Paciente.objects.all()  # Recupera todos os pacientes do banco de dados
    return render(request, 'pacientes.html', {'pacientes': pacientes})  # Renderiza a página inicial com os pacientes

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

    # Filtrar pacientes por status
    pacientes_ativos = Paciente.objects.filter(status="Ativo")
    pacientes_inativos = Paciente.objects.filter(status="Inativo")
    pacientes_manutencao = Paciente.objects.filter(status="Manutencao")
    pacientes_alta = Paciente.objects.filter(status="Alta")
    pacientes_obito = Paciente.objects.filter(status="Obito")
    pacientes_paleativo = Paciente.objects.filter(status="Paleativo")

    # Obter listas de pacientes que recebem cada tipo de cesta
    pacientes_cereais = Paciente.objects.filter(cereais__cereais=True).distinct()
    pacientes_frutas = Paciente.objects.filter(cereais__frutas=True).distinct()
    pacientes_nutren = Paciente.objects.filter(cereais__nutren=True).distinct()
    pacientes_fraldas = Paciente.objects.filter(cereais__fraldas=True).distinct()

    # Total de pacientes cadastrados
    total_pacientes = Paciente.objects.count()

    context = {
        'status_counts': status_counts,
        'pacientes_ativos': pacientes_ativos,
        'pacientes_inativos': pacientes_inativos,
        'pacientes_cereais': pacientes_cereais,
        'pacientes_frutas': pacientes_frutas,
        'pacientes_nutren': pacientes_nutren,
        'pacientes_fraldas': pacientes_fraldas,
        'total_pacientes': total_pacientes,
        'pacientes_manutencao': pacientes_manutencao,
        'pacientes_alta': pacientes_alta,
        'pacientes_obito': pacientes_obito,
        'pacientes_paleativo': pacientes_paleativo,
    }

    return render(request, 'relatorios.html', context)