import os
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.console import Console
console = Console()
# todo need to add more conversions and possibly other mathematical things (e.g. currency, basic calculations etc.)
choice = ''
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Panel("[bold magenta]Choose unit to convert:\n[blue]1) Miles\n2) Yards\n3) Inches", expand=True, padding=2))
    console.rule()
    choice = Prompt.ask(choices=["1", "2", "3"])
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == '1':
        print(Panel("[bold magenta]Miles"))
        choice_miles = ''
        while True:
            print(Panel("[bold magenta]What would you like to convert miles into?\n[blue]1) Centimetres\n2) "
                        "Metres\n3) Kilometres", expand=True, padding=2))
            console.rule()
            choice_miles = Prompt.ask(choices=["1", "2", "3"])
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice_miles == '1':
                print(Panel("[bold magenta]Miles to Centimetres"))
                console.rule()
                miles = Prompt.ask("Enter miles")
                miles = int(miles)
                centimetres = miles * 160934.4
                result_miles_cm = Panel(Text(str(centimetres) + " cm", justify="center", style="bold magenta"), expand=True, padding=0)
                print(result_miles_cm)
                break
            elif choice_miles == '2':
                print(Panel("[bold magenta]Miles to Metres"))
                console.rule()
                miles = Prompt.ask("Enter miles")
                miles = int(miles)
                metres = miles * 1609.344
                result_miles_m = Panel(Text(str(metres) + " m", justify="center", style="bold magenta"), expand=True, padding=0)
                print(result_miles_m)
                break
            elif choice_miles == '3':
                print(Panel("[bold magenta]Miles to Kilometres"))
                console.rule()
                miles = Prompt.ask("Enter miles")
                miles = int(miles)
                kilometres = miles * 1.609
                result_miles_km = Panel(Text(str(kilometres) + " km", justify="center", style="bold magenta"), expand=True, padding=0)
                print(result_miles_km)
                break
            else:
                print('Type a number from 1-3 : ')
                continue
        break
    elif choice == '2':
        print(Panel("[bold magenta]Yards"))
        choice_yards = ''
        while True:
            print(Panel("What would you like to convert yards into?\n[blue]1) "
                        "Centimetres\n2) Metres\n3) Kilometres", expand=True, padding=2))
            console.rule()
            choice_yards = Prompt.ask(choices=["1", "2", "3"])
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice_yards == '1':
                print(Panel("[bold magenta]Yards to Centimetres"))
                console.rule()
                yards = Prompt.ask("Enter yards")
                yards = int(yards)
                centimetres = yards * 91.44
                result_yards_cm = Panel(Text(str(centimetres) + " cm", justify="center", style="bold magenta"), expand=True, padding=0)
                print(result_yards_cm)
                break
            elif choice_yards == '2':  # todo prettify the output from here on
                print('Yards to Metres')
                yards = input("Enter yards: ")
                yards = int(yards)
                metres = yards * 0.91
                print(metres)
                break
            elif choice_yards == '3':
                print('Yards to Kilometres')
                yards = input("Enter yards: ")
                yards = int(yards)
                kilometres = yards * 0.000914
                print(kilometres)
                break
            else:
                print('Type a number from 1-3 : ')
                continue
        break
    elif choice == '3':
        print('Inches')
        choice_inches = ''
        while True:
            choice_inches = input("What would you like to convert inches into? 1) Centimetres 2) Metres 3) Kilometres "
                                  ": ")
            if choice_inches == '1':
                print('Inches to Centimetres')
                inches = input("Enter inches: ")
                inches = int(inches)
                centimetres = inches * 2.54
                print(centimetres)
                break
            elif choice_inches == '2':
                print('Inches to Metres')
                inches = input("Enter inches: ")
                inches = int(inches)
                metres = inches * 0.0254
                print(metres)
                break
            elif choice_inches == '3':
                print('Inches to kilometres')
                inches = input("Enter inches: ")
                inches = int(inches)
                kilometres = inches * 0.0000254
                print(kilometres)
                break
            else:
                print('Type a number from 1-3 : ')
                continue
        break
    else:
        print('Type a number from 1-3 : ')
        continue
