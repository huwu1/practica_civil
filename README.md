### Instrucciones para alojo/testeo local:

Primero, se debe clonar este repositorio; una vez ubicado en el directorio en el que se desee alojar el proyecto, escribe el siguiente comando:

```bash

git clone https://github.com/huwu1/practica\_civil.git

```



Una vez clonado, dentro del mismo directorio se tiene que crear un ambiente virtual para poder instalar las dependencias necesarias contenidas dentro del archivo 'requirements.txt'. El siguiente comando creará uno llamado 'venv', y el siguiente lo activará:



En Windows:

`

python -m venv venv

venv\\Scripts\\activate

`



En Mac / Linux:

`

python -m venv venv

source venv/bin/activate

`



Con esto, ya se puede descargar lo necesario con la siguiente línea:

`

pip install -r requirements.txt

`



¡Listo! Ya tienes el proyecto en tu dispositivo, ahora, para hacer válida la base de datos, se debe hacer saber a la misma los cambios y estructura contenida dentro de 'models.py'. Para esto, ubícate dentro del directorio '/webmap' (donde se encuentra 'manage.py') y aplica la siguiente linea:

`

python manage.py migrate

`



(Se utilizó DB Browser para la transferencia de datos, queda pendiente un script que se encargue de esta tarea)



Y listo, ya tienes todo lo necesario para poder ver cambios localmente y hacer testeo antes de comittearlos a la página web webampnunoa.me. Se recomienda de todas formas crear *branches* para diferenciar. Con el siguiente comando puedes correr localmente el servidor (ubicado en el mismo directorio que el paso anterior):

`

python manage.py runserver
`



### Acerca de la página:

Mediante CloudFlare se asoció una *whitelist* de direcciones de correo electrónico, las cuales son las únicas que tienen acceso. Cualquier inconveniente o si se desea ampliar este grupo de personas con acceso, me contactan vía correo a @hugogonzalez3063@gmail.com o por cualquier vía que les acomode.



Cabe recalcar que existen otros mapas visualizables en la página, como el de la velocidad, tiempo, DCA y planes. No aparecen como seleccionables pues no eran de interés a esta altura del proyecto, pero basta con des-comentar las líneas 25 a 29 dentro del HTML (.../webmap/map/templates/page.html) para poder observarlas.



También mencionar que por temas de tiempo la funcionalidad de la visualización de los mapas quedo inconclusa. Se sugiere si en el futuro se desea analizar este mapa, seguir la misma lógica para el slider que con el mapa de cinemática.



Dentro del HTML se encuentra un *disclaimer* al respecto del gradiente utilizado para la visualización de los mapas anteriormente mencionados.

