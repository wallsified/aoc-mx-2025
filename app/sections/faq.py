from reflex import Component, el, foreach
from app.atoms.faq_item import faq_item
from app.info.faqs import faqs


def faq_section() -> Component:
    return el.section(
        el.div(
            el.h2(
                "Preguntas Frecuentes",
                class_name="text-4xl font-bold text-white text-center mb-12",
            ),
            el.div(foreach(faqs, faq_item), class_name="flex flex-col gap-4"),
            class_name="max-w-3xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
