    
python -m pip install Django
python -m django --version
django-admin startproject zdravstveni_sustav
python manage.py startapp zdravstveni_sustav_app
python manage.py runserver


python manage.py makemigrations
python manage.py migrate

{% for narudzba in narudzba_set %}
    <li>
        <p>Pacijent {{ narudzba.ime_pacijenta }} {{ narudzba.prezime_pacijenta }} 
            naručio se na pregled kod vas datuma {{ narudzba.datum_pregleda|date:"d. m. Y." }} 
            u sljedeće vrijeme: {{ narudzba.vrijeme_pregleda }}</p>
        <p>{{ narudzba.ime_pacijenta }} je naveo sljedeće simptome: {{ narudzba.simptomi }}</p>
    </li>
{% endfor %}