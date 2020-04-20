"""Some console related functions"""

from common.constants import bcolors
from objects import glob
import random


def printServerStartHeader(asciiArt):
	"""
	Print server start header with optional ascii art

	asciiArt -- if True, will print ascii art too
	"""

	if asciiArt:
		DaColour = random.choice([bcolors.BLUE, bcolors.YELLOW, bcolors.PINK, bcolors.RED, bcolors.GREEN])
		printColored(" (                 (     ", DaColour)
		printColored(" )\\ )        *   ) )\\ )  ", DaColour)
		printColored("(()/(  (   ` )  /((()/(  ", DaColour)
		printColored(" /(_)) )\\   ( )(_))/(_)) ", DaColour)
		printColored("(_))  ((_) (_(_())(_))   ", DaColour)
		printColored("| |   | __||_   _|/ __|  ", DaColour)
		printColored("| |__ | _|   | |  \\__ \\  ", DaColour)
		printColored("|____||___|  |_|  |___/  \n", DaColour)

	printColored("> Welcome to the Latest Essential Tatoe Server (RealistikOsu! ver)", bcolors.GREEN)
	printColored("> Common submodule v{}".format(glob.COMMON_VERSION), bcolors.GREEN)
	printColored("> Forked by RealistikOsu!", bcolors.GREEN)
	printColored("> Made by the Ripple team", bcolors.GREEN)
	printColored("> {}https://github.com/RealistikOsu/LETS".format(bcolors.UNDERLINE), bcolors.GREEN)
	printColored("> Press CTRL+C to exit\n", bcolors.GREEN)


def printNoNl(string):
	"""
	Print string without new line at the end

	string -- string to print
	"""

	print(string, end="")


def printColored(string, color):
	"""
	Print colored string

	string -- string to print
	color -- see bcolors.py
	"""

	print("{}{}{}".format(color, string, bcolors.ENDC))


def printError():
	"""Print error text FOR LOADING"""

	printColored("Error", bcolors.RED)


def printDone():
	"""Print error text FOR LOADING"""

	printColored("Done", bcolors.GREEN)


def printWarning():
	"""Print error text FOR LOADING"""

	printColored("Warning", bcolors.YELLOW)

def printGetScoresMessage(message):
	printColored("[get_scores] {}".format(message), bcolors.PINK)

def printSubmitModularMessage(message):
	printColored("[submit_modular] {}".format(message), bcolors.YELLOW)

def printBanchoConnectMessage(message):
	printColored("[bancho_connect] {}".format(message), bcolors.YELLOW)

def printGetReplayMessage(message):
	printColored("[get_replay] {}".format(message), bcolors.PINK)

def printMapsMessage(message):
	printColored("[maps] {}".format(message), bcolors.PINK)

def printRippMessage(message):
	printColored("[ripp] {}".format(message), bcolors.GREEN)

# def printRippoppaiMessage(message):
# 	printColored("[rippoppai] {}".format(message), bcolors.GREEN)

def printWifiPianoMessage(message):
	printColored("[wifipiano] {}".format(message), bcolors.GREEN)

def printDebugMessage(message):
	printColored("[debug] {}".format(message), bcolors.BLUE)

def printScreenshotsMessage(message):
	printColored("[screenshots] {}".format(message), bcolors.YELLOW)

def printApiMessage(module, message):
	printColored("[{}] {}".format(module, message), bcolors.GREEN)
