import collections

"""
Holds queues dictionary connects officer to queue list.
"""


class OfficerQueuesManager:
    """
    Dictionary to hold officers queues
    """

    def __init__(self):
        self._queues_dict = collections.defaultdict(list)

    def push(self, officer, visitor):
        self._queues_dict[officer].append(visitor)

    def pop(self, officer):
        try:
            return self._queues_dict[officer].pop(0)
        except IndexError:
            return f"officer {officer} queue is empty"

    def print(self):
        print(self._queues_dict.items())


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
        print(manager.pop(cur_officer))

    # manager.print()
