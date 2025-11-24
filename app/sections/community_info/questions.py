from reflex import el, Component, icon, image
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
                    "Quien sea el reponsable de la comunidad debe acceder al Advent of Code original con algún método de los"
                ),
                " disponibles. Recomendamos GitHub y/o Google, pero debe de estar ligado a su comunidad de alguna manera u otra. ",
                "Esto es por que posteriormente la información de la comunidad será usada para crear el lobby. ",
                link(
                    text="Esto puedes hacerlo en este link.",
                    href="https://adventofcode.com/2025/auth/login",
                ),
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/lobbies/community_login.png",
            ),
            el.div(
                el.p(
                    "Posteriormente hay que ajustar la información del perfil. Idealmente, el perfil de la comunidad debe ",
                ),
                "de contener el nombre completo y la foto de la comunidad como en el ejemplo de abajo. El resto de campos dejalos en blanco. ",
                link(
                    text="Esto puedes hacerlo en este link.",
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
                    "¿Cómo creo un lobby para mi comunidad?", class_name="text-white"
                ),
                class_name="text-xl md:text-2xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            el.div(
                el.p(
                    "Una vez que tengas iniciada sesión la manera más facil de crearlo es dando click directamente "
                ),
                link(
                    text="aquí. ",
                    href="https://adventofcode.com/2025/leaderboard/private/create",
                ),
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            el.div(
                el.p(
                    "Lo que verás en la pantalla será algo como la imágen de abajo, donde en la pantalla se muestra tu ID de lobby. ",
                ),
                "Este es el ID que nos debes compartir para poder añadir el lobby al leaderboard principal de Posadas de Código.",
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/lobbies/created_leaderboard.png",
            ),
            class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
        ),
        class_name="container mx-auto px-4 py-5",
    )


def step_three() -> Component:
    return el.section(
        el.div(
            el.h2(
                el.span("¿Cómo se une la gente a mi lobby?", class_name="text-white"),
                class_name="text-xl md:text-2xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            el.div(
                el.p(
                    "El mismo ID que tienes del paso anterior es el ID que debes compartir entre tu comunidad para que"
                ),
                "la gente empiece a unirse. Lo que deberán hacer es ingresar ese ID en su perfil. Puedes enviarles",
                link(
                    text=" este link ",
                    href="https://adventofcode.com/2025/leaderboard/private",
                ),
                "para que solo deban añadirlo desde su cuenta. Esto se ve como en la imágen siguiente:",
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/lobbies/joining_leaderboard.png",
            ),
            class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
        ),
        class_name="container mx-auto px-4 py-5",
    )


def step_four() -> Component:
    return el.section(
        el.div(
            el.h2(
                el.span(
                    "¿Cómo se cuanta gente hay en el lobby?", class_name="text-white"
                ),
                class_name="text-xl md:text-2xl font-bold text-[#e7ecef] mb-6 text-center flex flex-col items-center",
            ),
            el.div(
                el.p("La primera parte de tu ID de lobby es lo que tienes que añadir "),
                link(
                    text=" a este link ",
                    href="https://adventofcode.com/2025/leaderboard/private",
                ),
                " en la url para que puedas revisar los usuarios en tu lobby. Esto se ve como en la imágen siguiente:",
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            faq_image(
                src="https://wallsified.github.io/aoc-mx-2025/assets/lobbies/members_in_leaderboard.png",
            ),
            el.div(
                el.p("La constante en todos los lobbys es que estará el usuario"),
                el.p("AWS Cloud Club UNAM", class_name="font-bold text-[#e7ecef]"),
                " Esto es por que es usuario que tenemos configurado para ser el usuario 'agregador' para todos los lobbys.",
                " Ten en cuenta que el usuario que aparece con el nombre de tu comunidad solo recursivo y lo ideal no es usarlo.",
                class_name="text-xl text-white-200 max-w-5xl mx-auto text-center leading-relaxed",
            ),
            class_name="bg-[#325832] bg-opacity-20 p-8 rounded-2xl border border-white-800",
        ),
        class_name="container mx-auto px-4 py-5",
    )


def community_faqs() -> Component:
    return el.div(step_one(), step_two(), step_three(), step_four())
