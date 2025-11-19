from reflex import Component, el, divider
from app.info.rules import Rule


def rule_item(rule: Rule) -> Component:
    return el.div(
        el.div(rule["number"], class_name="text-xl font-bold text-[#DD7230]"),
        el.p(rule["rule"], class_name="text-lg font-semibold text-white"),
        divider(
            size="4", orientation="vertical", decorative=True, color_scheme="orange"
        ),
        el.p(rule["description"], class_name="text-gray-300"),
        class_name="bg-[#0c142a] bg-opacity-20 bg-opacity-20 p-6 rounded-lg border border-gray-800 flex items-start gap-4",
    )
