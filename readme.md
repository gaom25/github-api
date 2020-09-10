# Gustavo Ortega

###Prueba S4N

Para esta prueba se programo un servicio que llama al api de github para obtener los gists y los events

Primero se instalan los requerimientos de la siguiente manera, desde la raiz del proyecto

```buildoutcfg
pip install -r requirements/development.txt
```

Para crear la base de datos se ejecutan el scrip en la carpeta scripts
de la siguiente manera:

```buildoutcfg
# desde la raiz del proyecto ejecutar

./scripts/database.sh
```

con este comando se crea la base de datos y se hacen las migraciones

Cabe acotar que la base de datos se crea con el usuario postgres y clave postgres


#### Endpoint

Para ejecutar endpoint que trae la data 
primer se levanta el servidor de la siguiente manera
```buildoutcfg
# desde la raiz del proyecto ejecutar

python git4nstats/manage.py runserver  --settings=git4nstats.settings.development
```

para ejecutar el endpoint se hace de la siguiente manera 
```buildoutcfg
POST localhost:8000/github-users/
```

con el body 
```
{
	"github_users" : ["a", "ovasgus"]
}
```