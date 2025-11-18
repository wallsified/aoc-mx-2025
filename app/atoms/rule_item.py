from reflex import Component, el, divider
from app.info.rules import Rule


def rule_item(rule: Rule) -> Component:
    return el.div(
        el.div(rule["number"], class_name="text-xl font-bold text-[#DCF763]"),
        el.p(rule["rule"], class_name="text-lg font-semibold text-white"),
        divider(size="1", orientation="vertical", decorative=True, color_scheme="gray"),
        el.p(rule["description"], class_name="text-gray-300"),
        class_name="bg-black bg-opacity-20 p-6 rounded-lg border border-gray-800 flex items-start gap-4",
    )
