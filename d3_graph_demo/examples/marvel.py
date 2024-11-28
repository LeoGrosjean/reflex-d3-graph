MARVEL_CONFIG = {
    "directed": True,
    "automatic_rearrange_after_drop_node": True,
    "collapsible": False,
    "height": "500",
    "highlight_degree": 2,
    "highlight_opacity": 0.2,
    "link_highlight_behavior": True,
    "max_zoom": 12,
    "min_zoom": 0.05,
    "node_highlight_behavior": True,
    "pan_and_zoom": False,
    "static_graph": False,
    "width": "800",
    "d3": {
        "alpha_target": 0.05,
        "gravity": -250,
        "link_length": 120,
        "link_strength": 2
    },
    "node": {
        "color": "#d3d3d3",
        "font_color": "green",
        "font_size": 10,
        "font_weight": "normal",
        "highlight_color": "red",
        "highlight_font_size": 14,
        "highlight_font_weight": "bold",
        "highlight_stroke_color": "red",
        "highlight_stroke_width": 1.5,
        "label_property": "n => (n.name ? `${n.id} - ${n.name}` : n.id)",
        "mouse_cursor": "crosshair",
        "opacity": 0.9,
        "render_label": True,
        "size": 200,
        "stroke_color": "none",
        "stroke_width": 1.5,
        "svg": "",
        "symbol_type": "circle",
        "view_generator": None
    },
    "link": {
        "color": "lightgray",
        "highlight_color": "red",
        "mouse_cursor": "pointer",
        "opacity": 1,
        "semantic_stroke_width": True,
        "stroke_width": 3,
        "type": "STRAIGHT"
    }
}

MARVEL_DATA = {
    "links": [
        {
            "source": "Marvel",
            "target": "Heroes"
        },
        {
            "source": "Marvel",
            "target": "Villains"
        },
        {
            "source": "Marvel",
            "target": "Teams"
        },
        {
            "source": "Heroes",
            "target": "Spider-Man"
        },
        {
            "source": "Heroes",
            "target": "CAPTAIN MARVEL"
        },
        {
            "source": "Heroes",
            "target": "HULK"
        },
        {
            "source": "Heroes",
            "target": "Black Widow"
        },
        {
            "source": "Heroes",
            "target": "Daredevil"
        },
        {
            "source": "Heroes",
            "target": "Wolverine"
        },
        {
            "source": "Heroes",
            "target": "Captain America"
        },
        {
            "source": "Heroes",
            "target": "Iron Man"
        },
        {
            "source": "Heroes",
            "target": "THOR"
        },
        {
            "source": "Villains",
            "target": "Dr. Doom"
        },
        {
            "source": "Villains",
            "target": "Mystique"
        },
        {
            "source": "Villains",
            "target": "Red Skull"
        },
        {
            "source": "Villains",
            "target": "Ronan"
        },
        {
            "source": "Villains",
            "target": "Magneto"
        },
        {
            "source": "Villains",
            "target": "Thanos"
        },
        {
            "source": "Villains",
            "target": "Black Cat"
        },
        {
            "source": "Teams",
            "target": "Avengers"
        },
        {
            "source": "Teams",
            "target": "Guardians of the Galaxy"
        },
        {
            "source": "Teams",
            "target": "Defenders"
        },
        {
            "source": "Teams",
            "target": "X-Men"
        },
        {
            "source": "Teams",
            "target": "Fantastic Four"
        },
        {
            "source": "Teams",
            "target": "Inhumans"
        }
    ],
    "nodes": [
        {
            "id": "Marvel",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/marvel.png",
            "size": 500,
            "fontSize": 18,
        },
        {
            "id": "Heroes",
            "symbolType": "circle",
            "color": "red",
            "size": 300
        },
        {
            "id": "Villains",
            "symbolType": "circle",
            "color": "red",
            "size": 300
        },
        {
            "id": "Teams",
            "symbolType": "circle",
            "color": "red",
            "size": 300
        },
        {
            "id": "Spider-Man",
            "name": "Peter Benjamin Parker",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png",
            "size": 400
        },
        {
            "id": "CAPTAIN MARVEL",
            "name": "Carol Danvers",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png",
            "size": 400
        },
        {
            "id": "HULK",
            "name": "Robert Bruce Banner",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_hulk.png",
            "size": 400
        },
        {
            "id": "Black Widow",
            "name": "Natasha Alianovna Romanova",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_blackwidow.png",
            "size": 400
        },
        {
            "id": "Daredevil",
            "name": "Matthew Michael Murdock",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_daredevil.png",
            "size": 400
        },
        {
            "id": "Wolverine",
            "name": "James Howlett",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_wolverine.png",
            "size": 400
        },
        {
            "id": "Captain America",
            "name": "Steven Rogers",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainamerica.png",
            "size": 400
        },
        {
            "id": "Iron Man",
            "name": "Tony Stark",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_ironman.png",
            "size": 400
        },
        {
            "id": "THOR",
            "name": "Thor Odinson",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_thor.png",
            "size": 400
        },
        {
            "id": "Dr. Doom",
            "name": "Victor von Doom",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/drdoom.png",
            "size": 400
        },
        {
            "id": "Mystique",
            "name": "Unrevealed",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/mystique.png",
            "size": 400
        },
        {
            "id": "Red Skull",
            "name": "Johann Shmidt",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/redskull.png",
            "size": 400
        },
        {
            "id": "Ronan",
            "name": "Ronan",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/ronan.png",
            "size": 400
        },
        {
            "id": "Magneto",
            "name": "Max Eisenhardt",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/magneto.png",
            "size": 400
        },
        {
            "id": "Thanos",
            "name": "Thanos",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/thanos.png",
            "size": 400
        },
        {
            "id": "Black Cat",
            "name": "Felicia Hardy",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/blackcat.png",
            "size": 400
        },
        {
            "id": "Avengers",
            "name": "",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/avengers.png",
            "size": 400
        },
        {
            "id": "Guardians of the Galaxy",
            "name": "",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/gofgalaxy.png",
            "size": 400
        },
        {
            "id": "Defenders",
            "name": "",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/defenders.png",
            "size": 400
        },
        {
            "id": "X-Men",
            "name": "",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/xmen.png",
            "size": 400
        },
        {
            "id": "Fantastic Four",
            "name": "",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/fantasticfour.png",
            "size": 400
        },
        {
            "id": "Inhumans",
            "name": "",
            "svg": "http://marvel-force-chart.surge.sh/marvel_force_chart_img/inhumans.png",
            "size": 400
        }
    ]
}

