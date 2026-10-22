import reflex as rx
from reflex.plugins import RadixThemesPlugin, SitemapPlugin

config = rx.Config(
    app_name="lumenfold",
    show_built_with_reflex=False,
    default_color_mode="dark",
    telemetry_enabled=False,
    disable_plugins=[SitemapPlugin],
    plugins=[
        RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="cyan",
                gray_color="slate",
                radius="small",
                scaling="100%",
            )
        )
    ],
)
