# Lekce 8: Jdeme online

WORK IN PROGRESS!

Až doposud jsme náš server spouštěli pouze lokálně.
A to buď u sebe na počítačí, anebo na repl.it

## Upload kódu na github

### Vytvoření repozitáře

### Nahrání kódu do repozitáře

## Nastavení serveru




### Nastavení služby na serveru



RHEL/CentOS/Fedora:

```
[Unit]
Description=Unusual subjects web server
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=inovotna
WorkingDirectory=/home/inovotna/unusual-subjects
ExecStart=python3 -u /home/inovotna/unusual-subjects/main.py -d False

[Install]
WantedBy=multi-user.target
```

