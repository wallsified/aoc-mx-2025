import reflex as rx
from app.components.description import description_section
from app.components.advent import advent_section
from app.components.communities import communities_section
from app.components.rules import rules_section
from app.components.requirements import requierements_section
from app.components.faq import faq_section
from app.components.footer import footer


def index() -> rx.Component:
    """Página principal completamente estática."""
    return rx.el.main(
        description_section(),
        rx.el.hr(class_name="border-t border-gray-700 my-2"),
        advent_section(),
        rx.el.hr(class_name="border-t border-gray-700 my-2"),
        communities_section(),
        rx.el.hr(class_name="border-t border-gray-700 my-2"),
        requierements_section(),
        rx.el.hr(class_name="border-t border-gray-700 my-2"),
        rules_section(),
        rx.el.hr(class_name="border-t border-gray-700 my-2"),
        faq_section(),
        footer(),
        class_name="font-['JetBrains_Mono'] bg-[#101935] min-h-screen",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.meta(charset="UTF-8"),
        rx.el.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        rx.el.meta(
            name="description",
            content="Advent of Code MX 2025 - El reto anual navideño de programación que une a las comunidades tech en México. Únete y mejora tus habilidades de programación.",
        ),
        rx.el.meta(
            name="keywords",
            content="Advent of Code, programming, Mexico, coding challenge, comunidades tech, programación, retos, navidad, desarrollo",
        ),
        rx.el.meta(property="og:title", content="Advent of Code MX 2025"),
        rx.el.meta(
            property="og:description",
            content="El reto anual navideño de programación que une a las comunidades tech en México",
        ),
        rx.el.meta(property="og:type", content="website"),
        rx.el.meta(property="og:locale", content="es_MX"),
        rx.el.meta(name="twitter:card", content="summary_large_image"),
        rx.el.meta(name="twitter:title", content="Advent of Code MX 2025"),
        rx.el.meta(
            name="twitter:description",
            content="El reto anual navideño de programación que une a las comunidades tech en México",
        ),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(rel="icon", type="image/x-icon", href="/favicon.ico"),
        rx.el.meta(name="theme-color", content="#101935"),
        rx.el.meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no",
        ),
    ],
    stylesheets=[],
)
app.add_page(
    index,
    route="/",
    title="Advent of Code MX 2025 | Reto de Programación Navideño",
    description="Únete al reto anual navideño de programación que une a las comunidades tech en México. Mejora tus habilidades y diviértete programando.",
    meta=[
        {"name": "robots", "content": "index, follow"},
        {"name": "author", "content": "Sudo FCiencias"},
        {"name": "language", "content": "Spanish"},
    ],
)