import multiprocessing


def calculate_currency(money, rate, conn):
    currency = money * rate
    conn.send(currency)
    conn.close()


if __name__ == '__main__':
    rate = 75

    conn1, conn2 = multiprocessing.Pipe()
    p = multiprocessing.Process(target=calculate_currency, args=(100, rate, conn2))
    p.start()

    while True:
        if conn1.poll():
            currency = conn1.recv()
            print(f'You can buy {currency} currency for 100 money')
            break

    p.join()