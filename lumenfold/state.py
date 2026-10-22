"""Interactive state for the Lumenfold preview."""

from __future__ import annotations

import re

import reflex as rx

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")
ROLES = ("Director", "Designer", "Producer", "Editor", "Writer", "Studio lead")
TEAMS = ("2-5", "6-15", "16-40", "41 or more")
PLANS = ("bench", "studio", "house")
FILTERS = ("all", "rooms", "critique", "studio")


def waitlist_errors(
    name: str, email: str, studio: str, role: str, team: str
) -> dict[str, str]:
    """Return a message for each waitlist field that is not ready to keep."""
    errors = {
        "name": "",
        "email": "",
        "studio": "",
        "role": "",
        "team": "",
    }
    if len(name) < 2 or not any(character.isalpha() for character in name):
        errors["name"] = "Enter the name we should use when we write back."
    if EMAIL_RE.fullmatch(email) is None:
        errors["email"] = "Enter a work email like ada@northline.studio."
    if len(studio) < 2:
        errors["studio"] = "Enter the studio or company name."
    if role not in ROLES:
        errors["role"] = "Choose the role you play on the work."
    if team not in TEAMS:
        errors["team"] = "Choose a team size."
    return errors


class State(rx.State):
    """Seats, plans, the changelog filter, and the waitlist form."""

    seats: int = 8
    plan: str = "studio"
    annual: bool = True
    menu_open: bool = False
    log_filter: str = "all"

    submitted: bool = False
    waitlist_name: str = ""
    waitlist_email: str = ""
    waitlist_studio: str = ""
    waitlist_role: str = ""
    waitlist_team: str = ""
    name_error: str = ""
    email_error: str = ""
    studio_error: str = ""
    role_error: str = ""
    team_error: str = ""

    @rx.event
    def set_plan(self, plan: str):
        if plan in PLANS:
            self.plan = plan

    @rx.event
    def set_seats(self, value: list[int | float]):
        raw = value[0] if isinstance(value, (list, tuple)) and value else value
        try:
            seats = int(float(raw))
        except (TypeError, ValueError):
            return
        if seats < 1:
            seats = 1
        if seats > 40:
            seats = 40
        self.seats = seats

    @rx.event
    def set_annual(self, value: bool):
        self.annual = bool(value)

    @rx.event
    def toggle_menu(self):
        self.menu_open = not self.menu_open

    @rx.event
    def close_menu(self):
        self.menu_open = False

    @rx.event
    def set_log_filter(self, value: str):
        if value in FILTERS:
            self.log_filter = value

    @rx.event
    def submit_waitlist(self, form_data: dict):
        name = str(form_data.get("name", "")).strip()
        email = str(form_data.get("email", "")).strip()
        studio = str(form_data.get("studio", "")).strip()
        role = str(form_data.get("role", "")).strip()
        team = str(form_data.get("team_size", "")).strip()
        errors = waitlist_errors(name, email, studio, role, team)

        self.waitlist_name = name
        self.waitlist_email = email
        self.waitlist_studio = studio
        self.waitlist_role = role
        self.waitlist_team = team
        self.name_error = errors["name"]
        self.email_error = errors["email"]
        self.studio_error = errors["studio"]
        self.role_error = errors["role"]
        self.team_error = errors["team"]
        self.submitted = not any(errors.values())

    @rx.event
    def reset_waitlist(self):
        self.submitted = False
        self.name_error = ""
        self.email_error = ""
        self.studio_error = ""
        self.role_error = ""
        self.team_error = ""

    @rx.var
    def plan_label(self) -> str:
        if self.plan == "bench":
            return "Bench"
        if self.plan == "house":
            return "House"
        return "Studio"

    @rx.var
    def list_rate(self) -> int:
        if self.plan == "bench":
            return 18
        if self.plan == "house":
            return 62
        return 36

    @rx.var
    def seat_rate(self) -> int:
        if self.annual:
            return (self.list_rate * 10) // 12
        return self.list_rate

    @rx.var
    def monthly_total(self) -> int:
        return self.seat_rate * self.seats

    @rx.var
    def yearly_total(self) -> int:
        return self.monthly_total * 12

    @rx.var
    def yearly_savings(self) -> int:
        return (self.list_rate - self.seat_rate) * self.seats * 12

    @rx.var
    def billing_label(self) -> str:
        if self.annual:
            return "Billed annually"
        return "Billed monthly"

    @rx.var
    def has_errors(self) -> bool:
        if self.name_error != "":
            return True
        if self.email_error != "":
            return True
        if self.studio_error != "":
            return True
        if self.role_error != "":
            return True
        if self.team_error != "":
            return True
        return False
