from reflex import el, Component, icon
from app.info.faqs import Faq


def faq_item(faq: Faq) -> Component:
    return el.div(
        el.details(
            el.summary(
                el.span(faq["question"], class_name="font-bold, text-xl"),
                el.span(
                    icon(
                        "chevron-down",
                        class_name="h-6 w-6 transition-transform duration-300",
                        color="white",
                    )
                ),
                class_name="flex w-full cursor-pointer list-none items-center justify-between",
            ),
            el.p(faq["answer"], class_name="text-white-300 pt-6 text-lg"),
            class_name="w-full",
        ),
        class_name="w-full bg-[#325832] bg-opacity-20 p-6 rounded-lg border border-white-800",
    )
