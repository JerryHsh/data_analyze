from random import choice


class Randomwalk():
    """a class create random date"""

    def __init__(self, num_points=5000):
        """initialize the attribute"""
        self.num_points = num_points
        # all the random walk start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all the points contained in random walk"""
        # keep walking until the list reach the required length
        while len(self.x_values) < self.num_points:
            #decide which direction to go and how far to go
            x_direction=choice([-1,1])
            x_distance=choice(list(range(0,5)))
            x_step=x_direction*x_distance

            y_direction=choice([-1,1])
            y_distance=choice(list(range(0,5)))
            y_step=y_direction*y_distance

            #reject move that go nowhere
            if x_step==0 and y_step==0:
                continue

            #calculate the next x value and y value
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
