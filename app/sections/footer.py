import reflex as rx
from app.atoms.link_alt import link_alt


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.hr(class_name="border-t border-gray-700 my-8"),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Advent of Code MX",
                        class_name="text-lg font-semibold text-white mb-4",
                    ),
                    rx.el.p(
                        "Resolviendo retos de programación, una comunidad a la vez.",
                        class_name="text-gray-400 text-sm",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Enlaces", class_name="text-lg font-semibold text-white mb-4"
                    ),
                    rx.el.ul(
                        rx.el.li(
                            link_alt(
                                "Repositorio GitHub",
                                href="https://github.com/null",
                            )
                        ),
                        rx.el.li(
                            link_alt(
                                "Advent of Code Oficial",
                                href="https://adventofcode.com/",
                            )
                        ),
                        class_name="space-y-2",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Contacto", class_name="text-lg font-semibold text-white mb-4"
                    ),
                    link_alt(
                        "sudofciencias@gmail.com",
                        href="mailto:sudofciencias@gmail.com",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8 text-center md:text-left",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2025 Sudo FCiencias.",
                    class_name="text-center text-xs text-gray-500 mt-8",
                )
            ),
            class_name="max-w-6xl mx-auto px-4 py-8",
        )
    )
