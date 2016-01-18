---
layout: post
title: Add Extension To Multiple Files
---

I created a python script to create a new empty blog post using today's date and a supplied title. Problem is I forgot to add the markdown file extension. Easy fix.

```bash
rename 's/(.*)/$1.md/' *
```
