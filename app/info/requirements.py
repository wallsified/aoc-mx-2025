from typing import TypedDict


class Requirement(TypedDict):
    number: str
    requirement: str
    description: str


requirements: list[Requirement] = [
    {
        "number": "01",
        "requirement": "Únete a una Comunidad",
        "description": "Cada comunidad tiene su forma de unirse. Es importante pertenecer a una para saber a donde va tu puntaje",
    },
    {
        "number": "02",
        "requirement": "Únete al lobby correcto",
        "description": "Debes unirte al de tu comunidad elegida para que tu partipación cuente.",
    },
    {
        "number": "03",
        "requirement": "Resuelve el ejercicio",
        "description": "Puedes resolverlo en el lenguaje en el que mejor te acomodes.",
    },
    # faltan más reglas evidentemente.
]
