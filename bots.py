import threading
import json
import time

with open('inventory.dat') as file:
    data = file.read()
data = json.loads(data)

def bot_clerk(items):
    cart = []
    list1 = []
    list2 = []
    list3 = []
    num = 0
    lock = threading.Lock()

    for i in items:
        num += 1
        if (num == 1):
            list1.append(i)
        elif (num == 2):
            list2.append(i)
        elif (num == 3):
            list3.append(i)
            num = 0

    bot1 = threading.Thread(target=bot_fetcher, args=(list1, cart, lock))
    bot2 = threading.Thread(target=bot_fetcher, args=(list2, cart, lock))
    bot3 = threading.Thread(target=bot_fetcher, args=(list3, cart, lock))

    bot1.start()
    bot2.start()
    bot3.start()

    bot1.join()
    bot2.join()
    bot3.join()

    return cart


def bot_fetcher(items, cart, lock):
    for i in items:
        time.sleep(data[i][1])
        lock.acquire()
        cart.append([i, data[i][0]])
        lock.release()