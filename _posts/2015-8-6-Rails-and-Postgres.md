---
layout: post
title: Rails and Postgres
---

Install Ruby and Rails with RVM

```bash
curl -L https://get.rvm.io | bash -s stable --rails
```

Or by gem
```bash
gem install rails pg
```

Switch to Postgres User and Drop into PG Shell
```bash
su - postgres && psql
```

Create Role

```sql
create role myapp with createdb login password 'password1';
```

Create Rails App

```bash
rails new myapp --database=postgresql
```

Configure dayabase.yml

```
development:
  adapter: postgresql
  encoding: unicode
  database: myapp_development
  pool: 5
  username: myapp
  password: password1

test:
  adapter: postgresql
  encoding: unicode
  database: myapp_test
  pool: 5
  username: myapp
  password: password1
```

Initial Setup

```bash
rake db:setup
```

Create App and Migrate

```bash
rails g scaffold Post title:string body:text
rake db:migrate
```
