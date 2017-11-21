class Company:
    def __init__(self, name):
        self.name = name
        self.ppc = []

    def get_performance(self):
        """
        used to calculate performance by taking average of all the profit per click calculated against keywords
        :return: average of all the profit per click
        """
        return sum(self.ppc)/float(len(self.ppc))
