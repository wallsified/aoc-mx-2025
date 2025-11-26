import reflex as rx

# No pienso ni mentir ni esconderlo: no tenia idea de como hacer esto
# de manera stateless y que funcionara sin backend o estados, asi que
# el reflex-bot se lo improvisó.


def top_banner() -> rx.Component:
    return rx.fragment(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "{",
                        rx.icon(
                            "tree-pine",
                            class_name="h-5 w-5 text-white mr-1 text-center fg-[#e6be9a]",
                        ),
                        rx.icon(
                            "snowflake",
                            class_name="h-5 w-5 text-white mr-1 text-center fg-[#e6be9a]",
                        ),
                        "}",
                        class_name="px-2 py-1 flex items-center shrink-0",
                    ),
                    rx.el.p(
                        "¡IDs de lobbys disponibles a partir del 27/11/25!",
                        class_name="text-white text-md font-semibold truncate",
                    ),
                    class_name="flex items-center justify-center flex-1 min-w-0",
                ),
                rx.el.button(
                    rx.icon("x", class_name="h-5 w-5"),
                    on_click=rx.call_script(
                        "document.getElementById('top-banner').style.display = 'none'; localStorage.setItem('banner_hidden', 'true');"
                    ),
                    class_name="text-white/70 hover:text-white bg-white/10 hover:bg-white/20 rounded-full p-1.5 transition-all duration-200 ml-4 shrink-0 flex items-center justify-center",
                ),
                class_name="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between",
            ),
            class_name="w-full bg-[#325832] border-b border-white/10 shadow-sm animate-fade-in",
            id="top-banner",
        ),
        rx.script("""
            if (localStorage.getItem('banner_hidden') === 'true') {
                const banner = document.getElementById('top-banner');
                if (banner) {
                    banner.style.display = 'none';
                }
            }
            """),
    )
