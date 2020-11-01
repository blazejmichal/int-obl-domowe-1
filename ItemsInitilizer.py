from Item import Item


class ItemsInitilizer:

    @staticmethod
    def initilizeItems():
        ITEMS = [Item() for i in range(11)]
        ITEMS[0] = Item(100, 7, "zegar")
        ITEMS[1] = Item(300, 7, "obraz-pejzaz")
        ITEMS[2] = Item(200, 6, "obraz-portret")
        ITEMS[3] = Item(40, 2, "radio")
        ITEMS[4] = Item(500, 5, "laptop")
        ITEMS[5] = Item(70, 6, "lampka nocna")
        ITEMS[6] = Item(100, 1, "srebrne sztucce")
        ITEMS[7] = Item(250, 3, "porcelana")
        ITEMS[8] = Item(300, 10, "figura z brazu")
        ITEMS[9] = Item(280, 3, "skorzana torebka")
        ITEMS[10] = Item(300, 15, "odkurzacz")
        return ITEMS