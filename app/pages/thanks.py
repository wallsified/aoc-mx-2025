import reflex as rx
from app.atoms.desktop_footer import desktop_footer
from app.atoms.mobile_footer import mobile_footer
from app.wraps.snow import snow
from app.atoms.navbar import navbar
from app.atoms.icon_stack import icon_stack
from app.atoms.link import link


def header() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                icon_stack(70),
                rx.el.p(".", class_name="text-[#1d351f] text-lg"),
                rx.el.span("""Agradecimientos"""),
                rx.el.span("Posadas de Código", class_name="text-[#e6be9a]"),
                class_name="text-5xl md:text-6xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            rx.el.p(
                rx.el.span(
                    "Por que nada de esto seria posible sin la ayuda de la comunidad."
                ),
                class_name="text-xl text-white-200 max-w-3xl mx-auto text-center mb-8",
            ),
            rx.el.div(
                rx.list(
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        " Principalmente, queremos agradecer a todas las personas que se unieron para participar en este evento. Ustedes son el corazón del evento y la razón por la que lo hacemos.",
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "A las comunidades que decidieron unirse para poder llegar aún a más gente para este torneo.",
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "El Equipo Sudo quiere agradecer en particular a ",
                        link("@pixelead0", "https://www.linkedin.com/in/pixelead0/"),
                        " por ser el principal impulsor y contacto con otras comunidades para el evento.",
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "El Equipo Sudo quiere agradecer en particular a ",
                        link("David Sol", "https://www.linkedin.com/in/soldavidcloud/"),
                        " por darnos el nombre y slogan para el evento.",
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "El Equipo Sudo quiere agradecer en particular a PUPZ por ser el pato de goma oficial para el desarrollo de la página.",
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "A todos los desarrolladores involucrados en Advent of Code y derivados que hacen que año con año el torneo global se pueda crear.",
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "Y de nuevo, a ti, que estás leeyendo esto, por querer ser un poco más superusuario .",
                    ),
                    list_style_type="none",
                    class_name="text-lg text-white-200",
                ),
                class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800, text-center",
            ),
            class_name="container mx-auto px-4 py-12",
        ),
    )


@rx.page(
    route="/agradecimientos",
    title="Pdc | Agradecimientos",
    description="Por que nada de esto seria posible sin la ayuda de la comunidad.",
    meta=[
        {"name": "author", "content": "Sudo FCiencias"},
        {"name": "language", "content": "Spanish"},
    ],
)
def thanks() -> rx.Component:
    return rx.el.main(
        snow(),
        navbar(),
        header(),
        rx.mobile_only(mobile_footer()),
        rx.tablet_and_desktop(desktop_footer()),
        class_name="font-['Red_Hat_Text'] bg-[#1d351f] min-h-screen",
    )
