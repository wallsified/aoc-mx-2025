from reflex import el, Component, divider
from app.info.requirements import Requirement


def requirements_item(req: Requirement) -> Component:
    return el.div(
        el.div(req["number"], class_name="text-3xl font-bold text-[#e6be9a]"),
        el.p(req["requirement"], class_name="text-lg font-semibold text-white"),
        divider(size="4", orientation="vertical", decorative=True, color_scheme="gray"),
        el.p(req["description"], class_name="text-white-300 text-lg"),
        class_name="bg-[#325832] bg-opacity-20 p-6 rounded-lg border border-white-800 flex items-start gap-4",
    )
