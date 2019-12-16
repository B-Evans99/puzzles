from colorama import init, Fore, Back, Style
init()

image = []

length = 25
height = 6

fullLayer = length * height

for i in open("fullImage.txt"):
    raw = list(i)
    for i in raw:
        image.append(int(i))

layers = []
start = 0
end = fullLayer

while(end <= len(image)):
    layers.append(image[start:end])
    start += fullLayer
    end += fullLayer

finished = layers[0][:]

for layer in layers:
    for (i, val) in enumerate(finished[:]):
        if(val == 2):
            finished[i] = layer[i]

for (i, val) in enumerate(finished):
    if (val == 0):
        print(Fore.RED + "█", end="")
    else:
        print(Fore.WHITE + "█", end="")
    if(i % 25 == 24):
        print()
