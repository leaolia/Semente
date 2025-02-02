from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=12)
    endereco = models.CharField(max_length=100)  # Campo para endereço
    bairro = models.CharField(max_length=50)  # Campo para bairro
    telefone = models.CharField(max_length=15)  # Para aceitar formatos como (XX) XXXXX-XXXX
    data_nasc = models.DateField()  # Campo para data de nascimento
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])  # Escolha de gênero
    data_entrada = models.DateField()  # Campo para data de entrada
    status = models.CharField(
        max_length=20, 
        choices=[
            ('Ativo', 'Ativo'), 
            ('Inativo', 'Inativo'), 
            ('Manutencao', 'Manutenção'),
            ('Alta', 'Alta'),
            ('Obito', 'Óbito'),
            ('Paleativo', 'Paleativo')
        ]
    )  # Status do paciente
    tipo_cancer = models.CharField(max_length=100, blank=True, null=True)  # Tipo de câncer
    observacao = models.TextField(blank=True, null=True)  # Observações adicionais

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome}"


class Cereais(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_cesta = models.CharField(
        max_length=20, 
        choices=[
            ('basica', 'Básica'),
            ('frutas', 'Frutas'),
            ('legumes', 'Legumes'),
            ('cereais', 'Cereais')
        ],
        blank=True,
        null=True
    )  # Tipo de cesta recebida
    opcao_cesta = models.CharField(
        max_length=20, 
        choices=[
            ('cesta_alternada', 'Cesta Alternada'),
            ('mensal', 'Mensal'),
            ('tempo_indeterminado', 'Tempo Indeterminado'),
            ('suspensa', 'Suspensa')
        ],
        blank=True,
        null=True
    )  # Detalhes da cesta
    cereais = models.BooleanField(default=False)  # Sim ou Não para cereais
    quantidade_cereais = models.IntegerField(default=0, blank=True)  # Quantidade de cereais (se aplicável)
    frutas = models.BooleanField(default=False)  # Sim ou Não para frutas
    quantidade_frutas = models.IntegerField(default=0, blank=True)  # Quantidade de frutas (se aplicável)
    nutren = models.BooleanField(default=False)  # Sim ou Não para Nutren
    quantidade_nutren = models.IntegerField(default=0, blank=True)  # Quantidade de Nutren (se aplicável)
    fraldas = models.BooleanField(default=False)  # Sim ou Não para fraldas
    quantidade_fraldas = models.IntegerField(default=0, blank=True)  # Quantidade de fraldas (se aplicável)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # Relacionamento com o Paciente

    def __str__(self):
        return (
            f"{self.paciente.nome} - "
            f"Tipo de Cesta: {self.tipo_cesta if self.tipo_cesta else 'Não Recebe'}, "
            f"Opção: {self.opcao_cesta if self.opcao_cesta else 'N/A'}, "
            f"Cereais: {'Sim' if self.cereais else 'Não'} ({self.quantidade_cereais}), "
            f"Frutas: {'Sim' if self.frutas else 'Não'} ({self.quantidade_frutas}), "
            f"Nutren: {'Sim' if self.nutren else 'Não'} ({self.quantidade_nutren}), "
            f"Fraldas: {'Sim' if self.fraldas else 'Não'} ({self.quantidade_fraldas})"
        )
