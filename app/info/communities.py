from typing import TypedDict


class Community(TypedDict):
    name: str
    logo_src: str
    url: str


communities: list[Community] = [
    {
        "name": "Sudo FCiencias",
        "logo_src": "/logos/sudo.png",
        "url": "https://linktr.ee/Sudo_FCiencias",
    },
    {
        "name": "PythonCDMX",
        "logo_src": "/logos/pythoncdmx.jpg",
        "url": "https://pythoncdmx.org/",
    },
    {
        "name": "AWS Cloud Club UNAM",
        "logo_src": "/logos/awscloudclubunam.png",
        "url": "https://linktr.ee/aws_unam",
    },
    {
        "name": "Guayaba Devs",
        "logo_src": "/logos/guayabadevs.jpeg",
        "url": "https://guayabadev.com/",
    },
    {
        "name": "Nebursaturn Academy",
        "logo_src": "/logos/nebursaturn.jpeg",
        "url": "https://www.instagram.com/nebursaturnacademy/",
    },
    {
        "name": "Panteras.Dev",
        "logo_src": "/logos/panterasdev.jpeg",
        "url": "https://linktr.ee/Panteras.Dev",
    },
    {
        "name": "shellaquiles",
        "logo_src": "/logos/shellaquiles.svg",
        "url": "https://shellaquiles.org/",
    },
    {
        "name": "FedoraMX",
        "logo_src": "/logos/fedoramx.png",
        "url": "https://t.me/fedoramexico",
    },
    {
        "name": "AWS USG Ajolotes en la Nube",
        "logo_src": "/logos/ajolotesaws.png",
        "url": "https://aws-cdmx.my.canva.site/",
    },
    {
        "name": "Grupo Linux Chihuahua",
        "logo_src": "/logos/gluch.jpg",
        "url": "https://www.facebook.com/groups/219085400136/",
    },
    {   "name": "RustMX", 
        "logo_src": "/logos/rustmx.jpg", 
        "url": "https://t.me/RustMX"},
    {
        "name": "Gophers MX",
        "logo_src": "logos/gomx.jpg",
        "url": "https://gophers-mx.github.io/gophers-mx/",
    },
    {   "name": "LIDSOL", 
        "logo_src": "logos/lidsol.jpg", 
        "url": "https://lidsol.org/"
    },
    {
        "name": "C++ MX",
        "logo_src": "logos/cppmx.png",
        "url": "https://cpp.com.mx/"
    },
    {
        "name": "Club de Programación FING",
        "logo_src": "logos/cdpfing.png",
        "url": "https://www.instagram.com/club_de_programacion_fing"
    },
    {
        "name": "AWS Cloud Club CardenalITOs",
        "logo_src": "logos/cardenalitos.jpg",
        "url": "https://linktr.ee/CardenalITOs_Cloud_Clubs"
    }
]
