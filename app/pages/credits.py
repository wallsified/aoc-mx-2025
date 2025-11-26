import reflex as rx
from app.atoms.desktop_footer import desktop_footer
from app.atoms.mobile_footer import mobile_footer
from app.wraps.snow import snow
from app.atoms.navbar import navbar
from app.atoms.link import link
from app.atoms.icon_stack import icon_stack
from app.atoms.top_banner import top_banner


def header() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                icon_stack(70),
                rx.el.p(".", class_name="text-[#1d351f] text-lg"),
                rx.el.span("""Créditos"""),
                rx.el.span("Posadas de Código", class_name="text-[#e6be9a]"),
                class_name="text-5xl md:text-6xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            rx.el.p(
                rx.el.span(
                    "Por que nada de esto seria posible sin el trabajo de otros desarrolladores."
                ),
                class_name="text-xl text-white-200 max-w-3xl mx-auto text-center mb-8",
            ),
            rx.el.div(
                rx.list(
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "Posadas de Código está sobre hombros de gigantes. Y el principal de ellos es ",
                        link("Eric Wastl", "https://was.tl/"),
                        " . Sin él, nada de esto seria posible. Todo lo referente a ",
                        link("Advent of Code", "https://adventofcode.com/2025/about"),
                        " es de su completa y total autoria.",
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "El código fuente que nos permite juntar los leaderboards de cada comunidad es creación de ",
                        link("Sergio de Carvalho", "https://github.com/scarvalhojr"),
                        " y de ",
                        link("Tatu Pesonen ", "https://github.com/tatupesonen"),
                        " . El repo de éste código está alojado en este ",
                        link("repo.", "https://github.com/scarvalhojr/aocleaderboard"),
                    ),
                    rx.list.item(
                        rx.icon("dot", size=30, color="white"),
                        "El código de la página para Posadas de Código, asi como su semblanza, aunque es propiedad de ",
                        link("Sudo FCiencias", "https://linktr.ee/sudo_fciencias"),
                        ", está disponible al mundo en este ",
                        link("repo.", "https://github.com/wallsified/aoc-mx-2025"),
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
    route="/creditos",
    title="PcD | Créditos",
    description="Los créditos de lo usado para realizar Posadas de Código.",
    meta=[
        {"name": "author", "content": "Sudo FCiencias"},
        {"name": "language", "content": "Spanish"},
    ],
)
def credits() -> rx.Component:
    return rx.el.main(
        snow(),
        top_banner(),
        navbar(),
        header(),
        rx.mobile_only(mobile_footer()),
        rx.tablet_and_desktop(desktop_footer()),
        class_name="font-['Red_Hat_Text'] bg-[#1d351f] min-h-screen",
    )
