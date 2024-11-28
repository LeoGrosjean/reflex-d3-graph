"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex.style import Style, format_as_emotion
from rxconfig import config

from custom_components.reflex_d3_graph.graph import d3_graph
from examples.marvel import MARVEL_DATA, MARVEL_CONFIG

MARVEL_CONFIG = format_as_emotion(Style(MARVEL_CONFIG))

class State(rx.State):
    """The app state."""

    @rx.event(background=True)
    async def test_log(self, source, target):
        return rx.toast((source, "->", target))

    @rx.event(background=True)
    async def test_on_click(self, node_id, node):
        return rx.toast(str((node_id, node)))


def logo_github(**props):
    return rx.center(
        rx.link(
            rx.hstack(
                "View source on ",
                rx.icon("github"),
                text_align="center",
                align="center",
                padding="1em",
            ),
            href="https://github.com/LeoGrosjean/reflex-d3-graph",
            is_external=True,
            size="3",
        ),
        width=props.pop("width", "100%"),
        **props,
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.fragment(
        rx.color_mode.button(position="top-right"),
        d3_graph(
            id="osef_id",
            data=MARVEL_DATA,
            config=MARVEL_CONFIG,
            on_click_node=State.test_on_click,
            on_click_link=State.test_log,
            width='100vw',
            height="100vh",
        ),
        logo_github(
            position="fixed",
            z_index=20,
            bottom="2rem",
        ),
    )

app = rx.App()
app.add_page(index)
