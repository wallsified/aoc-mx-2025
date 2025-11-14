import reflex as rx


def rule_item(number: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(number, class_name="text-xl font-bold text-[#DCF763]"),
        rx.el.p(text, class_name="text-gray-300"),
        class_name="bg-black bg-opacity-20 p-6 rounded-lg border border-gray-800 flex items-start gap-4",
    )


def rules_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Reglas de la Competición",
                class_name="text-4xl font-bold text-white text-center mb-12",
            ),
            rx.el.div(
                rule_item(
                    "01",
                    "Respeto y Colaboración: Todos los participantes deben mantener un ambiente de respeto. Se anima la colaboración, pero las soluciones finales deben ser individuales.",
                ),
                rule_item(
                    "02",
                    "No al Plagio: Las soluciones deben ser originales. Copiar código de otros participantes o de fuentes no autorizadas resultará en descalificación.",
                ),
                rule_item(
                    "03",
                    "Una cuenta por participante: Cada participante debe usar una única cuenta para enviar sus soluciones durante todo el evento.",
                ),
                rule_item(
                    "04",
                    "¡Diviértete y Aprende!: El objetivo principal es aprender, mejorar tus habilidades y divertirte. ¡Disfruta el reto!",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
            ),
            class_name="max-w-6xl mx-auto px-4 py-16",
        ),
        class_name="w-full",
    )
