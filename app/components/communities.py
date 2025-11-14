import reflex as rx
from app.states.landing_state import LandingState


def community_card(community: rx.Var[dict]) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.img(
                src=community["logo_src"],
                alt=community["name"],
                class_name="h-16 w-16 object-contain",
            ),
            class_name="bg-white rounded-2xl p-6 flex items-center justify-center h-32 w-full transition-transform duration-300 ease-in-out hover:scale-105 hover:shadow-2xl hover:shadow-[#DCF763]/20",
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
                "Conoce a las comunidades que hacen posible este evento.",
                class_name="text-lg text-gray-400 text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(LandingState.communities, community_card),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6",
            ),
            class_name="max-w-6xl mx-auto px-4 py-16",
        )
    )