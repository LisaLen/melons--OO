"""Classes for melon orders."""

class AbstractMelonOrdder():

    def __init__(self, species, qty, factor = 1 ):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.factor = factor

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5 * self.factor
        total = (1 + self.tax) * self.qty * base_price

        return total
        
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrdder):
    """A melon order within the USA."""

    """Initialize melon order attributes."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrdder):
    """An international (non-US) melon order."""

    """Initialize melon order attributes."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code
      
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
class GovernmentMelonOrder(AbstractMelonOrdder):

    passed_inspection = False
    order_type = "goverment"

    def mark_inspection(self, passed):
        if self.passed:
            self.passed_inspection = True


