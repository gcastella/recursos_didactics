# Welcome to Recursos didàctics!

Basat en [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). 

# Env
```
recursos\Scripts\activate
```

# DB
```
flask db init
flask db migrate -m "comment"
flask db upgrade
```

# ElasticSearch
Cal tenir una instància d'ElasticSearch corrent. Comprovar-ho a:
```
http://localhost:9200/
```