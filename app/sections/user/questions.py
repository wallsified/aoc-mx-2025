from reflex import el, Component, image
from app.atoms.link import link

# Esto seguramente tiene una manera mas elegante de hacerse, pero la verdad
# no tenemos tanto tiempo para averiguarlo.


def faq_image(src: str) -> Component:
    return image(
        src=src,
        border_radis="15px",
        class_name=" flex mx-auto max-w-5xl gap-x-4 block sm:shrink-0 sm:py-4",
    )


def step_one() -> Component:
    return el.section(
        el.div(
            el.h2(
                el.span(
                    "¿Cómo creo un perfil para el torneo?", class_name="text-white"
                ),
                class_name="text-xl md:text-2xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            el.div(
                el.p(
                    "Lo primero que debes hacer es acceder a la página de Advent of Code y, desde la sección de 'Login' "
                ),
                " crear tu cuenta. Recomendamos Google y GitHub para hacerlo. Puedes crear la cuenta accediendo desde",
                link(
                    text=" este link.",
                    href="https://adventofcode.com/2025/auth/login",
                ),
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/lobbies/community_login.png",
            ),
            el.div(
                el.p(
                    "Luego puedes ajustar la información del perfil. Puedes ocupar un pseudónimo o gamertag si lo prefieres. ",
                ),
                "Esto se hace desde la sección 'Settings', a la cual puedes acceder con  ",
                link(
                    text="este link.",
                    href="https://adventofcode.com/2025/settings",
                ),
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/lobbies/edit_profile.png",
            ),
            class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
        ),
        class_name="container mx-auto px-4 py-5",
    )


def step_two() -> Component:
    return el.section(
        el.div(
            el.h2(
                el.span(
                    "¿Cómo me uno al lobby de una comunidad?", class_name="text-white"
                ),
                class_name="text-xl md:text-2xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            el.div(
                el.p(
                    "Cada comunidad tiene un ID único, por lo que debes de tenerlo a la mano y escribirlo correctamente."
                ),
                "Este ID lo debes ingresar desde tu perfil en el recuadro negro al lado del botón que dice '[Join]'"
                " y luego presionar el botón. Una vez que hagas esto estarás participando por tu comunidad elegida."
                " Puedes ingresar el ID desde",
                link(
                    text=" este link ",
                    href="https://adventofcode.com/2025/leaderboard/private",
                ),
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/lobbies/joining_leaderboard.png",
            ),
            class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
        ),
        class_name="container mx-auto px-4 py-5",
    )


def step_three() -> Component:
    return el.section(
        el.div(
            el.h2(
                el.span("¿Cómo funciona el reto de cada día?", class_name="text-white"),
                class_name="text-xl md:text-2xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            el.div(
                el.p(
                    "Cada día, en el link correcto (revisa la paǵina principal) aparecerá la descripción y la información "
                ),
                "necesaria para cada reto. Esto se ve como en la imágen siguiente:",
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/user-info/challenge_info.png",
            ),
            el.div(
                el.p(
                    "En la parte inferior de la página aparecerá un recuadro despues de la palabra 'Answer'. Cada reto tiene"
                ),
                " una solución en particular, y es justamente y lo único que debes ingresar ahi.",
                " Para validarlo, debes hacer click en '[Submit]'. ¡No debes pegar tu código ahi!",
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/user-info/answer_input.png",
            ),
            class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
        ),
        class_name="container mx-auto px-4 py-5",
    )


def user_info() -> Component:
    return el.div(step_one(), step_two(), step_three())
