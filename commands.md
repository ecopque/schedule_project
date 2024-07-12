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

# SHELL DJANGO
python3 manage.py shell #1:

from contact.models import cls_contact #2:
cls_contact #2:
c = cls_contact(first_name='Edsu') #3:
c #3:
c.save() #3:
c.last_name = 'Copque' #4:
c.save() #4:
c.phone = '+5571999888777' #5:
c.delete() #5:
c.save() #6: vai recuperar contato.

c = cls_contact.objects.get(id=2) # ou pk=2
c.firts_name='Dr. Enéas'
c.save()
c.pk

c = cls_contact.objects.all()
c # <QuerySet [<cls_contact: Carl Sagan>, <cls_contact: Dr. Enéas Carneiro>, <cls_contact: Edsu Copque>]>
for i in c: i.first_name # Não funcionou.

c = cls_contact.objects.filter(pk=2)
c