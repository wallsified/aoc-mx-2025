import reflex as rx

config = rx.Config(
    app_name="app",
    plugins=[rx.plugins.TailwindV3Plugin()],
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    enable_state=False,
    backend_exception_handler=None
)
