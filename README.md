# letsencrypt-proxmox
Letsencrypt plugin for Proxmox VE

Installation guide:
* Install [Proxmox VE](https://www.proxmox.com/en/proxmox-ve)
* Deploy latest version of [Let's Encrypt](https://github.com/letsencrypt/letsencrypt)
* Install letsencrypt-proxmox plugin pip install letsencrypt-proxmox

## Use cases:
* Get/Renew and install new certificate

 ```./letsencrypt-auto run --standalone-supported-challenges http-01 -t -i letsencrypt-proxmox:proxmox -d some.domain.tld --no-redirect```

** To automate the renewal process without prompts (for example, with a monthly cron), you can add the letsencrypt parameters --renew-by-default --text

* Install-only existing certificate

 ```./letsencrypt-auto install -t -i letsencrypt-proxmox:proxmox  --letsencrypt-proxmox:proxmox-location /etc/pve/local --cert-path /etc/letsencrypt/live/some.domain.tld/cert.pem --key-path /etc/letsencrypt/live/some.domain.tld/privkey.pem -d some.domain.tld  --fullchain-path /etc/letsencrypt/live/some.domain.tld/fullchain.pem  --no-redirect```

 ```./letsencrypt-auto install -t -i letsencrypt-proxmox:proxmox  --cert-path /etc/letsencrypt/live/some.domain.tld/cert.pem --key-path /etc/letsencrypt/live/some.domain.tld/privkey.pem --fullchain-path /etc/letsencrypt/live/some.domain.tld/fullchain.pem -d some.domain.tld --no-redirect```
