import collections

"""
Holds queues dictionary connects officer to queue list.
Also manages _not_empty_queues set, 
so free officer takes other busy officers visitors.
"""


class OfficerQueuesManager:
    """
    Dictionary to hold officers queues
    """

    def __init__(self):
        self._queues_dict = collections.defaultdict(list)
        self._not_empty_queues = set()

    def push(self, officer, visitor):
        self._queues_dict[officer].append(visitor)
        self._not_empty_queues.add(officer)

    def pop(self, officer):
        try:
            visitor = self._queues_dict[officer].pop(0)
            if len(self._queues_dict[officer]) == 0:
                self._not_empty_queues.remove(officer)
        except IndexError:
            if len(self._not_empty_queues) > 0:
                busy_officer = list(self._not_empty_queues)[0]
                visitor = self._queues_dict[busy_officer].pop(0)
                if len(self._queues_dict[busy_officer]) == 0:
                    self._not_empty_queues.remove(busy_officer)
            else:
                visitor = f"{officer} and all other officers queues are empty"
        return visitor

    def print(self):
        print(self._queues_dict.items())
        print(self._not_empty_queues)


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
