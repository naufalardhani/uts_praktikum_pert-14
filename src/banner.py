from src.util.color import Color

from sys import stdout
from time import sleep
import time

def show_banner():
    txt = f"""

    {Color.CPURPLE2}██╗███╗   ██╗███████╗    ███████╗██╗  ██╗██████╗ ██████╗ ███████╗███████╗███████╗
    {Color.CPURPLE2}██║████╗  ██║██╔════╝    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    {Color.CPURPLE2}██║██╔██╗ ██║█████╗█████╗█████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ███████╗███████╗
    {Color.CPURPLE2}██║██║╚██╗██║██╔══╝╚════╝██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║
    {Color.CPURPLE2}██║██║ ╚████║██║         ███████╗██╔╝ ██╗██║     ██║  ██║███████╗███████║███████║
    {Color.CPURPLE2}╚═╝╚═╝  ╚═══╝╚═╝         ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
    
                   """
    
    credit = f">{Color.ENDC} Ekspedisi Dalam Negeri Terbaik di Indonesia{Color.ENDC}\n\n"
    
    for col in txt:
        print(col, end="")
        stdout.flush()
        sleep(0.001)
    
    for col in credit:
        print(col, end="")
        stdout.flush()
        sleep(0.028)
