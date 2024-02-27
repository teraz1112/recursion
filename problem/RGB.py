class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def getHexCode(self):
        return '#'+format(self.red, '02x')+format(self.green, '02x')+format(self.blue, '02x')

    def getBits(self):
        return str(int(format(self.red, '08b')+format(self.green, '08b')+format(self.blue, '08b')))

    def getColorShade(self):
        if self.red == self.green == self.blue:
            return "grayscale"
        elif self.red >= self.green and self.red >= self.blue:
            return "red"
        elif self.green >= self.red and self.green >= self.blue:
            return "green"
        else:
            return "blue"

color1 = RGB(0, 153, 255)
color2 = RGB(255, 255, 204)
color3 = RGB(0, 87, 0)
gray = RGB(123, 123, 123)

print(color1.getHexCode())
print(color1.getBits())
print(color1.getColorShade())
print(color2.getHexCode())
print(color2.getBits())
print(color2.getColorShade())
print(color3.getHexCode())
print(color3.getBits())
print(color3.getColorShade())
print(gray.getHexCode())
print(gray.getBits())
print(gray.getColorShade())
