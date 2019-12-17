from computer import Computer

comp = Computer("painter.txt")

result = comp.getOutput(0)
while(not result):
    result = comp.getOutput(1)

world = {}

