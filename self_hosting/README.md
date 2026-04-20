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

```
ansible-playbook -i inventory.ini ./playbook_hardening.yml
```


instalace Docker





