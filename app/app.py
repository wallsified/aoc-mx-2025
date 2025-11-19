from reflex import el, App, theme
from app.pages.index import index

app = App(
    theme=theme(appearance="dark"),
    head_components=[
        el.meta(charset="UTF-8"),
        el.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        el.meta(
            name="description",
            content="Advent of Code MX 2025 - El reto anual navideño de programación que une a las comunidades tech en México. Únete y mejora tus habilidades de programación.",
        ),
        el.meta(
            name="keywords",
            content="Advent of Code, programming, Mexico, coding challenge, comunidades tech, programación, retos, navidad, desarrollo",
        ),
        el.meta(property="og:title", content="Advent of Code MX 2025"),
        el.meta(
            property="og:description",
            content="El reto anual navideño de programación que une a las comunidades tech en México",
        ),
        el.meta(property="og:type", content="website"),
        el.meta(property="og:locale", content="es_MX"),
        el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        el.link(
            href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap",
            rel="stylesheet",
        ),
        el.link(rel="icon", type="image/x-icon", href="/favicon.ico"),
        el.meta(name="theme-color", content="#101935"),
        el.meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no",
        ),
    ],
    enable_state=False
)