import reflex as rx
from app.atoms.rule_item import rule_item
from app.info.rules import rules


def rules_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Reglas de la Competencia",
                class_name="text-4xl font-bold text-white text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(rules, rule_item),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
            ),
            class_name="max-w-6xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
