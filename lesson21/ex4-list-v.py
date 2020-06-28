"""
Holds list of Turn objects represents queues.

ynonp06/25/2020
לגבי תרגיל 4 - יש לי תחושה שהיה יותר קל לשמור רשימה אחת של ״ממתינים״,
 ואז כשפקיד מתפנה לחפש את הממתין הבא שמחכה לו, ואם אין כזה להזמין את הממתין הבא הכללי
"""


class Turn:
    def __init__(self, visitor, officer):
        self.visitor = visitor
        self.officer = officer


class OfficerQueuesManager:
    """
    Dictionary to hold officers queues
    """

    def __init__(self):
        self.turns = []

    def push(self, officer, visitor):
        turn = Turn(visitor, officer)
        self.turns.append(turn)

    def pop(self, officer):
        try:
            # And to get a specific clerk's visitor we'll have:
            cur_officer_turns = [turn for turn in self.turns if turn.officer == officer]
            cur_officer_turn = cur_officer_turns.pop(0)
            self.turns.remove(cur_officer_turn)
            return cur_officer_turn

        except IndexError:
            return f"officer {officer} queue is empty"

    def print(self):
        for turn in self.turns:
            print(f"{turn.visitor, turn.officer}")


"""
To hold each iteration command parts <action> <officer> <visitor>,
to send to manager.
"""


class Command:
    PUSH_ACTION = 'wait'
    POP_ACTION = 'next'

    def __init__(self):
        self._action = None
        self._officer = None
        self._visitor = None

    def parse_commands_list(self):
        """
        parse and assign
        """
        while True:
            command = input("Please enter <action> <officer> <visitor>|optional : ")
            commands_list = command.strip().split(" ")
            if len(commands_list) not in [2, 3]:
                print("Illegal format, try again.")
                continue

            if len(commands_list) == 3:
                [self._action, self._officer, self._visitor] = commands_list
            elif len(commands_list) == 2:
                [self._action, self._officer] = commands_list

            if not self.validate_commands_list():
                print("Illegal format, try again.")
                continue
            return

    def validate_commands_list(self):
        if self._action == Command.PUSH_ACTION and len(self._officer) > 0 and len(self._visitor) > 0:
            return True
        elif self._action == Command.POP_ACTION and len(self._officer) > 0 and self._visitor is None:
            return True
        else:
            return False

    def get_commands_list(self):
        return [self._action, self._officer, self._visitor]


# main
manager = OfficerQueuesManager()
while True:

    cur_command = Command()
    cur_command.parse_commands_list()
    [cur_action, cur_officer, cur_visitor] = cur_command.get_commands_list()

    if cur_action == Command.PUSH_ACTION:
        manager.push(cur_officer, cur_visitor)
    if cur_action == Command.POP_ACTION:
        try:
            cur_turn = manager.pop(cur_officer)
            print(f"{cur_turn.visitor}")
        except Exception:
            print(f"{cur_officer} queue is empty")


    manager.print()
