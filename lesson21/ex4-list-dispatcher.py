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
    List to hold turns of all (visitor,officer)
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


# main
manager = OfficerQueuesManager()

commands = {
    'wait': manager.push,
    'next': manager.pop,
}

while True:

    try:
        cmd, *params = command = input("Please enter <action> <officer> <visitor>|optional : ")\
            .strip().split()
        cur_officer, *_ = params
        cur_turn = commands[cmd](*params)
        if cur_turn is not None:
            try:
                print(f"{cur_turn.visitor}")
            except Exception:
                print(f"{cur_officer} queue is empty")
    except Exception:
        print("Illegal format, try again.")
        continue

    manager.print()
