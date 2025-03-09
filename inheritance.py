class Music:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def show(self):
        print(f"Model is {self.model}, price is {self.price}")
class Violin(Music):
    def __init__(self, model, price, kolor1):
            super().__init__(model, price)
            self.kolor1 = kolor1
    def show(self):
        print(f"Model is {self.model}, price is {self.price}, color is {self.kolor1}")

class Guitar(Music):
    def __init__(self, model, price, type):
        super().__init__(model, price)
        self.type = type
    def show(self):
        print(f"Model is {self.model}, price is {self.price}, type is {self.type}")

instruments = [
    Violin("Abid", 100, "brown"),
    Violin("Yamaha", 1500, "black"),
    Violin("Stina", 820, "red"),
    Violin("Comod", 1200, "brown"),
    Guitar("Fiol", 950, "elect"),
    Guitar("Gibson", 2000, "acustic"),
    Guitar("Ibanez", 700, "bass")
]
most_expensive = instruments[0]

for instrument in instruments:
    if instrument.price > most_expensive.price:
        most_expensive = instrument
most_expensive.show()