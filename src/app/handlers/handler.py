from app.actions.action import Action


class Handler:
    action = None

    def __init__(self):
        self.action = Action()
