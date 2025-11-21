import reflex as rx


class Snow(rx.Component):
    """
    Intento de wrapping de react-snowfall.
    """

    library = "react-snowfall"
    lib_dependencies: list[str] = ["react-fast-compare"]
    tag = "Snowfall"
    is_default = (True,)
    snowflakeCount = ({250},)
    style = {
        "position": "fixed",
        "width": "100vw",
        "height": "100vh",
    }


# Convenience function to create the Spline component.
snow = Snow.create
