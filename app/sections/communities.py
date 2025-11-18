import reflex as rx
from app.info.communities import communities
from app.atoms.community_card import community_card


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
