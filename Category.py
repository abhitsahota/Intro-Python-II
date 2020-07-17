class Category:
    def __init__(self, name, desc, products):
        self.name = name
        self.desc = desc
        self.products = products

    def __str__(self):
        return f' {self.name}: {self.desc}'