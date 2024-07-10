git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# MODELS.py:
1  python3 manage.py makemigrations #1:
2  python3 manage.py migrate #2:
3  python3 manage.py createsuperuser #3:
4  python3 manage.py changepassword USERNAME #4: