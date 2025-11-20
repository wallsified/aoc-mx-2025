import reflex as rx
from app.atoms.link import link


def description_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                rx.icon("tree-pine", size=90, color="white"),
                rx.el.p(".", class_name="text-[#1d351f] text-lg"),
                rx.el.span("""¡Bienvenidx a las
"""),
                rx.el.span("Posadas de Código!", class_name="text-[#e6be9a]"),
                class_name="text-5xl md:text-7xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            rx.el.p(
                rx.el.span("En el nombre del cielo,"),
                rx.el.span("""
os pido un programa..."""),
                class_name="italic text-xl text-white-200 max-w-3xl mx-auto text-center mb-8",
            ),
            rx.el.div(
                rx.el.p(
                    "Las Posadas de Código es una iniciativa para fomentar la práctica de la programación y la resolución de problemas a través de los retos diarios de ",
                    link(
                        "Advent of Code",
                        href="https://adventofcode.com/",
                    ),
                    ". Nuestro objetivo es crear un espacio de aprendizaje colaborativo, fortalecer los lazos entre las comunidades tech mexicanas y, sobre todo, ¡divertirnos programando!",
                    class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
                ),
                class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
            ),
            class_name="container mx-auto px-4 py-18",
        ),
    )
