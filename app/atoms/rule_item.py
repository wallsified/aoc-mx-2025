from reflex import Component, el, divider
from app.info.rules import Rule


def rule_item(rule: Rule) -> Component:
    return el.div(
        el.div(rule["number"], class_name="text-3xl font-bold text-[#e6be9a]"),
        el.p(rule["rule"], class_name="text-lg font-semibold text-white"),
        divider(
            # aqui la excepción de color es usar gray por que asi ya viene en reflex, no acepta "white".
            size="4",
            orientation="vertical",
            decorative=True,
            color_scheme="gray",
        ),
        el.p(rule["description"], class_name="text-white-300 text-lg"),
        class_name="bg-[#325832] bg-opacity-20 bg-opacity-20 p-6 rounded-lg border border-white-800 flex items-start gap-4",
    )
