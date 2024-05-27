# Sesiunea 23 - Django PART 1

## 📝 Obiective
- Ce este un framework
- Ce este un web framework?
- Django
- Parte practica: Setup proiect + baza de date proiect cu Django

## 📌 Dezvoltarea unei aplicatii web cu Django
- In cadrul sesiunilor 23, 24 si 25 vom dezvolta o aplicatie
web folosind web framework-ul Django.
- Aceasta aplicatie va reprezenta un marketplace cu produse
de patiserie.
- In sesiunea curenta (23):
  - vom crea structura proiect github
  - structura proiect Django si creare aplicatii/module
  - setup baza de date
- In sesiunea 24:
  - vom crea modelul pentru products
  - vom crea si aplica migrari de baza de date
  - vom crea rutele de acces lista produse, produs individual
  - vom crea, actualiza, sterge produse din panoul de admin
  - vom renderiza template-uri HTML stilizate cu CSS si Bootstrap
  - vom vedea cum functioneaza Jinja
- In sesiunea 25:
  - vom gestiona sistemul de autentificare, login si logout users
  - (optional) vom adauga complexitate proiectului prin implementarea unui sistem de cos de cumparaturi

## 📌 Ce este un framework?
- Un framework reprezinta un set de librarii, instrumente care ajuta
dezvoltatorii sa construiasca aplicatii mai usor si mai eficient.
- Acesta vine cu un set de reguli, conventii, componente comune care
pot fi utilizate pentru a dezvolta diverse tipuri de aplicatii
  (aplicatii web, aplicatii desktop, aplicatii mobile)

## 📌 Ce este un web framework?
- Un web framework este un tip specific de framework care se concentreaza
pe dezvoltarea aplicatiilor web.
- Acestea sunt proiectate pentru a simplifica procesele comune
asociate cu dezvoltarea web, cum ar fi:
  - manipulare request-uri HTTP
  - creare sabloane HTML
  - interactiune cu baza de date
  - gestionare sesiuni
- Exemple web framework-uri Python: Django, Flask, FastAPI

## 📌 Django
- Web framework puternic si popular pentru dezvoltare rapida de
aplicatii web.
- Vine cu un ORM integrat, sistem de administarare, gestionare
automata a formularelor.
- Resursa utila: https://www.w3schools.com/django/

## 📌 Aplicatie web cu Django - PART 1

### 🔷 Pasi creare si configurare proiect Github
- Creeaza un repo pe Github
  - asigura-te ca ai fisier-ul ```.gitignore``` (template Python) + fisierul ```README.md``` 
- Clonare repo pe local
- Actualizare fisier ```.gitignore```:
  - trebuie sa ne asiguram ca folder-ul privat creat de Pycharm (.idea)
nu va fi incarcat niciodata in repo-ul de pe Github

### 🔷 Virtualenv & Instalare Django
- Creare virtualenv: ```python -m venv venv```
- Activare virtualenv: ```venv/Scripts/Activate.ps1```
- Instalare django in virtualenv: ```pip install django```
- Creare fisier ```requirements.txt```
- Adaugarea tuturor pachetelor instalate in virtualenv in fisierul ```requirements.txt```:
```pip freeze > requirements.txt```

### 🔷 Creare proiect Django
- Inainte de a incepe sa lucram la aplicatia web, este necesar
sa cream un proiect Django
- Acesta ne va oferi o colectie de setari pentru aplicatia noastra,
inclusiv configurarea bazei de date
- Rulam comanda urmatoare: ```django-admin startproject marketplace```
- Verificam ca proiectul Django functioneaza: ```python manage.py runserver```
  - ATENTIE: Aceasta comanda trebuie rulata din terminal, dupa ce am navigat
  in folder-ul root ```marketplace```: ```cd marketplace```

### 🔷 Structura proiect Django:
- Folder-ul root ```marketplace```: container-ul pentru proiect.
- Fisierul ```manage.py```: responsabil de gestionarea si administrarea proiectului.
  - o serie de comenzi care pot fi folosite pentru a realiza
  diferite activitati in cadrul proiectului Django:
    - initializare db
    - creare superuser
    - rulare server de dezvoltare
- Folder-ul interior ```marketplace```: Pachetul Python al proiectului, care
contine configurarile principale ale proiectului
- Fisierul ```marketplace\__init__.py```: un fisier gol care face folder-ul
interior ```marketplace``` sa fie tratat ca un Python package.
- Fisierul ```marketplace\settings.py```: setarile/configurarea proiectului.
- Fisierul ```marketplace\urls.py```: aici se definesc rutele principale
ale proiectului.
- Fisierele ```marketplace\asgi.py``` si ```marketplace\wsgi.py```: necesare
pentru a face aplicatia Django sa poata fi deservita de diferite tipuri de servere
web.

