import reflex as rx
from app.sections.description import description_section
from app.sections.advent import advent_section
from app.sections.communities import communities_section
from app.sections.rules import rules_section
from app.sections.requirements import requierements_section
from app.sections.faq import faq_section
from app.sections.retos import day_cards_section
from app.atoms.desktop_footer import desktop_footer
from app.atoms.mobile_footer import mobile_footer
from app.wraps.snow import snow
from app.atoms.navbar import navbar


@rx.page(
    route="/",
    title="Posadas de Código",
    description="Únete al reto anual navideño de programación que une a las comunidades tech en México. Mejora tus habilidades y diviértete programando.",
    meta=[
        {"name": "author", "content": "Sudo FCiencias"},
        {"name": "language", "content": "Spanish"},
    ],
)
def index() -> rx.Component:
    return rx.el.main(
        snow(),
        navbar(),
        description_section(),
        advent_section(),
        communities_section(),
        requierements_section(),
        rules_section(),
        day_cards_section(),
        faq_section(),
        rx.mobile_only(mobile_footer()),
        rx.tablet_and_desktop(desktop_footer()),
        class_name="font-['Red_Hat_Text'] bg-[#1d351f] min-h-screen",
    )
