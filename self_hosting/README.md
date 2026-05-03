# Velmi stručný úvod do self-hostingu

## Vyvojarsky stroj

instalace ansible
```
python3 -m pip install --user ansible
```
na MacOS take pres Homebrew: https://formulae.brew.sh/formula/ansible


vygenerovat SSH klic
vzdy nastavit passkey
```
ssh-keygen -t ed25519 -f ~/.ssh/my_key -C "yourusername@domain.com"
```

pridat klic
```
ssh-add ~/.ssh/my_key
```

## Server

### Manualni pred-nastaveni

Ansible potrebuje Python, proto jej nainstalujeme a pro jistotu jeste pred tim updatenem vsechny packages:
```
apt update
apt upgrade
apt install python3
```

### Prvni run Ansible

Pri prvnim behu casto jeste nemame vytvoreneho usera na serveru, ale musime se pripojit jako root.
Muzeme overridovat ansible_user v inventory.ini pomoci argumentu --extra-vars (https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html#key-value-format):

Pred spustenim doplnit do skriptu vlastni SSH public klice!
```
ansible-playbook -i inventory.ini ./playbook_hardening.yml --extra-vars "user=andy"
```

Hardening muzeme i nekdy v budoucnu spoustet, pak uz nemusime nastavovat usera, ale proste spustime:

```
ansible-playbook -i inventory.ini ./playbook_hardening.yml
```

playbook_hardening.yml provede zakladni security hardening serveru:
- vypne SSH prihlasovani pomoci username/password a nastavi pouze prihlasovani pomoci SSH klice
- nainstaluje fail2ban, ktery automaticky banuje IP adresy, ktere marne zkousi prihlaseni pres SSH
- taky nastavi uzivatele - v examplu 2, ale muzeme jich pridat vice

### Reverse proxy a example service - playbook_basic.yml

Playbook playbook_basic.yml obsahuje nastaveni reverzni proxy Traefik a dale ukazkove jednoduche Whoami sluzby (zobrazuje info o pripojenem klientovi - IP, headers atd.)

Bezne by jeden server na portech 80 a 433 poskytoval vlastne jeden web.
To je ale trochu plytvani - na nasem self-hostingu chceme mit spoustu sluzeb.
A k tomu je idealni pouzit reverse proxy - reverse proxy sedi na portu 80 a 433 a cte prichozi requesty.
Zjisti, jake URL request vyzaduje - a pote tento request presmeruje do jednotliveho kontejneru.
Muzeme tak dostahnout toho, ze:
- whoami.example.com obsluhuje kontejner whoami
- pocketbase.example.com obsluhuje kontejner pb1
- blog.example.com obsluhuje kontejner writefreely apod.

```
ansible-playbook -i inventory.ini ./playbook_basic.yml
```

### PocketBase databaze - playbook_pocketbase.yml

Playbook nastavi 2 PocketBase databaze, je to jednoducha databaze s friendly API.
Hodi se jako zakladni jednoduchy backend, kdyz ho potrebujeme a nechcem si ho psat rucne :)