### 🔷 Creare aplicatie

- In interiorul proiectului Django, putem sa ne cream
una sau mai multe aplicatii/module care sa contina functionalitatile
necesare pentru aplicatia web marketplace.
- Vom avea o aplicatie, numita ```marketplaceapp```.
- ```python manage.py startapp marketplaceapp```

### 🔷 Structura aplicatie/modul in Django
- Vom analiza structura aplicatiei/modulului creat
in Django.
- Folder-ul ```marketplaceapp```: folder-ul principal al aplicatiei/modulului
cu produse. Acesta este un Python Package si va contine codul necesar pentru
implementarea si interactiunea cu produsele.
- Fisierul ```marketplaceapp\__init__.py```: fisier gol care face
directorul ```marketplaceapp``` sa fie un Python package.
- Fisierul ```marketplaceapp\admin.py```: configurari ale modelelor
pentru a fi gestionate prin intermediul panoului de administrare Django.
- Fisierul ```marketplaceapp\apps.py```: configurari specifice ale aplicatiei/modulului
- Fisierul ```marketplaceapp\models.py```: Definirea modelelor/tabelelor din baza de date.
- Fisierul ```marketplaceapp\tests.py```: definirea testelor pentru aplicatia/modulul curent
- Fisierul ```marketplaceapp\views.py```: definirea comportamentelor ce vor fi accesate de la diferite
rute din aplicatie.
- Folder-ul ```marketplaceapp\migrations```: folder ce va contine migrari ale bazei de date.


### 🔷 Crearea primului view in aplicatie
- In fisierul ```marketplaceapp\views.py``` vom crea primul view al aplicatiei
noastre.
- Un view reprezinta o functie care returneaza un response sau un template,
care va fi apoi asociata cu o ruta, astfel incat in momentul in care,
din aplicatia web se va accesa acea ruta, se va declansa comportamentul definit
in view (se va apela functia asociata din fisierul ```views.py``)

```python
# in fisierul marketplaceapp\views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're on the marketplace app home.")
```

- Dupa definirea view-ului, pentru a-l vedea in aplicatia web, va trebui sa
il mapam la un url.
- Creeaza un fisier ```urls.py``` in folder-ul ```marketplaceapp```.
- Include urmatorul cod in fisierul ```marketplaceapp\urls.py```:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```
- Urmatorul pas este includerea tuturor rutelor ce vor fi definite
in aplicatia ```marketplaceapp``` la nivelul proiectului.
- Pentru asta, in fisierul ```urls.py``` de la nivelul proiectului,
in lista de ```urlpatterns```, vom adauga urmatorul path: ```path("marketplace/", include("marketplaceapp.urls"))```
- **IMPORTANT**: functia include() va fi importata din ```django.urls```
- **NOTA**: primul parametru dat la functia path() reprezinta inceputul fiecarei rute
din aplicatia ```marketplaceapp```. Poti sa schimbi astfel valoarea sa cu valoarea
dorita de tine.

### 🔷 Setup baza de date
- In fisierul ```marketplace\settings.py``` sunt definite mai multe
variabile/constante, reprezentand configurari ale proiectului Django.
  - In constanta ```DATABASES``` este definita configurarea bazei de date
  pentru proiectul Django curent. Acesta este configurat default sa foloseasca
  SQLite.
  - Actualizeaza valoarea constantei TIME_ZONE: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
  - Setarea INSTALLED_APPS - contine toate aplicatiile care vor fi instalate
  in instanta curenta de Django. Mai multe aplicatii sunt incluse ca default, care ofera
  diferite functionalitati aplicatiei web dezvoltate.
  - Aceste aplicatii default folosesc cel putin un tabel in baza de date, motiv pentru care
  trebuie sa facem setup bazei de date si sa cream tabelele necesare.
- Setup baza de date (creare db + tabele initiale): ```python manage.py migrate```
- De fiecare data cand vom avea modificari la nivelul bazei de date (adaugari de tabele noi,
actualizari) va trebui sa facem o migrare a acesteia (vom discuta in sesiunile urmatoare).
- Dupa rularea comenzii de migrare baza de date, se poate observa la nivelul
proiectului, fisierul ce reprezinta baza de date.
