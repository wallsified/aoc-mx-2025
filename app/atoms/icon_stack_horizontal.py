from reflex import el, flex, Component, icon


def icon_stack(size: int) -> Component:
    return el.div(
        flex(
            el.h3(
                "{",
                class_name="text-left text-lg font-semibold text-white mb-4",
            ),
            icon("tree-pine", size=size, color="white"),
            icon("snowflake", size=size, color="white"),
            el.h3(
                "}",
                class_name="text-left text-lg font-semibold text-white mb-4",
            ),
            # osea que reflex no procesa espacios en los textos, pero podemos esconder los espacios?
            el.p("...", class_name="text-[#101935]"),
            el.h3(
                "Posadas de Código",
                class_name="text-left text-lg font-semibold text-white mb-4",
            ),
            direction="row",
            gap="4",
            align="start",
        ),
    )
