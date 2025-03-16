from django.contrib import admin
from .models import Usuario, Clinica, Paciente, ProfissionalSaude, Recepcionista, Consulta

# Permite visualizar e gerenciar usuários
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'tipo_usuario', 'clinica')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('tipo_usuario', 'clinica')

# Gerenciamento de Clínicas
@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')
    search_fields = ('nome',)

# Pacientes
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_de_nascimento', 'idade', 'endereco')
    search_fields = ('nome',)

# Profissionais de Saúde
@admin.register(ProfissionalSaude)
class ProfissionalSaudeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade')
    search_fields = ('nome', 'especialidade')

# Recepcionistas
@admin.register(Recepcionista)
class RecepcionistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'data_contratacao')
    search_fields = ('nome',)

# Consultas
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'profissional_saude', 'clinica', 'data_hora', 'status')
    search_fields = ('paciente__nome', 'profissional_saude__nome', 'clinica__nome')
    list_filter = ('status', 'data_hora', 'clinica')