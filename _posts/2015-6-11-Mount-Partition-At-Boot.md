---
layout: post
title: Mount Partition At Boot
---

I have created an SMB share on second hard drive and want it to mount automatically after the computer starts up.

Create a folder to mount the device in.

```bash
sudo mkdir /media/josh/storage
```

Get a list of all disks.

```bash
sudo fdisk -l
```

The device I want is ```/dev/sdb1```. Add it to ```/etc/fstab```. 

```
/dev/sdb1 /media/josh/storage ext4 0 0
```

In plain english, mount the device ```/dev/sdb1``` in the folder ```/media/josh/storage```. The device was formatted using ```ext4```. The file system doesn't need to be dumped and doesn't need to be checked at boot time.

These fields are explained in ```man fstab```.

Mount all devices in ```/etc/fstab``` manually to avoid rebooting.

```bash
sudo mount -a
```
