import reflex as rx
from app.sections.community_info.header import header
from app.sections.community_info.questions import community_faqs
from app.atoms.desktop_footer import desktop_footer
from app.atoms.mobile_footer import mobile_footer
from app.wraps.snow import snow


@rx.page(
    route="/community-info",
    title="PcD | Info. Comunidades",
    description="¿Eres comunidad participante? Esta información es para ti.",
    meta=[
        {"name": "author", "content": "Sudo FCiencias"},
        {"name": "language", "content": "Spanish"},
    ],
)
def community_info() -> rx.Component:
    return rx.el.main(
        # snow(),
        header(),
        community_faqs(),
        rx.mobile_only(mobile_footer()),
        rx.tablet_and_desktop(desktop_footer()),
        class_name="font-['Red_Hat_Text'] bg-[#1d351f] min-h-screen",
    )
