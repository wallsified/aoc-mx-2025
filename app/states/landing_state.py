import reflex as rx
from typing import TypedDict


class Community(TypedDict):
    name: str
    logo_src: str
    url: str


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
            "logo_src": "/logos/guayabadevs.png",
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
    ]
