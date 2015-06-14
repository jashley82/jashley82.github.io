---
layout: post
title: Create A Samba Share
---

Install samba.
```bash
sudo apt-get install samba
```

Set a password.
```bash
sudo smbpasswd -a josh
```

Create a share in ```/etc/samba/smb.conf```
```
[movies]
  path = /media/josh/storage/movies
  available = yes
  valid users = josh
  read only = yes
  browsable = yes
  public = no
  writable = no
```

Restart the service.
```bash
sudo service smbd restart
```

Now make sure ```/media/josh/storage``` gets properly mounted and g2g.
