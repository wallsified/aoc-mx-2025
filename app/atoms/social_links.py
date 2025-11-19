# Tomadas prestadas de las recipies oficiales de Reflex.
# La "receta" original se encuentra aquí: https://reflex.dev/docs/recipes/layout/footer/

import reflex as rx


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon, stroke_width=2, size=20, color="white"), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("github", "https://github.com/orgs/Sudo-FCiencias"),
        social_link("instagram", "https://instagram.com/sudo_fciencias"),
        social_link("send", "https://t.me/+5HauBpACCEU5OTQx"),
        # social_link("linkedin", "https://linkedin.com/company/sudo-fciencias/"),
        social_link("youtube", "https://www.youtube.com/@SudoFCiencias"),
        social_link("mail", "mailto:sudofciencias@gmail.com"),
        spacing="5",
        justify_content=["center", "center", "end"],
        width="100%",
        class_name="",
    )
