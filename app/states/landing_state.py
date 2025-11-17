import reflex as rx
from typing import TypedDict


class Community(TypedDict):
    name: str
    logo_src: str
    url: str


class Faq(TypedDict):
    question: str
    answer: str


class LandingState(rx.State):
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
            "logo_src": "/logos/fedoramx.jpg",
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
        {
            "name": "RustMX",
            "logo_src": "/logos/rustmx.jpg",
            "url": "https://t.me/RustMX",
        },
        # pendientes de confirmacion: JavaMX, LIDSOL, Hackers Fight Club
        # pendientes de informacion: RustMX, GoMX
    ]
    faqs: list[Faq] = [
        {
            "question": "¿Necesito saber programar para participar?",
            "answer": "No es estrictamente necesario, pero sí recomendable. Los retos de Advent of Code están diseñados para ser resueltos con código, por lo que tener conocimientos básicos de programación te será de gran ayuda. ¡Es una excelente oportunidad para aprender!",
        },
        {
            "question": "¿Tengo que usar un lenguaje de programación específico?",
            "answer": "No, puedes usar el lenguaje de programación que prefieras. La belleza de Advent of Code es que es agnóstico al lenguaje.",
        },
        {
            "question": "¿Tengo que pertenecer a una comunidad para participar?",
            "answer": "Sí, para que tus puntos cuenten para la competencia, necesitas unirte a una de las comunidades participantes. Esto nos ayuda a fomentar la colaboración y el espíritu de equipo.",
        },
        {
            "question": "¿Qué pasa si me uno a la mitad del evento?",
            "answer": "¡No hay problema! Puedes unirte en cualquier momento. Aún podrás resolver los retos de los días anteriores y sumar puntos para tu comunidad.",
        },
    ]
