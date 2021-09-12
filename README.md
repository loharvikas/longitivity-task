### Setup the enivronment and install all dependencies.
```bash
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Start development server.
```bash
python3 manage.py runserver 8000
```

Then open http://localhost:8000 to see your app.

# How it works
---
* It has two endpoints api/register and api/organisation

* api/register is to register a user can be a organisation or  just user.

* api/organisation is to register an organisation(e.g welltory).



