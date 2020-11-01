from random import randrange

from Item import Item


class ItemsInitilizer:

    @staticmethod
    def initilizeItems():
        ITEMS = [Item() for i in range(11)]
        ITEMS[0] = Item(100, 7)
        ITEMS[1] = Item(300, 7)
        ITEMS[2] = Item(200, 6)
        ITEMS[3] = Item(40, 2)
        ITEMS[4] = Item(500, 5)
        ITEMS[5] = Item(70, 6)
        ITEMS[6] = Item(100, 1)
        ITEMS[7] = Item(250, 3)
        ITEMS[8] = Item(300, 10)
        ITEMS[9] = Item(280, 3)
        ITEMS[10] = Item(300, 15)
        return ITEMS

    @staticmethod
    def initilizeItemsLarge(size):
        ITEMS = []
        for i in range(0, size):
            ITEMS.append(Item(randrange(10, 310, 10), randrange(1, 16, 1)))
        return ITEMS
