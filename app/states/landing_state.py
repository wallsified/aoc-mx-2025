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
            "logo_src": "/placeholder.svg",
            "url": "https://linktr.ee/Sudo_FCiencias",
        },
        {
            "name": "PythonCDMX",
            "logo_src": "/placeholder.svg",
            "url": "https://pythoncdmx.org/",
        },
        {
            "name": "AWS Cloud Club UNAM",
            "logo_src": "/placeholder.svg",
            "url": "https://linktr.ee/aws_unam",
        },
        {
            "name": "Guayaba Devs",
            "logo_src": "/placeholder.svg",
            "url": "https://guayabadev.com/",
        },
        {
            "name": "Nebursaturn",
            "logo_src": "/placeholder.svg",
            "url": "https://www.instagram.com/nebursaturnacademy/",
        },
    ]