from rich.console import Console
from time import sleep

console = Console()

# data = [1, 2, 3, 4, 5]

_id = input("Hapus data > ")
with console.status("[bold green]Fetching data...") as status:
    sleep(1)
    console.log(f" Id {_id} deleted!")
#     while data:
#         num = data.pop(1)
#         sleep(1)
#         console.log(f"[green]Finish fetching data[/green] {num}")

#     console.log(f'[bold][red]Done!')