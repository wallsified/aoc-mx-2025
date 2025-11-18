from reflex import el, Component, divider
from app.info.requirements import Requirement


def requirements_item(req: Requirement) -> Component:
    return el.div(
        el.div(req["number"], class_name="text-2xl font-bold text-[#DD7230]"),
        el.p(req["requirement"], class_name="text-lg font-semibold text-white"),
        divider(size="1", orientation="vertical", decorative=True, color_scheme="gray"),
        el.p(req["description"], class_name="text-gray-300"),
        class_name="bg-black bg-opacity-20 p-6 rounded-lg border border-gray-800 flex items-start gap-4",
    )
