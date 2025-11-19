import reflex as rx

config = rx.Config(
    app_name="app",
    plugins=[rx.plugins.TailwindV4Plugin(), rx.plugins.sitemap.SitemapPlugin()],
    #backend_host="0.0.0.0",
    #backend_port=None,
    show_built_with_reflex=False
)
