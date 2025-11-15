import reflex as rx


def faq_answer(answer: str) -> rx.Component:
    return rx.list.item(
        rx.el.p(answer, class_name="text-gray-300"),
    )


def faq_question(question: str, answer: rx.Component) -> rx.Component:
    return rx.list.item(
        rx.icon("dot", color="#DD7230"),
        rx.el.p(question, class_name="font-bold text-[#DD7230]"),
        # aquí debería haber un salto de linea o algo parecido
        rx.el.p(f"{answer}", class_name="text-gray-300"),
        class_name="bg-black bg-opacity-20 p-6 rounded-lg border border-gray-800 flex items-start gap-4",
    )


def faq_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Preguntas Frecuentes",
                class_name="text-4xl font-bold text-white text-center mb-12",
            ),
            rx.el.div(
                faq_question("how are we supposed to do that? \n", "like this"),
            ),
            class_name="max-w-6xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
