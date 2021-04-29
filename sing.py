import random
import sys
import subprocess
import argparse

# MacOS A Cappella
# by Otto Benson, 2/27/20

parser = argparse.ArgumentParser()
parser.add_argument("--live", help="perform the piece live", action="store_true")
args = parser.parse_args()

# North American English phonemes
phonemes = ["AE","EY","AO","AX","IY","EH","IH","AY","IX","AA","UW","UH","UX","OW","AW","OY"]
# single character phonemes
phonemes = phonemes + ["b","C","d","D","f","g","h","J","k","l","m","n","N","p","r","s","S","t","T","v","w","y","z","Z"]
# punctuation / functional phonemes
phonemes = phonemes + ["#","@","?",".",",","\""]

tune = "[[inpt TUNE; rate 80]]\n~"
for i in range(random.randint(1200, 1500)):
    break_chance = 2
    case = random.randint(0, break_chance)
    if case == break_chance: # chance to break a "word" = 1/break_chance
        prosodic_chance = random.randint(0,3)
        if prosodic_chance == 1:
            select = "~"
        if prosodic_chance == 2:
            select = "="
        if prosodic_chance == 3:
            select = "+"
        else:
            select = "_"
    else:
        select = str(random.choice(phonemes))
        decay = random.randint(10, 400)
        select = select + " {D " + str(decay) + "; P" # decay
        phoneme_percentage = 0 # percentage of phoneme
        for j in range(random.randint(1, 9)):
            random_freq = round(random.uniform(0, 800), 2)
            # -----chromatic tuning option (doesn't sound that different from random_freq with this implementation)-----
            # chromatic_raw = random.choice(
            #     [130.82, 138.59, 146.83, 155.56, 164.81, 174.61, 185, 196, 207.65, 220, 233.08, 246.94])
            # chromatic = random.randint(1, 3) * (chromatic_raw / 2)

            select = select + " " + str(random_freq)
            select = select + ":" + str(phoneme_percentage)
            if phoneme_percentage == 100:
                break
            else:
                phoneme_percentage = random.randint(phoneme_percentage, 100)
        select = select + "}"

    tune = tune + select + "\n"

tune = tune + "\n[[inpt TEXT]]"

if args.live:
    p = subprocess.Popen(["say", "-f", "-"], stdin=subprocess.PIPE, universal_newlines=True)
    p.communicate(tune)
else:
    sys.stdout = open('out.txt','w')
    print (tune)
    sys.stdout.close()
