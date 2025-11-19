import reflex as rx

config = rx.Config(
    app_name="app",
    plugins=[rx.plugins.TailwindV3Plugin()],
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    frontend_port=3000,
    backend_port=None,
    telemetry_enabled=False,
    is_reflex_cloud=False
)