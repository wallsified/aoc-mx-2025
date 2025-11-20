import reflex as rx
from app.atoms.link import link


def advent_section() -> rx.Component:
    return rx.section(
        rx.el.h2(
            "¿Qué es el Advent of Code?",
            class_name="text-4xl font-bold text-white text-center mb-12",
        ),
        rx.el.div(
            rx.el.p(
                link(
                    "Advent of Code",
                    href="https://adventofcode.com/",
                ),
                " es un calendario de adviento con pequeños acertijos de programación para distintos niveles de habilidad que se pueden resolver en cualquier lenguaje de programación que se desee. La idea original es de ",
                link(
                    "Eric Wastl",
                    href="https://was.tl/",
                ),
                ". La idea es que puedas ocupar estos retos para mejorar tus habilidades de programación y que te pueda servir para entrevistas, hackatones, etc.",
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
        ),
        class_name="container mx-auto px-4 py-16",
    )
