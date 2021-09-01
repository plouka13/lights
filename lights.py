from phue import Bridge
import readchar
import random

peters_room = ['Hue ambiance lamp 1', 'Hue ambiance lamp 2']
b = Bridge('192.168.1.5')

def lights_on ():
    for light in peters_room:
        b.set_light(light, 'on', True, transitiontime=1)

def lights_off ():
    for light in peters_room:
        b.set_light(light, 'on', False, transitiontime=1)

def lights_rainbow ():
    lights = b.get_light_objects()
    
    x, y = random.random(), random.random()
    for light in lights[0:2]:
        light.brightness = 254
        light.xy = [x, y]
        

print("press 1, 0 or x\n\n")
while True:
    val = readchar.readkey()
    if val == '1':
        lights_on()

    elif val == '0':
        lights_off()
    
    elif val == '2':
        for i in range(50):
            lights_rainbow()

    elif val == 'x':
        exit()
    
    


