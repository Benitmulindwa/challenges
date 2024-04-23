from flet import *


def main(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = "white"
    page.theme_mode = "light"
    page.window_width = 370
    page.window_height = 720

    eyes = Row(
        [
            Container(
                width=20,
                height=20,
                bgcolor=colors.CYAN,
                border_radius=10,
                border=border.all(5, color=colors.CYAN),
            ),
            Row(expand=True),
            Container(
                width=20,
                height=20,
                bgcolor=colors.CYAN,
                border_radius=10,
                border=border.all(5, color=colors.CYAN),
            ),
        ],
        top=90,
        left=60,
        right=60,
    )

    emoji = Container(
        Stack(
            [
                eyes,
                Container(
                    LineChart(
                        data_series=[
                            LineChartData(
                                data_points=[
                                    LineChartDataPoint(1, 0),
                                    LineChartDataPoint(2, 0),
                                    LineChartDataPoint(3, 0),
                                ],
                                color=colors.CYAN,
                                stroke_width=5,
                                curved=True,
                                stroke_cap_round=True,
                            ),
                        ],
                        max_y=5,
                        max_x=3,
                    ),
                    margin=margin.only(bottom=60, left=60, right=60),
                ),
            ]
        ),
        width=260,
        height=260,
        border_radius=130,
        border=border.all(5, color=colors.CYAN),
    )

    def get_value(e):
        val = e.control.value
        smile = emoji.content.controls[1].content.data_series[0].data_points[1]
        smile.y = -val
        emoji.update()

    page.add(
        emoji,
        Container(
            Slider(
                adaptive=True,
                value=0.0,
                min=-0.9,
                max=0.9,
                active_color=colors.CYAN,
                on_change=get_value,
            ),
            margin=margin.only(top=50),
        ),
    )


app(target=main)
