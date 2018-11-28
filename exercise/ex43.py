# Basic Object-Oriented Analysis and Design

# [1] Bottom Up approach
# 1. Take a small piece of the problem; hack on some code and get it to run barely.
# 2. Refine the code into something more formal with classes and automated tests.
# 3. Extract the key concepts you’re using and try to find research for them.
# 4. Write a description of what’s really going on.
# 5. Go back and refine the code, possibly throwing it out and starting over.
# 6. Repeat, moving on to some other piece of the problem.

# [1] Top Down approach
# 1. Write or draw about the problem.
# 2. Extract key concepts from 1 and research them.
# 3. Create a class hierarchy and object map for the concepts.
# 4. Code the classes and a test to run them.
# 5. Repeat and refine.


class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
