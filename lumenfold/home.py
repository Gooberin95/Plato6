"""Landing page for the Lumenfold studio."""

import reflex as rx

from lumenfold.layout import page_shell
from lumenfold.state import ROLES, TEAMS, State

FEATURES = (
    (
        "01",
        "layers",
        "Shared rooms",
        "A show gets one room. Picture, boards, and the script stay there instead of scattering across tools.",
    ),
    (
        "02",
        "square-dashed-mouse-pointer",
        "Frame notes",
        "Pin a comment to a frame, a line, or a timestamp. The note sits on the work, not in a channel beside it.",
    ),
    (
        "03",
        "git-branch",
        "Version threads",
        "The next cut inherits open notes. Resolved notes stay on the version where they were settled.",
    ),
    (
        "04",
        "users",
        "Presence",
        "See who is in the room and which frame they have open before you talk over them.",
    ),
    (
        "05",
        "stamp",
        "Decision stamps",
        "Approve, hold, or redo. The stamp sticks to that version, with the name of the person who made the call.",
    ),
    (
        "06",
        "ticket",
        "Guest passes",
        "Send a client a pass to one cut. They can mark frames. They cannot wander into the rest of the studio.",
    ),
)

FAQS = (
    (
        "room",
        "What is a room?",
        "A room is one show, campaign, or product. Everything you drop in — a cut, a board, a script — stays in that room, and so does the conversation about it.",
    ),
    (
        "guests",
        "Do clients need a seat?",
        "No. A guest pass opens one cut. Clients can pin notes on frames. They cannot open other rooms or read the decision log for older versions.",
    ),
    (
        "files",
        "Which files can we drop in?",
        "Picture cuts, still boards, and scripts. A version is created when the file lands. Lumenfold is not a general drive — if it is not part of the review, it does not belong in the room.",
    ),
    (
        "versions",
        "What happens to notes on a new cut?",
        "Open notes follow the new version and land on the nearest frame. Notes you already stamped stay behind on the version where the decision was made.",
    ),
    (
        "storage",
        "Where is the work stored?",
        "In this preview, only on the machine you are using. The product story is a private region per studio. House accounts can pin that region. This demo does not upload anything.",
    ),
    (
        "pay",
        "Can I pay for a seat today?",
        "No. Lumenfold is a fictional studio tool. The calculator shows the rates we would charge, and the waitlist only remembers your note for this browser session.",
    ),
)


def section_head(eyebrow: str, title: str, lede: str, center: bool = False) -> rx.Component:
    classes = "section-head center" if center else "section-head"
    return rx.box(
        rx.text(eyebrow, class_name="eyebrow"),
        rx.heading(title, as_="h2", class_name="section-title"),
        rx.text(lede, class_name="lede"),
        class_name=classes,
    )


def hero() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text("Creative collaboration for studios", class_name="eyebrow"),
            rx.heading(
                "The whole studio, folded into one room.",
                as_="h1",
                class_name="display",
            ),
            rx.text(
                "Lumenfold is the creative-collaboration app for people who make pictures together. Briefs, cuts, and critique stay on the work, so the decision is still there when the next version arrives.",
                class_name="lede",
            ),
            rx.box(
                rx.link(
                    "Request a founding seat",
                    href="/#waitlist",
                    class_name="btn btn-primary",
                ),
                rx.link(
                    "See what changed",
                    href="/changelog",
                    class_name="btn btn-ghost",
                ),
                class_name="cta-row",
            ),
            rx.box(
                principle(
                    "01",
                    "One room per show",
                    "The cut, the board, and the script share a single thread.",
                ),
                principle(
                    "02",
                    "Notes on the frame",
                    "A comment points at a moment, not at a message from Tuesday.",
                ),
                principle(
                    "03",
                    "A stamp, then the next cut",
                    "Approve, hold, or redo. The following version opens with that attached.",
                ),
                class_name="principles",
            ),
            rx.text(
                "Preview cohort · Northline Pictures, Harbor & Field, Glass District, Kite Office",
                class_name="cohort",
            ),
            class_name="panel hero",
        ),
        class_name="hero-wrap",
        id="top",
    )


def principle(index: str, title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(index, class_name="principle-index"),
        rx.heading(title, as_="h3"),
        rx.text(body),
        class_name="principle",
    )


def steps() -> rx.Component:
    return rx.box(
        section_head(
            "01 — How a room works",
            "From the drop to the stamp.",
            "Three moves. No side channel for the decision to fall into.",
            center=True,
        ),
        rx.box(
            step(
                "01",
                "Drop the work",
                "Bring in a cut, a board, or a script. The room makes a version the moment it lands.",
            ),
            step(
                "02",
                "Mark the frame",
                "Anyone with access pins a note to the exact moment that needs a decision.",
            ),
            step(
                "03",
                "Stamp it",
                "The lead stamps approve, hold, or redo. The next version opens with that thread attached.",
            ),
            class_name="steps",
        ),
        class_name="panel",
        id="how",
    )


def step(index: str, title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(index, class_name="step-index"),
        rx.heading(title, as_="h3"),
        rx.text(body),
        class_name="step",
    )


