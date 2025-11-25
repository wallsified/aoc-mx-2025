# ¡Bienvenidx a las Posadas de Código!

Este repo es la landing page del proyecto + algunos otros archivos que eran necesarios alojar
para que funcionara la página y parte del backend de los leaderboards. 

Si quieres unirte, puedes revisar toda la información del evento en [posadasdecódigo.com](posadasdecódigo.com)

## Instalación y Dependencias del Proyecto

- La página está realizada en su totalidad usando Reflex, la cual es una libreria de Python.
- Se recomienda encarecidamente usar Python>3.11 y uv.

```bash
uv sync
source .venv/bin/activate
reflex init
reflex run
```

Esto abrirá los puertos 3000 (para el frontend) y el 8000 (para el backend, pero este no se usa)

## Distribución del Proyecto

- `/app` Contiene los archivos fuente de la página.
  - `/atoms` Son los componentes base-modificados a las necesidades de Posadas de Código.
  - `/info` son los archivos que dan pie a las reglas, información de comunidades, FAQs, etc. Más que nada, son los diccionarios del proyecto.
  - `/pages` Los archivos de las páginas de Posadas de Código (index, créditos, etc.)
  - `/sections` Cada página está compuesta de secciones armadas a partir de (en parte) lo ubicado en `atoms`. 
    - `/community_info` Información particular para las comunidades participantes.
    - `/credits` Información de los créditos del proyecto.
    - `/thanks` Nuestros agradecimientos.
  - `/wraps` Componentes de React _wrappeados_ para la paǵina.
- `/assets` Recursos varios del proyecto. 
  - `/lobbies` Imágenes para crear los lobbies de las comunidades.
  - `/logos` Logotipos de las comunidades participantes.
  
>[!NOTE]
>Sobra decir que el contenido de `/logos` pertenece unicamente a las comunidades participantes, y por ningún
>motivo se deben ocupar sin el permiso previo y explícito de los líderes de las mismas.


## Despliegue

Dada la naturelza poco ortodoxa del proyecto, el despliegue está realizado en Vercel conectado al dominio
de Posadas de Código. Si quieres replicarlo, usa los archivos `build.sh`y `vercel.json`


## FAQ's

- ¿Por qué en Python?
Por que la verdad es que no se mucho (si no es que nada) de diseño web. Necesitabamos crear una landing
page de manera rápida y ocupando lo que ya sabiamos. Y Reflex justo cumplia ese propósito.

- ¿Por qué en Vercel?
Por lo anterior del despliegue y por que no involucraría un costo asociado. 

- ¿Por qué aquí y no en los repos de Sudo FCiencias?
Por que no hay capa gratuita de despliegue desde perfiles de organizaciones en Vercel. Pero en todo sentido
es un repo para la comunidad. 

- ¿Puedo tomar parte del código aquí para yo crear algo?
¡Adelante! Eres libre de hacerlo al 100%. Solo no uses los logotipos de las comunidades a menos que tengas permiso explícito de hacerlo.