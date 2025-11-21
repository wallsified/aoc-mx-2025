from reflex import Component, el
from app.atoms.day_item import day_cards


def day_cards_section() -> Component:
    return el.section(
        el.div(
            el.h2(
                "Consulta el reto del día aquí",
                class_name="text-4xl font-bold text-white text-center mb-4",
            ),
            el.p(
                "Si el link aun no lleva al reto, es por que aún no ha sido liberado",
                class_name="text-lg text-white-400 text-center mb-12",
            ),
            day_cards(),
            class_name="max-w-3xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
