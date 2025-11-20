from typing import TypedDict


class Rule(TypedDict):
    number: str
    rule: str
    description: str


rules: list[Rule] = [
    {
        "number": "01",
        "rule": "Se Respetuoso",
        "description": "Todxs lxs participantes deben mantener un ambiente de respeto. No permitimos actos de discriminación ni de violencia de ningún tipo.",
    },
    {
        "number" : "02",
        "rule": "Colaboración Limitada",
        "description": "Se anima la colaboración, pero tus soluciones finales deben ser individuales."
    },
    {
        "number": "03",
        "rule": "No al Plagio",
        "description": "Las soluciones deben ser originales. Copiar código de otros participantes o de fuentes no autorizadas resultará en descalificación.",
    },
    {
        "number": "04",
        "rule": "No uses multicuentas",
        "description": "Cada participante debe usar una única cuenta y jugar para una única comunidad para enviar sus soluciones durante todo el evento.",
    },
    {
        "number": "05",
        "rule": "¡Lo importante no es ganar!",
        "description": "El objetivo principal es aprender, mejorar tus habilidades y divertirte. ¡Disfruta el reto!",
    },
]
