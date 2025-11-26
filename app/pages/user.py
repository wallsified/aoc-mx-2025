import reflex as rx
from app.sections.user.header import header
from app.sections.user.questions import user_info
from app.atoms.desktop_footer import desktop_footer
from app.atoms.mobile_footer import mobile_footer
from app.atoms.navbar import navbar
from app.wraps.snow import snow
from app.atoms.top_banner import top_banner


@rx.page(
    route="/user-info",
    title="PcD | Info. Participantes",
    description="¿Vas a participar en PcD? Esta información es para ti.",
    meta=[
        {"name": "author", "content": "Sudo FCiencias"},
        {"name": "language", "content": "Spanish"},
    ],
)
def community_info() -> rx.Component:
    return rx.el.main(
        snow(),
        top_banner(),
        navbar(),
        header(),
        user_info(),
        rx.mobile_only(mobile_footer()),
        rx.tablet_and_desktop(desktop_footer()),
        class_name="font-['Red_Hat_Text'] bg-[#1d351f] min-h-screen",
    )
