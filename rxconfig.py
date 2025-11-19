import reflex as rx

config = rx.Config(
    app_name="app",
    plugins=[rx.plugins.TailwindV4Plugin(), rx.plugins.sitemap.SitemapPlugin()],
    # disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    backend_host="0.0.0.0",
    backend_port=8000,
)
