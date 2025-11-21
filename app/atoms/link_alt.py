from reflex import el, Component, icon, hstack


def link_alt(text: str, href: str) -> Component:
    return hstack(
        icon("calendar-days", size=30, color="#e6be9a"),
        el.a(
            f"{text}",
            href=href,
            target="_blank",
            class_name="text-xl text-white-600 hover:text-[#6f0f11] transition-colors",
        ),
        spacing="3",
        align="center",
        direction="row",
        justify="center",
        wrap="wrap",
    )