def feature_card(index: str, icon: str, title: str, body: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.icon(icon, size=18, color="#8eebf4", aria_hidden=True),
                class_name="icon-frame",
            ),
            rx.text(index, class_name="feature-index"),
            class_name="feature-top",
        ),
        rx.heading(title, as_="h3"),
        rx.text(body),
        class_name="feature-card",
    )


def features() -> rx.Component:
    return rx.box(
        section_head(
            "02 — Inside the room",
            "The tools a review actually uses.",
            "Built for directors, designers, editors, and producers who are already in the cut — not for another inbox.",
            center=True,
        ),
        rx.box(
            *[feature_card(*feature) for feature in FEATURES],
            class_name="feature-grid",
        ),
        class_name="panel",
        id="features",
    )


def plan_choice(plan_id: str, name: str, price: str, note: str) -> rx.Component:
    return rx.el.button(
        rx.el.span(name, class_name="plan-name"),
        rx.el.span(price, class_name="plan-price"),
        rx.el.span(note, class_name="plan-note"),
        type="button",
        class_name=rx.cond(State.plan == plan_id, "plan-btn is-on", "plan-btn"),
        on_click=State.set_plan(plan_id),
    )


def include_list(lines: list[str]) -> rx.Component:
    return rx.el.ul(
        *[rx.el.li(line) for line in lines],
        class_name="includes",
    )


def pricing() -> rx.Component:
    return rx.box(
        section_head(
            "03 — Seats and plans",
            "Price the room before you ask for it.",
            "Move the seats, pick a plan, and switch billing. The quote updates with the room.",
            center=True,
        ),
        rx.box(
            rx.box(
                rx.text("Plan", class_name="control-label"),
                rx.box(
                    plan_choice("bench", "Bench", "$18", "Small team"),
                    plan_choice("studio", "Studio", "$36", "Usual pick"),
                    plan_choice("house", "House", "$62", "Several shows"),
                    class_name="plan-row",
                    role="group",
                    aria_label="Plan",
                ),
                rx.box(
                    rx.switch(
                        checked=State.annual,
                        on_change=State.set_annual,
                        color_scheme="cyan",
                        size="2",
                        high_contrast=True,
                    ),
                    rx.text(State.billing_label, class_name="switch-label"),
                    class_name="switch-row",
                ),
                rx.box(
                    rx.box(
                        rx.text("Seats", class_name="control-label"),
                        rx.text(State.seats, class_name="seat-count"),
                        class_name="seat-head",
                    ),
                    rx.slider(
                        min=1,
                        max=40,
                        step=1,
                        default_value=8,
                        on_change=State.set_seats.throttle(80),
                        color_scheme="cyan",
                        size="2",
                        high_contrast=True,
                        aria_label="Number of seats",
                        width="100%",
                    ),
                    rx.text(
                        "1 to 40 people with a login. Guest passes are not seats.",
                        class_name="hint",
                    ),
                    class_name="seat-block",
                ),
            ),
            rx.box(
                rx.text("Your quote", class_name="quote-kicker"),
                rx.el.p(
                    rx.el.span("$", class_name="currency"),
                    rx.el.span(State.monthly_total, class_name="quote-figure"),
                    rx.el.span("/ month", class_name="per"),
                    class_name="quote-hero",
                ),
                rx.cond(
                    State.seats == 1,
                    rx.text(
                        "$",
                        State.seat_rate,
                        " per seat · ",
                        State.plan_label,
                        " · 1 seat",
                        class_name="quote-caption",
                    ),
                    rx.text(
                        "$",
                        State.seat_rate,
                        " per seat · ",
                        State.plan_label,
                        " · ",
                        State.seats,
                        " seats",
                        class_name="quote-caption",
                    ),
                ),
                rx.cond(
                    State.annual,
                    rx.text(
                        "Save $",
                        State.yearly_savings,
                        " a year versus paying monthly.",
                        class_name="savings-line",
                    ),
                    rx.text(
                        "Annual billing uses a 10-month rate.",
                        class_name="savings-line",
                    ),
                ),
                rx.box(
                    quote_row("Plan", State.plan_label),
                    quote_row("Billing", State.billing_label),
                    quote_row("Per year", rx.text("$", State.yearly_total)),
                    class_name="quote-rows",
                ),
                rx.match(
                    State.plan,
                    (
                        "bench",
                        include_list(
                            [
                                "3 active rooms",
                                "Frame and line notes",
                                "30-day version history",
                                "Replies within two weekdays",
                            ]
                        ),
                    ),
                    (
                        "house",
                        include_list(
                            [
                                "Everything in Studio",
                                "SSO and a private region",
                                "An audit log of every stamp",
                                "A producer on the account",
                            ]
                        ),
                    ),
                    include_list(
                        [
                            "Unlimited rooms",
                            "Live presence",
                            "Notes that follow the next cut",
                            "Guest passes for clients",
                        ]
                    ),
                ),
                rx.text(
                    "List prices are per seat, per month. Annual billing charges the 10-month rate. Nothing here is a real invoice.",
                    class_name="fine-print",
                ),
                class_name="quote",
            ),
            class_name="price-layout",
        ),
        class_name="panel",
        id="pricing",
    )


