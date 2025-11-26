from typing import TypedDict


class Requirement(TypedDict):
    number: str
    requirement: str
    description: str


requirements: list[Requirement] = [
    {
        "number": "01",
        "requirement": "Únete a una Comunidad",
        "description": "Cada comunidad tiene su forma de unirse. Es importante pertenecer a una para saber a donde va tu puntaje.",
    },
    {
        "number": "02",
        "requirement": "Únete al lobby correcto",
        "description": "Debes unirte al de tu comunidad elegida para que tu partipación cuente. Revisa con tu comunidad el ID de lobby correcto.",
    },
    {
        "number": "03",
        "requirement": "Resuelve el reto",
        "description": "Puedes resolverlo en el lenguaje en el que mejor te acomodes. ¡No estás limitado a uno específico!",
    },
    {
        "number": "04",
        "requirement": "Valida tu solución",
        "description": "Cada reto tiene una sola solución. ¡Y solo las correctas cuentan!",
    },
    {
        "number": "05",
        "requirement": "Y el ganador es....",
        "description": "Al final del torneo sabremos quien ganó por comunidad y en general. ¡Cada ejercicio cuenta!",
    },
    # faltan más reglas evidentemente.
]
