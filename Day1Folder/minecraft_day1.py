# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################

def on_chat():
    agent.teleport_to_player()
player.on_chat("tp", on_chat)
def on_chat2():
    agent.turn(TurnDirection.LEFT)
player.on_chat("tl", on_chat2)

def on_chat3():
    agent.turn(TurnDirection.RIGHT)
player.on_chat("tr", on_chat3)
def on_chat4(steps):
    agent.move(FORWARD, steps)
player.on_chat("fw", on_chat4)
def on_chat5(steps):
    agent.move(BACK, steps)
player.on_chat("bk", on_chat5)
def on_chat6(steps):
    agent.move(UP, steps)
player.on_chat("up", on_chat6)
def on_chat7(steps):
    agent.move(DOWN, steps)
player.on_chat("down", on_chat7)


################## On Chat Commands Section #####################
