import reflex as rx
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
    {"name": "RustMX", "logo_src": "/logos/rustmx.jpg", "url": "https://t.me/RustMX"},
]


def community_card(community: Community) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.img(
                src=community["logo_src"],
                alt=community["name"],
                class_name="h-31 w-31 object-contain",
            ),
            class_name=f"bg-white rounded-3xl p-3 flex items-center justify-center h-31 w-full transition-transform duration-300 ease-in-out hover:scale-105 hover:shadow-2xl hover:shadow-[#DCF763]/15",
        ),
        href=community["url"],
        target="_blank",
        rel="noopener noreferrer",
    )


def communities_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Comunidades Participantes",
                class_name="text-4xl font-bold text-white text-center mb-4",
            ),
            rx.el.p(
                "Conoce a las comunidades que harán posible este evento.",
                class_name="text-lg text-gray-400 text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(communities, community_card),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6",
            ),
            class_name="max-w-6xl mx-auto px-4 py-16",
        )
    )
