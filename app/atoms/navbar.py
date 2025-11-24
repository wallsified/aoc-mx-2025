import reflex as rx


def link_alt(text: str, href: str) -> rx.Component:
    return rx.el.a(
        f"{text}",
        href=href,
        target="_blank",
        class_name="text-lg text-white-600 font-semibold hover:text-[#6f0f11] transition-colors",
    )


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


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                icon_stack(),
                rx.spacer(),
                rx.hstack(
                    rx.hstack(
                        link_alt("Home", "https://www.posadasdecodigo.com/"),
                        link_alt("Créditos", "/#"),
                        link_alt("Agradecimientos", "/#"),
                        justify="end",
                        spacing="5",
                    ),
                    justify="between",
                    align_items="right",
                ),
                align_items="right",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=25)),
                    rx.menu.content(
                        link_alt("Home", "https://www.posadasdecodigo.com/"),
                        link_alt("Creditos", "/#"),
                        link_alt("Agradecimientos", "/#"),
                    ),
                    justify="end",
                    color_scheme="green",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg="#1d351f",
        padding="2em",
        # position="fixed",
        top="10px",
        # z_index="5",
        width="100%",
    )
