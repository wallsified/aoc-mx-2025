from typing import TypedDict


class Rule(TypedDict):
    number: str
    rule: str
    description: str


rules: list[Rule] = [
    {
        "number": "01",
        "rule": "Respeto y Colaboración",
        "description": "Todos los participantes deben mantener un ambiente de respeto. Se anima la colaboración, pero las soluciones finales deben ser individuales.",
    },
    {
        "number": "02",
        "rule": "No al Plagio",
        "description": "Las soluciones deben ser originales. Copiar código de otros participantes o de fuentes no autorizadas resultará en descalificación.",
    },
    {
        "number": "03",
        "rule": "Una comunidad por participante",
        "description": "Cada participante debe usar una única cuenta y jugar para una única comunidad para enviar sus soluciones durante todo el evento.",
    },
    {
        "number": "04",
        "rule": "¡Lo importante no es ganar!",
        "description": "El objetivo principal es aprender, mejorar tus habilidades y divertirte. ¡Disfruta el reto!",
    },
]
