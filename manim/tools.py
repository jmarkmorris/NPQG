
# A helpful way to draw a grid when composing the animation
INDIGO = "#4B0082"
    grid = NumberPlane(
        x_range=[-7, 7],
        y_range=[-4, 4],
        axis_config={
            "stroke_color": WHITE,
            "stroke_width": 1,
            "include_ticks": False,
            "include_tip": False,
        },
        background_line_style={
            "stroke_color": INDIGO,
            "stroke_width": 1,
        }
    )
    self.add(grid)