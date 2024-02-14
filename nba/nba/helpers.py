import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.image(src="/nba.png", width="50px"),
                rx.heading("NBA Data", size="8"),
                rx.flex(
                    rx.badge("2015-2016 Season"),
                ),
            ),
            rx.dropdown_menu.root(
                rx.dropdown_menu.trigger(
                    rx.button("Menu", color="white", size="3", radius="medium", px=4, py=2),
                ),
                rx.dropdown_menu.content(
                    rx.link(rx.dropdown_menu.item("Graph"), href="/"),
                    rx.dropdown_menu.separator(),
                    rx.link(
                        rx.dropdown_menu.item(
                            rx.hstack(rx.text("20Dataset"), rx.icon(tag="download"))
                        ),
                        href="https://media.geeksforgeeks.org/wp-content/uploads/nba.csv",
                    ),
                ),
            ),
            justify="space-between",
            border_bottom="0.2em solid #F0F0F0",
            padding_inline_start="2em",
            padding_inline_end="2em",
            padding_top="1em",
            padding_bottom="1em",
            bg="rgba(255,255,255, 0.97)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )