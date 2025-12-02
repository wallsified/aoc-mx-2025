import reflex as rx
from app.atoms.icon_stack_horizontal import icon_stack


def link_alt(text: str, href: str) -> rx.Component:
    return rx.el.a(
        f"{text}",
        href=href,
        is_external=False,
        class_name="text-lg text-white-600 font-semibold hover:text-[#6f0f11] transition-colors",
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                icon_stack(25),
                rx.spacer(),
                rx.hstack(
                    rx.hstack(
                        link_alt("Home", "/#"),
                        link_alt(
                            "Leaderboard", "https://leaderboard.posadasdecodigo.com/"
                        ),
                        link_alt("Info. Participantes", "/user-info"),
                        link_alt("Créditos", "/creditos"),
                        link_alt("Agradecimientos", "/agradecimientos"),
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
                        link_alt("Home", "/#"),
                        link_alt(
                            "Leaderboard", "https://leaderboard.posadasdecodigo.com/"
                        ),
                        link_alt("Info. Participantes", "/user-info"),
                        link_alt("Creditos", "/creditos"),
                        link_alt("Agradecimientos", "/agradecimientos"),
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
