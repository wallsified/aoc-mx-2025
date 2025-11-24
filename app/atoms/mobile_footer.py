import reflex as rx
from app.atoms.social_links import socials


def icon_stack() -> rx.Component:
    return rx.el.div(
        rx.flex(
            rx.el.h3(
                "{",
                class_name="text-left text-lg font-semibold text-white mb-4",
            ),
            rx.icon("tree-pine", size=25, color="white"),
            rx.icon("snowflake", size=25, color="white"),
            rx.el.h3(
                "}",
                class_name="text-left text-lg font-semibold text-white mb-4",
            ),
            # osea que reflex no procesa espacios en los textos, pero podemos esconder los espacios?
            rx.el.p("...", class_name="text-[#101935]"),
            rx.el.h3(
                "Posadas de Código",
                class_name="text-left text-lg font-semibold text-white mb-4",
            ),
            direction="row",
            gap="4",
            align="start",
        ),
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
