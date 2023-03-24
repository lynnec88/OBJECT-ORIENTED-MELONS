"""Classes for melon orders."""
class AbstractMelonOrder:
    order_type = None
    tax = 0

    def __init__(self, species, qty, shipped=False):
        self.species = species
        self.qty = qty
        self.shipped = shipped

    def get_total(self):
        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total
        
    def mark_shipped(self):
        
        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order purchased by the US Government."""

    order_type = "government"
    tax = 0.0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.pass_inspection = False
    
    def mark_inspection(self, passed):
        self.pass_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08
    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        
        # self.species = species
        # self.qty = qty
        # self.country_code = country_code
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code