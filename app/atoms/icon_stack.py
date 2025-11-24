from reflex import text, hstack, Component, icon


def icon_stack(size: int) -> Component:
    return hstack(
        text("{", class_name="text-15xl"),
        icon("tree-pine", size=size, color="white"),
        icon("snowflake", size=size, color="white"),
        text("}", class_name="text-15xl"),
        align="center",
    )
