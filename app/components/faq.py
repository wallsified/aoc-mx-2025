import reflex as rx
from typing import TypedDict


class Faq(TypedDict):
    question: str
    answer: str


faqs: list[Faq] = [
    {
        "question": "¿Necesito saber programar para participar?",
        "answer": "No es estrictamente necesario, pero sí recomendable. Los retos de Advent of Code están diseñados para ser resueltos con código, por lo que tener conocimientos básicos de programación te será de gran ayuda. ¡Es una excelente oportunidad para aprender!",
    },
    {
        "question": "¿Tengo que usar un lenguaje de programación específico?",
        "answer": "No, puedes usar el lenguaje de programación que prefieras. La belleza de Advent of Code es que es agnóstico al lenguaje.",
    },
    {
        "question": "¿Tengo que pertenecer a una comunidad para participar?",
        "answer": "Sí, para que tus puntos cuenten para la competencia, necesitas unirte a una de las comunidades participantes. Esto nos ayuda a fomentar la colaboración y el espíritu de equipo.",
    },
    {
        "question": "¿Qué pasa si me uno a la mitad del evento?",
        "answer": "¡No hay problema! Puedes unirte en cualquier momento. Aún podrás resolver los retos de los días anteriores y sumar puntos para tu comunidad.",
    },
]


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
            rx.el.div(rx.foreach(faqs, faq_item), class_name="flex flex-col gap-4"),
            class_name="max-w-3xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
