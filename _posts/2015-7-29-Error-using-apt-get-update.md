---
layout: post
title: Error using apt-get update
---

Running ```apt-get update``` returned the following error:

```
Reading package lists... Error!
E: Encountered a section with no Package: header
E: Problem with MergeList /var/lib/apt/lists/repo.steampowered.com_steam_dists_precise_steam_i18n_Translation-en
E: The package lists or status file could not be parsed or opened.
```

The soultion was to remove cache directories ```sudo rm -r /var/cache/apt /var/lib/apt/lists```
and re-run the command.
