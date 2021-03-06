from turtle import Turtle
# starting positions for my first three snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SEGMENT_SHAPE = 'square'
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.make_snakes()
        self.head = self.segments[0]

    def make_snakes(self):
        # this loop constructs my 3 starting snake segments
        # with designated shape, color, and position
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        # this for loop will help the tail segments of the snake move to
        # the location of the segment in front of them
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle(shape=SEGMENT_SHAPE)
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.make_snakes()
        self.head = self.segments[0]
