import reflex as rx


def requirements_item(number: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(number, class_name="text-xl font-bold text-[#DD7230]"),
        rx.el.p(text, class_name="text-gray-300"),
        class_name="bg-black bg-opacity-20 p-6 rounded-lg border border-gray-800 flex items-start gap-4",
    )


def requierements_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "¿Cómo participo?",
                class_name="text-4xl font-bold text-white text-center mb-12",
            ),
            rx.el.div(
                requirements_item(
                    "01",
                    "Únete a una Comunidad: Así sabremos cual es tu equipo y hacia donde irá tu puntaje. Revisa los enlaces de cada comunidad para hacerlo.",
                ),
                requirements_item(
                    "02",
                    "Haz fork del repo de tu comunidad: Así tendrás tu propia copia de los ejercicios para que puedas resolverlos.",
                ),
                requirements_item(
                    "03",
                    "Resuelve el ejercicio: Puedes resolverlo en el lenguaje en el que mejor te acomodes.",
                ),
                requirements_item(
                    "04",
                    "Subelo a tu Repo y haz una PR: Así tu solución se añadirá junto a las demás de tu comunidad.",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
            ),
            class_name="max-w-6xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )