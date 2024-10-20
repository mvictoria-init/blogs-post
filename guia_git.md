# Hacer requeriments.txt

pip freeze > requirements.txt

# si no tienes git en el proyecto

1. git init

# si tienes el proyecto creado

1. crear repositorio (gitlab, github, entre otros)

<!-- procurar crear el proyecto en blanco -->
2. se copia el url del repositorio (https://github.com/mvictoria-init/blogs-post.git)

<!-- si el repositorio no esta vacio -->
1. git remote add origin url (https://github.com/mvictoria-init/blogs-post.git)
2. verificar los git remote con: git remote -v
3. git pull origin main(es la rama principal)

# .gitignore

colocar siempre los entornos de programacion en el .gitignore como por ejemplo el env de python