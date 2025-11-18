from reflex import el, Component


def link_alt(text: str, href: str) -> Component:
    return el.a(
        f"{text}",
        href=href,
        target="_blank",
        class_name="text-sm text-gray-400 hover:text-[#DCF763] transition-colors",
    )
