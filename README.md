# MicroServis pre REST API
##  na manažovanie príspevkov použivateľov

Aplikácia je postavená na Flasku.
- Prístup k databáze je riešený cez Flask SQLAlchemy.
- API je postavené na Flask Marshmallow
- Pre dokumentáciu k API sa využíva Swegger

## Info 

Odkazy na jednotlive použité frameworky a knižnice

| Knižnica | Dokumentácia |
| ------ | ------ |
| Flask-SQLAlchemy | https://flask-sqlalchemy.palletsprojects.com/en/2.x/ |
| flask-marshmallow | https://flask-marshmallow.readthedocs.io/en/latest/ |
| marshmallow-sqlalchemy | https://marshmallow-sqlalchemy.readthedocs.io/en/latest/ |
| marshmallow | https://marshmallow.readthedocs.io/en/stable/ |
| connexion[swagger-ui] | https://connexion.readthedocs.io/en/latest/quickstart.html |

## Inštalácia cez Príkazový riadok (command line)
! Testované na pre Windows 10 !
Preto sa inštalácia môže v niektorých miestach líšiť naprieč rôznymi OS.

Spustiť si vo windowse **príkazový riadok** alebo **WIN + R** a napísať **cmd.exe**

Treba sa nastaviť do priečinka s projektami, napr:
```sh
    cd C:\Kod\2022\
```

Vytvorenie priečinku, nazveme si ho napr. micro:

```sh
mkdir micro
cd micro
```

## Inštalácia programu
Program stačí stiahnuť cez zip súbor, alebo ho naklonovať cez git rezitár.
#### Stiahnúť zip 
```sh
https://github.com/jastrab/api_microservice/archive/refs/heads/main.zip
```
stiahnúť a rozbaliť do priečinku api, v adresári micro.

alebo
#### Cez repozitár git:
```sh
   git clone https://github.com/jastrab/api_microservice.git api
```

### Vytvorenie virtualky cez venv:
Inštalácia je pre virtuálku (venv), cez ktorú beží aplikácia. 
Aplikácia nevžaduje virtuálku, ale je to odporúčané.
Inštalácia knižníc je nevyhnutná pre chod aplikácie, pokiaľ už neboli predtým nainštalované.

Inštalácia
```sh
python -m venv venv
```
Aktivácia
```sh
venv\Scripts\activate
```
- pre cmd: venv\Scripts\activate.bat
- pre powershell : venv\Scripts\Activate.ps1
- pre linux venv/bin/activate 

pripade pozriet dokumentaciu https://docs.python.org/3/library/venv.html
Pre úspešné aktivovanie virtuálky je na začiatku príkazu (venv)
```sh
(venv) C:\KoD\2022\micro>
```
### Inštalácia knižníc
Pozor! Stále pracujeme pod virtuálkou, ale pre prehľadnosť príkazov, ju nezobrazujem.

Všetko v jednom príkaze:
```sh
python -m pip install Flask-SQLAlchemy flask-marshmallow marshmallow-sqlalchemy marshmallow connexion[swagger-ui]
```
alebo postupná:
```sh
python -m pip install Flask-SQLAlchemy
python -m pip install flask-marshmallow 
python -m pip install marshmallow-sqlalchemy
python -m pip install marshmallow
python -m pip install connexion[swagger-ui]
```


## Spustenie

### Incializácia DB

```sh
python .\api\create_db.py
```

### Spustenie servisu
```sh
python .\api\server.py
```

### Ukážka úspešného spustenia servisu:
```sh
(venv) C:\KoD\2022\micro>python .\api\server.py
 * Serving Flask app 'config' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.237.122:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 102-400-544
```

## Spustenie Segger API
Servis nemá domovskú stránku, ale používa UI Seggera, preto treba zadať:
IP - ip pridelená frameworkom - buď lokálna - localhost, alebo globálna
PORT - defaultne nastavený na 5000
```sh
    [IP:PORT]/api/ui
```
### Príklad URL pre prehliadač
```sh
http://127.0.0.1:5000/api/ui
```
## License

MIT

**Free Software!**

