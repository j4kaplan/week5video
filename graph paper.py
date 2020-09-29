import arcade
def draw_lines ():
    arcade.open_window(800,800,"lines demo")
    arcade.set_background_color(arcade.color.APPLE_GREEN)
    width= arcade.get_window().width
    height= arcade.get_window().height
    arcade.start_render()
    #drawing goes here
    for location in range (80,width, 80):
        arcade.draw_line(location,0,location, height, arcade.color.BLACK_OLIVE, 2)
        for location2 in range (80,height,80):
            arcade.draw_line(0, location2,width, location2,arcade.color.BLACK_OLIVE,2)
    arcade.finish_render()

    arcade.run()


draw_lines()
