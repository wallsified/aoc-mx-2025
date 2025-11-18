import reflex as rx
from app.atoms.link import link


def description_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                rx.el.span("""¡Bienvenido a 
"""),
                rx.el.span("Advent of Code MX 2025!", class_name="text-[#DD7230]"),
                class_name="text-5xl md:text-7xl font-bold text-white mb-6 text-center flex flex-col items-center",
            ),
            rx.el.p(
                rx.el.span("El reto anual navideño de programación"),
                rx.el.span("""
que une a las comunidades tech en México"""),
                class_name="text-xl text-gray-300 max-w-3xl mx-auto text-center mb-8",
            ),
            rx.el.div(
                rx.el.p(
                    "Advent of Code MX es una iniciativa para fomentar la práctica de la programación y la resolución de problemas a través de los retos diarios de ",
                    link(
                        "Advent of Code",
                        href="https://adventofcode.com/",
                    ),
                    ". Nuestro objetivo es crear un espacio de aprendizaje colaborativo, fortalecer los lazos entre comunidades y, sobre todo, ¡divertirnos programando!",
                    class_name="text-lg text-gray-400 max-w-4xl mx-auto text-center leading-relaxed",
                ),
                class_name="bg-black bg-opacity-20 p-8 rounded-2xl border border-gray-800",
            ),
            class_name="container mx-auto px-4 py-16",
        )
    )
