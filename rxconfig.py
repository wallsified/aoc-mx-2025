import reflex as rx

config = rx.Config(
    app_name="app",
    plugins=[rx.plugins.TailwindV3Plugin(), rx.plugins.sitemap.SitemapPlugin()],
    #disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    telemetry_enabled=False,
    is_reflex_cloud=False
)