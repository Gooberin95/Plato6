"""Public log of the Lumenfold preview."""

import reflex as rx

from lumenfold.layout import page_shell
from lumenfold.state import State

ENTRIES = (
    {
        "version": "0.9.0",
        "date": "14 Oct 2026",
        "tag": "rooms",
        "title": "Folded rooms",
        "summary": "A room can hold a cut, a board, and a script without splitting the thread. The conversation stays on the show, whichever file you open.",
    },
    {
        "version": "0.8.2",
        "date": "2 Sep 2026",
        "tag": "studio",
        "title": "Guest passes",
        "summary": "Clients mark a frame and leave. A pass opens one cut. It does not open the archive, the other shows, or the decision log.",
    },
    {
        "version": "0.8.0",
        "date": "18 Aug 2026",
        "tag": "critique",
        "title": "Decision stamps",
        "summary": "Approve, hold, or redo, pinned to the exact version. The stamp records who made the call, so the next review starts from a fact.",
    },
    {
        "version": "0.7.1",
        "date": "30 Jun 2026",
        "tag": "rooms",
        "title": "Notes that follow the cut",
        "summary": "Open notes from cut 4 arrive on cut 5, on the nearest frame. Stamped notes stay behind on the version where they were settled.",
    },
    {
        "version": "0.6.0",
        "date": "9 May 2026",
        "tag": "critique",
        "title": "Pins for picture and script",
        "summary": "A picture note lands on a frame or a timestamp. A script note lands on a line. Both use the same stamp when the decision is made.",
    },
    {
        "version": "0.4.0",
        "date": "11 Mar 2026",
        "tag": "studio",
        "title": "Presence",
        "summary": "See who is in the room and which frame they have open. The point is to stop two people giving the same note at once.",
    },
)


def filter_button(value: str, label: str) -> rx.Component:
    return rx.el.button(
        label,
        type="button",
        class_name=rx.cond(State.log_filter == value, "filter-btn is-on", "filter-btn"),
        on_click=State.set_log_filter(value),
    )


def log_entry(item: dict[str, str]) -> rx.Component:
    return rx.cond(
        (State.log_filter == "all") | (State.log_filter == item["tag"]),
        rx.box(
            rx.box(
                rx.text(item["version"], class_name="log-version"),
                rx.text(item["date"], class_name="log-date"),
                class_name="log-meta",
            ),
            rx.box(
                rx.text(item["tag"], class_name="log-tag"),
                rx.heading(item["title"], as_="h3", class_name="log-title"),
                rx.text(item["summary"], class_name="log-summary"),
                class_name="log-body",
            ),
            class_name="log-entry",
        ),
    )


def changelog() -> rx.Component:
    return page_shell(
        rx.box(
            rx.text("Preview log", class_name="eyebrow"),
            rx.heading("What changed in the room.", as_="h1", class_name="display"),
            rx.text(
                "Six notes from the preview, newest first. Filter them by rooms, critique, or the studio around the work.",
                class_name="lede",
            ),
            rx.box(
                filter_button("all", "All"),
                filter_button("rooms", "Rooms"),
                filter_button("critique", "Critique"),
                filter_button("studio", "Studio"),
                class_name="filter-row",
                role="group",
                aria_label="Filter the log",
            ),
            rx.match(
                State.log_filter,
                ("rooms", rx.text("How a room holds the work.", class_name="lede log-blurb")),
                ("critique", rx.text("Notes, pins, and stamps.", class_name="lede log-blurb")),
                ("studio", rx.text("People, passes, and presence.", class_name="lede log-blurb")),
                rx.text("Everything in the preview, newest first.", class_name="lede log-blurb"),
            ),
            class_name="panel hero",
        ),
        rx.box(
            *[log_entry(item) for item in ENTRIES],
            class_name="panel log-list",
        ),
        active="changelog",
    )
