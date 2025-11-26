import reflex as rx


def icon_stack() -> rx.Component:
    return rx.hstack(
        rx.text("{", class_name="text-15xl"),
        rx.icon("tree-pine", size=90, color="white"),
        rx.icon("snowflake", size=90, color="white"),
        rx.text("}", class_name="text-15xl"),
        align="center",
    )


def header() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                icon_stack(),
                rx.el.p(".", class_name="text-[#1d351f] text-lg"),
                rx.el.span("""Información para Participantes
"""),
                rx.el.span("Posadas de Código", class_name="text-[#e6be9a]"),
                class_name="text-5xl md:text-7xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            rx.el.div(
                rx.el.p(
                    "Aqui está la información que necesitas conocer participar en el evento: como crear tu cuenta, como entrar a un lobby, etc. ",
                    "Cualquier otra duda que tengas que este o no aquí puedes contactarnos y la resolveremos.",
                    class_name="text-xl text-white-200 max-w-3xl mx-auto text-center leading-relaxed",
                ),
                class_name="bg-opacity-20 p-6 rounded-2xl",
            ),
            class_name="container mx-auto px-4 py-18",
        ),
    )
