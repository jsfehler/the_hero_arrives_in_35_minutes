init -1500 python:
    class BattleAction(object):
        """
        name (str)
        action (function)
        """
        def __init__(self, name, action, cost=0):
            self.name = name
            self.action = action
            self.cost = cost

        def use(self, user, targets):
            """Use an action."""
            if user.sp >= self.cost:
                user.sp -= self.cost

                return self.action(user, targets)
            return False


    def battle_action(action_name, cost=0):
        """Decorator to define new Battle Actions."""
        def decorator(func):
                action = BattleAction(name=action_name, action=func, cost=cost)
                var_name = action_name.lower().replace(' ', '_')
                globals()[var_name] = action

                return func

        return decorator


    def _hide_and_show_battle_numbers(position, amount, text_style):
        renpy.hide_screen('battle_number_display', layer=str(position))
        renpy.show_screen(
            'battle_number_display',
            position,
            amount,
            text_style=text_style,
            _layer=str(position)
        )


    def hide_and_show_damage(position, amount):
        """Ensures the damage text is hidden before showing a value."""
        _hide_and_show_battle_numbers(position, amount, 'damage_text')


    def hide_and_show_heal(position, amount):
        """Ensures the heal text is hidden before showing a value."""
        _hide_and_show_battle_numbers(position, amount, 'heal_text')
