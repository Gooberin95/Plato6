"""Page shell, glass navigation, and footer."""

import reflex as rx

from lumenfold.state import State


def mark() -> rx.Component:
    """Geometric fold used as the wordmark."""
    return rx.el.span(
        rx.el.span(class_name="mk mk-a"),
        rx.el.span(class_name="mk mk-b"),
        rx.el.span(class_name="mk mk-c"),
        class_name="mark",
        aria_hidden="true",
    )


def nav_link(label: str, href: str, active: bool = False) -> rx.Component:
    classes = "nav-link is-active" if active else "nav-link"
    return rx.link(label, href=href, class_name=classes, on_click=State.close_menu)


def mobile_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        class_name="mobile-link",
        on_click=State.close_menu,
    )


def navbar(active: str) -> rx.Component:
    return rx.el.header(
        rx.box(
            rx.link(
                mark(),
                rx.el.span("Lumenfold", class_name="wordmark"),
                href="/",
                class_name="brand",
                on_click=State.close_menu,
            ),
            rx.el.nav(
                nav_link("Product", "/#features", active == "product"),
                nav_link("Pricing", "/#pricing"),
                nav_link("FAQ", "/#faq"),
                nav_link("Changelog", "/changelog", active == "changelog"),
                class_name="nav-links",
                aria_label="Primary",
            ),
            rx.box(
                rx.link(
                    "Request a seat",
                    href="/#waitlist",
                    class_name="btn btn-primary nav-cta",
                ),
                rx.el.button(
                    rx.cond(State.menu_open, "Close", "Menu"),
                    type="button",
                    class_name="menu-btn",
                    on_click=State.toggle_menu,
                    aria_expanded=State.menu_open,
                    aria_label="Open the menu",
                ),
                class_name="nav-actions",
            ),
            class_name="nav-bar",
        ),
        rx.cond(
            State.menu_open,
            rx.el.nav(
                mobile_link("Product", "/#features"),
                mobile_link("Pricing", "/#pricing"),
                mobile_link("FAQ", "/#faq"),
                mobile_link("Changelog", "/changelog"),
                rx.link(
                    "Request a seat",
                    href="/#waitlist",
                    class_name="btn btn-primary mobile-cta",
                    on_click=State.close_menu,
                ),
                class_name="mobile-panel",
                aria_label="Mobile",
            ),
        ),
        class_name="lf-nav",
        position="sticky",
        top="0",
        z_index="40",
        background="rgba(8, 14, 30, 0.46)",
        backdrop_filter="blur(18px) saturate(150%)",
        border_bottom="1px solid rgba(190, 220, 255, 0.18)",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.box(
            rx.box(
                mark(),
                rx.el.span("Lumenfold", class_name="wordmark"),
                class_name="brand",
            ),
            rx.text(
                "A fictional creative-collaboration studio. The waitlist stays in this browser session and nothing is billed.",
                class_name="footer-note",
            ),
            rx.box(
                rx.link("Product", href="/#features"),
                rx.link("Pricing", href="/#pricing"),
                rx.link("Changelog", href="/changelog"),
                class_name="footer-links",
            ),
            class_name="footer-inner",
        ),
        class_name="panel lf-footer",
    )


def page_shell(*children: rx.Component, active: str) -> rx.Component:
    """Root frame. The painting is applied once, here, and stays fixed while scrolling."""
    return rx.box(
        navbar(active),
        rx.el.main(*children, class_name="lf-main"),
        footer(),
        class_name="lf-root",
        background_image="url('/background.jpg')",
        background_size="cover",
        background_position="center",
        background_attachment="fixed",
        background_repeat="no-repeat",
        background_color="#070b16",
        min_height="100vh",
        color="#eef4fb",
        width="100%",
    )
