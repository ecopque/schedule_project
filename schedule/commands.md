# Criando projeto no terminal:
. django-admin startproject schedule_project . #1:

# Iniciando git dentro da subpasta:
. git init #2:

# Configurando git dentro da subpasta:
. git config --global user.name "SEU_NOME". #3:
. git config --global user.email "SEU_EMAIL" #4:
. git config --global init.defaultBranch main #5:

# Como ignorar um arquivo, me privando de retirá-lo e o Git nem olhar?:
. touch .gitignore #6: #7:
. nano .gitignore #8:

# Verificar arquivos ignorados dentro da subpasta:
. git status #9:

# Adicioanndo arquivos:
. git add . #10:

# Fazendo commit:
. git commit -m "SUA_MENSAGEM" #11:

# Vinculando ao repositório Github:
. git remote add origin https://github.com/ecopque/schedule_project.git #12:

# Primeiro push + autenticação com Token:
. git push -u origin main (insira e-mail e token) #13:
. git push

# Para onde foram os commits?:
. git log #14:
. :wq #15:
. git log --oneline #16:
. git show "NÚMERO_DO_COMMIT" #17:

# Clonar/Copiar todos os arquivos do github para outra máquina:
. git clone https://github.com/ecopque/schedule_project.git #18:

# Baixar os arquivos do repositório que foram adicionados por outra máquina:
. git pull origin main #19:

# Retirar arquivo do commit:
. git reset HEAD .env #20:

# Apagar um commit errado (ex: e-mail privado):
. git log #21:
. git rebase -i -HEAD~2 #22:
. #Mudar de pick para drop #23:
. #Salvar Nano: "ctrl + o" e depois "enter"
. #Sair do Nano: "ctrl + x"

# Renomeando branch:
. git branch -M main #24: