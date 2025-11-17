import reflex as rx
from app.components.description import description_section
from app.components.advent import advent_section
from app.components.communities import communities_section
from app.components.rules import rules_section
from app.components.requirements import requierements_section
from app.components.faq import faq_section
from app.components.footer import footer


def index() -> rx.Component:
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
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    route="/",
    title="Advent of Code MX 2025",
    description="Advent of Code MX 2025",
)
