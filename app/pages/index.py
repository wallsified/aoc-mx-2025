import reflex as rx
from app.sections.index.description import description_section
from app.sections.index.advent import advent_section
from app.sections.index.communities import communities_section
from app.sections.index.rules import rules_section
from app.sections.index.requirements import requierements_section
from app.sections.index.faq import faq_section
from app.sections.index.retos import day_cards_section
from app.atoms.desktop_footer import desktop_footer
from app.atoms.mobile_footer import mobile_footer
from app.wraps.snow import snow
from app.atoms.navbar import navbar
from app.atoms.top_banner import top_banner


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
        top_banner(),
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
