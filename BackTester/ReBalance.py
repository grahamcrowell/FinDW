
class Portfolio(object):
    def __init__(self):
        raw = []
        with open('3stocks.csv') as f:
            raw = f.readlines()
        print(raw)


if __name__ == '__main__':
    p = Portfolio()
