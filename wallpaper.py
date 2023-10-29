import mpmath

from manim import *
from themes.dracula import dracula

# 4k resolution
config.pixel_height = 2160
config.pixel_width = 3840

dracula.set()
VMobject.set_default(fill_opacity=0)


def zeta(z):
    max_norm = config.frame_x_radius
    try:
        return complex(mpmath.zeta(z))
    except:
        return complex(max_norm, 0)


x_range = np.array([-90, 90])
y_range = x_range.copy()


class Inversion(Scene):
    def construct(self):
        bg = ComplexPlane()
        fg = ComplexPlane(
            x_range=x_range,
            y_range=y_range,
            axis_config={"stroke_width": 0},
            faded_line_ratio=5,
            background_line_style={
                "stroke_color": dracula.highlight2,
                # "stroke_width": 1,
            },
            faded_line_style={"stroke_width": 1},
        )
        self.add(bg, fg)
        fg.prepare_for_nonlinear_transform()
        fg.apply_complex_function(
            lambda z: 2 / z if z != 0 else complex(config.frame_x_radius, 0)
        )


class Zeta(Scene):
    def construct(self):
        bg = ComplexPlane()
        fg = ComplexPlane(
            x_range=x_range,
            y_range=y_range,
            axis_config={"stroke_width": 0},
            faded_line_ratio=5,
            background_line_style={
                "stroke_color": dracula.highlight2,
            },
            faded_line_style={"stroke_width": 1},
        )
        self.add(bg, fg)
        fg.prepare_for_nonlinear_transform()
        fg.apply_complex_function(zeta)
