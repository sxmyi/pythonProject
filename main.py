import arcade

window = arcade.Window(700, 500, "Snowman")
arcade.start_render()


arcade.draw_rectangle_filled(100, 500, 1300, 700, arcade.color.DARK_BLUE)
arcade.draw_rectangle_filled(100, 50, 1600, 200, arcade.color.BLUE_GRAY)


arcade.draw_circle_filled(300, 200, 50, arcade.color.WHITE)
arcade.draw_circle_filled(300, 270, 40, arcade.color.WHITE)
arcade.draw_circle_filled(300, 320, 30, arcade.color.WHITE)

arcade.draw_circle_filled(310, 325, 4.5, arcade.color.BLACK)
arcade.draw_circle_filled(290, 325, 4.5, arcade.color.BLACK)
arcade.finish_render()
arcade.run()



