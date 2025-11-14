import reflex as rx


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                rx.el.span("¡Bienvenido a "),
                rx.el.span("Advent of Code MX 2025!", class_name="text-[#DD7230]"),
                class_name="text-5xl md:text-7xl font-bold text-white mb-6 text-center flex flex-col items-center",
            ),
            rx.el.p(
                """El reto anual navideño de programación 
 que une a las comunidades tech de México.""",
                class_name="text-xl text-gray-300 max-w-3xl mx-auto text-center mb-8",
            ),
            rx.el.div(
                rx.el.p(
                    "Advent of Code MX es una iniciativa para fomentar la práctica de la programación y la resolución de problemas a través de los retos diarios de ",
                    rx.el.a(
                        "Advent of Code",
                        href="https://adventofcode.com/",
                        target="_blank",
                        class_name="text-[#DCF763] font-semibold underline hover:text-[#DD7230] transition-colors",
                    ),
                    ". Nuestro objetivo es crear un espacio de aprendizaje colaborativo, fortalecer los lazos entre comunidades y, sobre todo, ¡divertirnos programando!",
                    class_name="text-lg text-gray-400 max-w-4xl mx-auto text-center leading-relaxed",
                ),
                class_name="bg-black bg-opacity-20 p-8 rounded-2xl border border-gray-800",
            ),
            class_name="container mx-auto px-4 py-16",
        )
    )