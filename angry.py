from smiley import Smiley

class Angry(Smiley):
    """
    Provides a Smiliey with an angry expression
    """
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_eyes()
        self.draw_mouth()

    def draw_eyes(self):
        """
        Draw angry eyes for the smiley by blanking pixels
        """
        eyes = [17, 18, 26, 21, 22, 29]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK

    def draw_mouth(self):
        """
        Draw an angry mouth for the smiley by blanking pixels
        """
        mouth = [42,43,44,45,49,54]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK