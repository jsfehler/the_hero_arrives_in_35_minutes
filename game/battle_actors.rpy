init -500 python:
    class BattleActors(renpy.python.RevertableList):
        """Stores a list of Actors to use in battle.
        Actors in a BattleActors list should be swapped out using the
        change_battle_actor method. This allows every Actor in the group to
        keep track of the other Actors in the same group.
        """

        def add_actor(self, position, new_actor):
            """Add a new actor, maintaining and updating the list of allies.
            """
            self.insert(position, new_actor)

            # Replace list of allies
            new_actor.allies = [i for i in self if i != new_actor]

            # Update allies for other actors in group
            for actor in self:
                if actor != new_actor:
                    actor.allies.append(new_actor)

        def add_enemies(self, enemies_list):
            """Adds a list of enemies to each actor in the group."""
            for actor in self:
                actor.enemies = enemies_list

        def change_battle_actor(self, position, new_actor):
            """Swap an actor and ensure the allies and enemies are remapped
            correctly.
            """
            old_actor = self[position]

            self.pop(position)
            self.insert(position, new_actor)

            new_actor.allies = old_actor.allies
            new_actor.enemies = old_actor.enemies

            for actor in self:
                #for rule in actor.rules:
                #    if old_actor == rule.user:
                #        rule.user == new_actor
                # Replace old_actor in everyone's allies list
                if old_actor in actor.allies:
                    actor.allies.remove(old_actor)
                    actor.allies.append(new_actor)
                # Replace old_actor in everyone's enemies list
                if old_actor in actor.enemies:
                    actor.enemies.remove(old_actor)
                    actor.enemies.append(new_actor)
