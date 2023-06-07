# Sistema de Gestão para Nutricionistas

### **Objetivo:** desenvolver um sistema para que profissionais de nutrição possam cadastrar dados dos clientes e acompanhar seu estado de saúde

## Tecnologias Utilizadas:
* ### Python
* ### Django
* ### Git
* ### PostgreSQL
* ### Docker

## Funcionallidades do Projeto
### 1. Sistema de cadastro e login de usuário
### 2. Cadastro de pacientes
### 3. Listagem de dados dos pacientes
### 4. Adiciona informações referentes ao estado de saúde do paciente e exibe a evolução do peso em um gráfico
### 5. Cadastro de um plano alimentar personalizado para o paciente que inclui diferentes opções para cada tipo de refeição (café da manhã, almoço e jantar)

## Instruções para instalação

#### _Versão do Python requerida:_ 3.9.13

### Faça o clone do projeto:
```commandline
git clone git@github.com:JulianaRaquel/SISTEMA_GESTAO_NUTRICIONISTAS.git
```
### Criar ambiente virtual (venv):
```commandline
python3 -m venv venv
```
### Ativar ambiente virtual no linux:
```commandline
source venv/bin/activate
```
### Ativar ambiente virtual no windows:
```commandline
venv\Scripts\Activate
```
### Instalar dependências:
```commandline
pip install -r requirements.txt
```

### Copiar as variáveis de ambiente:
```commandline
cp .env.example .env
```
### Aplicar as migrações:
```commandline
python3 manage.py migrate
```
### Rodar o servidor:
```commandline
python3 manage.py runserver
```