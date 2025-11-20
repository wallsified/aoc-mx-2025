import reflex as rx
from app.atoms.social_links import socials


def icon_stack() -> rx.Component:
    # Aqui, curiosamente, los corchetes no se alinean. 
    return rx.flex(
        #rx.el.h3("{", class_name="text-lg text-center font-semibold text-white mb-4"),
        rx.icon("tree-pine", size=25, color="white"),
        rx.icon("snowflake", size=25, color="white"),
        #rx.el.h3("}", class_name="text-lg font-semibold text-white mb-4"),
        align="center",
    )


def mobile_footer() -> rx.Component:
    return rx.el.footer(
        rx.mobile_only(
            rx.el.div(
                rx.el.hr(class_name="border-t border-white-700 my-8"),
                rx.el.div(
                    rx.el.div(
                        rx.vstack(
                            icon_stack(),
                            rx.el.h3(
                                "Posadas de Código",
                                class_name="text-center text-lg font-semibold text-white mb-4",
                            ),
                            align="center",
                        ),
                        rx.el.p(
                            "Resolviendo retos de programación, una comunidad a la vez.",
                            class_name="text-white-300, text-center text-lg",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Contacto",
                            class_name="text-center text-lg font-semibold text-white mb-4",
                        ),
                        socials(),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "© 2025 Sudo FCiencias",
                            class_name="text-center text-white mb-4",
                        ),
                    ),
                    class_name="grid gap-8 text-center md:text-left",
                ),
                class_name="max-w-6xl mx-auto px-4 py-8",
            )
        )
    )
