from . import Place


class Water(Place):
    """Water is a place that can only hold watersafe fighters."""

    def add_fighter(self, fighter):
        """Add a Fighter to this place. If the fighter is not watersafe, reduce
        its armor to 0."""
        # BEGIN 4.1
        "*** YOUR CODE HERE ***"
        Place.add_fighter(self,fighter)
        if fighter.is_watersafe==False:
            fighter.armor=0
            self.remove_fighter(fighter)
            fighter.death_callback()
