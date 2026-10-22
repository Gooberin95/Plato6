"""Lumenfold, a fictional creative-collaboration studio."""

import reflex as rx

from lumenfold.changelog import changelog
from lumenfold.home import index

app = rx.App(
    stylesheets=["/lumenfold.css"],
    html_lang="en",
)
app.add_page(
    index,
    title="Lumenfold — the studio, folded into one room",
    description="Lumenfold is a creative-collaboration app for studios. Shared rooms, frame notes, and a decision log.",
)
app.add_page(
    changelog,
    route="/changelog",
    title="Changelog — Lumenfold",
    description="What changed in the Lumenfold studio rooms.",
)