def quote_row(label: str, value: rx.Component | str) -> rx.Component:
    return rx.box(
        rx.text(label, class_name="q-label"),
        rx.box(value, class_name="q-value"),
        class_name="q-row",
    )


def faq() -> rx.Component:
    return rx.box(
        section_head(
            "04 — Questions",
            "Before you ask for a seat.",
            "Short answers. The last one matters: this is a preview of a fictional product.",
            center=True,
        ),
        rx.accordion.root(
            *[
                rx.accordion.item(
                    header=question,
                    content=rx.text(answer, class_name="faq-a"),
                    value=value,
                )
                for value, question, answer in FAQS
            ],
            type="single",
            collapsible=True,
            variant="ghost",
            color_scheme="cyan",
            show_dividers=True,
            default_value="room",
            class_name="lf-faq",
            width="100%",
        ),
        class_name="panel",
        id="faq",
    )


def field(
    label: str,
    control_id: str,
    control: rx.Component,
    error: rx.Var,
    span: bool = False,
) -> rx.Component:
    classes = "field span-2" if span else "field"
    return rx.box(
        rx.el.label(label, html_for=control_id, class_name="field-label"),
        control,
        rx.cond(error != "", rx.text(error, class_name="field-error", role="alert")),
        class_name=classes,
    )


def text_input(control_id: str, name: str, placeholder: str, autocomplete: str) -> rx.Component:
    return rx.el.input(
        id=control_id,
        name=name,
        placeholder=placeholder,
        auto_complete=autocomplete,
        max_length=120,
        class_name="lf-input",
    )


def select_input(control_id: str, name: str, placeholder: str, options: tuple[str, ...]) -> rx.Component:
    return rx.el.select(
        rx.el.option(placeholder, value=""),
        *[rx.el.option(option, value=option) for option in options],
        id=control_id,
        name=name,
        default_value="",
        class_name="lf-select",
    )


def waitlist_form() -> rx.Component:
    return rx.form(
        rx.cond(
            State.has_errors,
            rx.text(
                "Fix the highlighted fields and request the seat again.",
                class_name="form-banner",
                role="alert",
            ),
        ),
        rx.box(
            field(
                "Name",
                "waitlist-name",
                text_input("waitlist-name", "name", "Ada North", "name"),
                State.name_error,
            ),
            field(
                "Work email",
                "waitlist-email",
                rx.el.input(
                    id="waitlist-email",
                    name="email",
                    type="email",
                    placeholder="ada@northline.studio",
                    auto_complete="email",
                    max_length=120,
                    class_name="lf-input",
                ),
                State.email_error,
            ),
            field(
                "Studio",
                "waitlist-studio",
                text_input("waitlist-studio", "studio", "Northline Pictures", "organization"),
                State.studio_error,
                span=True,
            ),
            field(
                "Role",
                "waitlist-role",
                select_input("waitlist-role", "role", "Choose a role", ROLES),
                State.role_error,
            ),
            field(
                "Team size",
                "waitlist-team",
                select_input("waitlist-team", "team_size", "Choose a size", TEAMS),
                State.team_error,
            ),
            rx.box(
                rx.el.button(
                    "Request a founding seat",
                    type="submit",
                    class_name="btn btn-primary",
                ),
                class_name="span-2 submit-row",
            ),
            class_name="form-grid",
        ),
        on_submit=State.submit_waitlist,
        no_validate=True,
        width="100%",
        class_name="waitlist-form",
    )


def waitlist() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.text("05 — Founding seats", class_name="eyebrow"),
                rx.heading(
                    "Ask for a seat in the preview.",
                    as_="h2",
                    class_name="section-title",
                ),
                rx.text(
                    "Tell us who you are and how big the room needs to be. We check the fields before keeping the note. It never leaves this session.",
                    class_name="lede",
                ),
                class_name="section-head",
            ),
            rx.cond(
                State.submitted,
                rx.box(
                    rx.text("Seat requested", class_name="eyebrow"),
                    rx.heading(
                        "You're on the list, ",
                        State.waitlist_name,
                        ".",
                        as_="h3",
                        class_name="success-title",
                    ),
                    rx.text(
                        "We'll hold a founding seat for ",
                        State.waitlist_studio,
                        " and write ",
                        State.waitlist_email,
                        ". Role: ",
                        State.waitlist_role,
                        ". Team: ",
                        State.waitlist_team,
                        ". This demo keeps that note in the session only.",
                        class_name="lede",
                    ),
                    rx.el.button(
                        "Add someone else",
                        type="button",
                        class_name="btn btn-ghost",
                        on_click=State.reset_waitlist,
                        margin_top="1rem",
                    ),
                    class_name="success-card",
                ),
                waitlist_form(),
            ),
            class_name="waitlist-layout",
        ),
        class_name="panel",
        id="waitlist",
    )


def index() -> rx.Component:
    return page_shell(
        hero(),
        steps(),
        features(),
        pricing(),
        faq(),
        waitlist(),
        active="home",
    )
