# Track your expenses
This is really simple application to help you track your expenses, monthy.

### Installation
Simply git repo and 
```
python manage.py migrate
python manage.py runserver
```

of course it's good idea to run it through Nginx or something similar

### Configuration
You have to add entry to CRON so you can receive Expense Reports eg. (don't forget to set SHELL to bash so you can source)

```
SHELL=/bin/bash
* * * * * source /home/user/.bashrc && source /home/user/django/bin/activate && /home/user/django/bin/python /home/user/django/expenses/manage.py runcrons >> /home/user/django/expenses/cronjob.log
```

Also don't forget to fill your .env file
