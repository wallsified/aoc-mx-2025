from reflex import el, Component


def link(text: str, href: str) -> Component:
    # Componente modificado para tener la misma base para todos los links.
    return el.a(
        f"{text}",
        href=href,
        target="_blank",
        class_name="text-[#e6be9a] font-semibold hover:text-[#6f0f11] transition-colors",
    )
