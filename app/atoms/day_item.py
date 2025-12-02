from reflex import Component, el, grid, foreach, Var
from app.atoms.link_alt import link_alt

base_link = "https://adventofcode.com/2025/day/"


def day_card_unit(text: str, href: str) -> Component:
    return el.div(
        el.p(
            link_alt(
                text=text,
                href=href,
            ),
            class_name="text-xl text-white-200 max-w-xl mx-auto text-center leading-relaxed",
        ),
        class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
    )


def day_cards() -> Component:
    return grid(
        foreach(
            Var.range(12),
            lambda i: day_card_unit(
                text=f"Día {i + 1}/12", href=base_link + f"{i + 1}"
            ),
        ),
        columns="3",
        spacing="4",
        width="100%",
    )
