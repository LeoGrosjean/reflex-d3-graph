"""Reflex custom component react-d3-graph."""
from typing import Dict, Any
from .types import DataType
from uuid import uuid4
import reflex as rx


def _on_click_graph(event) -> list[rx.Var]:
    return [event]

def _on_click_node(node_id: str, node: Dict[str, Any]) -> list[rx.Var]:
    return [node_id, node]

def _on_double_click_node(node_id, node) -> list[rx.Var]:
    return [node_id, node]

def _on_right_click_node(event, node_id, node) -> list[rx.Var]:
    return [event, node_id, node]

def _on_mouse_over_node(node_id, node) -> list[rx.Var]:
    return [node_id, node]

def _on_mouse_out_node(node_id, node) -> list[rx.Var]:
    return [node_id, node]

def _on_click_link(source, target) -> list[rx.Var]:
    return [source, target]

def _on_right_click_link(event, source, target) -> list[rx.Var]:
    return [event, source, target]

def _on_mouse_over_link(source, target) -> list[rx.Var]:
    return [source, target]

def _on_mouse_out_link(source, target) -> list[rx.Var]:
    return [source, target]

def _on_node_position_change(node_id, x, y) -> list[rx.Var]:
    return [node_id, x, y]

def _on_zoom_change(previous_zoom, new_zoom) -> list[rx.Var]:
    return [previous_zoom, new_zoom]


class D3Graph(rx.Component):
    """Calendar component."""

    # The React library to wrap.
    library: str = "react-d3-graph18"

    # lib_dependencies: list[str] = []

    # The React component tag.
    tag = "Graph"

    # If you are wrapping another components with the same tag as a component in your project
    # you can use aliases to differentiate between them and avoid naming conflicts.
    alias = "ReflexGraph"

    # The props of the React component.
    # id is mandatory, if no id is defined rd3g will throw an error
    data: rx.Var[DataType]
    config: rx.Var[Dict[str, Any]] # rx.Var[GraphSettingsModel]#
    on_click_graph: rx.EventHandler[_on_click_graph]
    on_click_node: rx.EventHandler[_on_click_node]
    on_double_click_node: rx.EventHandler[_on_double_click_node]
    on_right_click_node: rx.EventHandler[_on_right_click_node]
    on_click_link: rx.EventHandler[_on_click_link]
    on_right_click_link: rx.EventHandler[_on_right_click_link]
    on_mouse_over_node: rx.EventHandler[_on_mouse_over_node]
    on_mouse_out_node: rx.EventHandler[_on_mouse_out_node]
    on_mouse_over_link: rx.EventHandler[_on_mouse_over_link]
    on_mouse_out_link: rx.EventHandler[_on_mouse_out_link]
    on_node_position_change: rx.EventHandler[_on_node_position_change]
    on_zoom_change: rx.EventHandler[_on_zoom_change]

    def add_hooks(self):
        if self.id == None:
            self.id = "uuid" + str(uuid4()).replace('-', '')

        return [f"""
  useEffect(() => {{
    if (!ref_{self.id}.current) return;
    const element = document.querySelector(`[name="svg-container-{self.id}"]`);
    if (element) {{
      {'element.style.width = ' + str(self.style.get('width'))  + ';' if self.style.get('width') is not None else '//'}
      {'element.style.height = ' + str(self.style.get('height')) + ';' if self.style.get('height') is not None else '//'}
    }}
    const div_element = document.querySelector(`[id="{self.id}-graph-wrapper"]`);
     if (div_element) {{
      div_element.classList.add("rt-Container")
    }}
  }}, [ref_{self.id}]);
        """]

    @classmethod
    def create(
        cls,
        *children,
        **props,
    ):
        return rx.fragment(super().create(
            *children,
            **props,
            padding="0px"
        ))

d3_graph = D3Graph.create
