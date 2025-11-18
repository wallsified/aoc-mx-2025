import reflex as rx
from app.info.requirements import requirements
from app.atoms.requirement_item import requirements_item


def requierements_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "¿Cómo participo?",
                class_name="text-4xl font-bold text-white text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(requirements, requirements_item),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
            ),
            class_name="max-w-6xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
