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
    {
        "question": "¿Puedo usar IA para resolver los retos?",
        "answer": "La respuesta corta es no. Pero también sabemos que no podemos evitar que no lo hagas. Recuerda que el reto es por el afán de aprender, no por ganar.",
    },
]
