import math
import time
import turtle


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
SPINNER_RADIUS = 120
ARM_LENGTH = 100
ARM_WIDTH = 18
CENTER_RADIUS = 28

BACKGROUND_COLOR = "#202124"
ARM_COLORS = ("#ff4d4d", "#4caf50", "#4285f4")

MIN_SPEED = 0.2
MAX_SPEED = 18.0
SPIN_BOOST = 4.0
FRICTION = 0.97


class FidgetSpinner:
    """Interactive fidget spinner with momentum-based animation."""

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen.title("Fidget Spinner")
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.tracer(0)

        self.spinner = turtle.Turtle()
        self.spinner.hideturtle()
        self.spinner.speed(0)

        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color("white")
        self.speed_bar = turtle.Turtle()
        self.speed_bar.hideturtle()
        self.speed_bar.speed(0)

        self.angle = 0.0
        self.speed = 0.0
        self.spin_count = 0
        self.running = True
        self.last_time = time.perf_counter()

        self._bind_controls()
        self._draw_interface()

    def _bind_controls(self):
        """Set up keyboard and mouse controls."""
        self.screen.listen()
        self.screen.onkey(self.spin, "space")
        self.screen.onkey(self.reset, "r")
        self.screen.onkey(self.quit, "Escape")
        self.screen.onclick(self._mouse_spin)

    def _mouse_spin(self, x, y):
        """Spin the spinner when the user clicks the window."""
        self.spin()

    def spin(self):
        """Add rotational momentum to the spinner."""
        self.speed = min(
            self.speed + SPIN_BOOST,
            MAX_SPEED,
        )
        self.spin_count += 1

    def reset(self):
        """Reset the spinner angle, speed and counter."""
        self.angle = 0.0
        self.speed = 0.0
        self.spin_count = 0
        self._draw_interface()

    def quit(self):
        """Close the application."""
        self.running = False
        self.screen.bye()

    def _draw_spinner(self):
        """Draw the three-arm spinner."""
        self.spinner.clear()

        for index, color in enumerate(ARM_COLORS):
            arm_angle = math.radians(
                self.angle + index * 120
            )

            end_x = math.cos(arm_angle) * ARM_LENGTH
            end_y = math.sin(arm_angle) * ARM_LENGTH

            self.spinner.penup()
            self.spinner.goto(0, 0)
            self.spinner.pendown()

            self.spinner.color(color)
            self.spinner.width(ARM_WIDTH)
            self.spinner.goto(end_x, end_y)

            self.spinner.penup()
            self.spinner.goto(end_x, end_y)
            self.spinner.dot(70, color)

        self.spinner.goto(0, 0)
        self.spinner.dot(
            CENTER_RADIUS * 2,
            "#eeeeee",
        )

        self.spinner.dot(
            CENTER_RADIUS,
            "#303030",
        )

    def _draw_interface(self):
        """Draw the spinner and information text."""
        self._draw_spinner()
        self.speed_bar.clear()
        self.speed_bar.penup()
        self.speed_bar.goto(-120, -245)
        self.speed_bar.pendown()
        bar_width = 240
        filled_width = bar_width * (self.speed / MAX_SPEED)

        self.speed_bar.color("#555555")
        self.speed_bar.width(12)
        self.speed_bar.forward(bar_width)

        self.speed_bar.penup()
        self.speed_bar.goto(-120, -245)
        self.speed_bar.pendown()
        self.speed_bar.color("#4caf50")
        self.speed_bar.forward(filled_width)

        self.info.clear()
        self.info.goto(
            0,
            -WINDOW_HEIGHT // 2 + 25,
        )

        self.info.write(
            f"SPINS: {self.spin_count}    SPEED: {self.speed:.1f}",
            align="center",
            font=("Arial", 16, "bold"),
        )

        self.info.goto(
            0,
            WINDOW_HEIGHT // 2 - 50,
        )

        self.info.write(
            "SPACE / Click = Spin    "
            "R = Reset    ESC = Quit",
            align="center",
            font=("Arial", 12, "normal"),
        )

        self.screen.update()

    def update(self):
        """Update the spinner animation."""
        if not self.running:
            return

        current_time = time.perf_counter()
        elapsed = current_time - self.last_time
        self.last_time = current_time

        self.angle += self.speed * elapsed * 60
        self.speed *= FRICTION ** (elapsed * 60)

        if self.speed < MIN_SPEED:
            self.speed = 0.0

        self._draw_interface()

        self.screen.ontimer(
            self.update,
            16,
        )

    def run(self):
        """Start the animation loop."""
        self.update()
        self.screen.mainloop()


def main():
    game = FidgetSpinner()
    game.run()


if __name__ == "__main__":
    main()
