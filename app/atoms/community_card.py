from reflex import el, Component
from app.info.communities import Community


def community_card(community: Community) -> Component:
    return el.a(
        el.div(
            el.img(
                src=community["logo_src"],
                alt=community["name"],
                class_name="h-44 w-44 object-contain",
            ),
            class_name=f"bg-white rounded-3xl p-3 flex items-center justify-center h-full w-full transition-transform duration-300 ease-in-out hover:scale-110 hover:shadow-2xl hover:shadow-[#e6be9a]/20",
        ),
        href=community["url"],
        target="_blank",
        rel="noopener noreferrer",
    )
