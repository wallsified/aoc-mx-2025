from reflex import el, Component


def link_alt(text: str, href: str) -> Component:
    return el.a(
        f"{text}",
        href=href,
        target="_blank",
        class_name="text-sm text-white-400 hover:text-[#6f0f11] transition-colors",
    )
