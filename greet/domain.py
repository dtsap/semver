

class Dataset:
    pass


class Datasource:
    pass


dataset = Dataset()
dataset.add(Datasource("https://data.org"))
dataset.read()
dataset.show()
dataset.delete()
dataset.columns("column1")

