import reflex as rx
from app.states.landing_state import LandingState, Faq


def faq_item(faq: Faq) -> rx.Component:
    return rx.el.div(
        rx.el.details(
            rx.el.summary(
                rx.el.span(faq["question"], class_name="font-bold text-[#DD7230]"),
                rx.el.span(
                    rx.icon(
                        "chevron-down",
                        class_name="h-6 w-6 transition-transform duration-300",
                    )
                ),
                class_name="flex w-full cursor-pointer list-none items-center justify-between",
            ),
            rx.el.p(faq["answer"], class_name="text-gray-300 pt-4"),
            class_name="w-full",
        ),
        class_name="w-full bg-black bg-opacity-20 p-6 rounded-lg border border-gray-800",
    )


def faq_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Preguntas Frecuentes",
                class_name="text-4xl font-bold text-white text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(LandingState.faqs, faq_item),
                class_name="flex flex-col gap-4",
            ),
            class_name="max-w-3xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
