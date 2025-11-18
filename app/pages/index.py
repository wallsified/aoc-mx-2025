import reflex as rx
from app.sections.description import description_section
from app.sections.advent import advent_section
from app.sections.communities import communities_section
from app.sections.rules import rules_section
from app.sections.requirements import requierements_section
from app.sections.faq import faq_section
from app.sections.footer import footer


@rx.page(
    route="/",
    title="AdventMX 2025",
    description="Únete al reto anual navideño de programación que une a las comunidades tech en México. Mejora tus habilidades y diviértete programando.",
    meta=[
        {"name": "robots", "content": "index, follow"},
        {"name": "author", "content": "Sudo FCiencias"},
        {"name": "language", "content": "Spanish"},
    ],
)
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
