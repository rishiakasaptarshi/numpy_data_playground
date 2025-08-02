try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt
except ModuleNotFoundError:
    print("The 'rich' module is not installed. Please install it using 'pip install rich' and try again.")
    exit(1)

from array_generator import generate_1d_array, generate_2d_array
from array_operations import arithmetic_operations, filter_even, filter_odd, row_col_sum, swap_rows, swap_columns, reshape_array
from array_utils import stack_arrays, concatenate_arrays

console = Console()

def display_menu():
    table = Table(title="NumPy Data Playground", show_lines=True)
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Action", style="magenta")
    menu_items = [
        ("1", "Generate Arrays"),
        ("2", "Perform Arithmetic Operations"),
        ("3", "Filter Even/Odd Numbers"),
        ("4", "Row & Column Sums"),
        ("5", "Swap Rows/Columns"),
        ("6", "Reshape Array"),
        ("7", "Stacking vs Concatenation"),
        ("0", "Exit"),
    ]
    for option, action in menu_items:
        table.add_row(option, action)
    console.print(table)

def main():
    arr1, arr2 = None, None
    while True:
        display_menu()
        choice = Prompt.ask("[bold green]Enter your choice[/]")

        if choice == "1":
            size = int(Prompt.ask("Enter size for 1D arrays"))
            arr1 = generate_1d_array(size)
            arr2 = generate_1d_array(size)
            console.print(Panel(f"[cyan]Array 1:[/] {arr1}\n[cyan]Array 2:[/] {arr2}", title="Generated Arrays"))

        elif choice == "2":
            if arr1 is None or arr2 is None:
                console.print("[red]Please generate arrays first![/]")
                continue
            results = arithmetic_operations(arr1, arr2)
            res_text = "\n".join([f"[bold]{op.title()}:[/] {res}" for op, res in results.items()])
            console.print(Panel(res_text, title="Arithmetic Operations", border_style="blue"))

        elif choice == "3":
            if arr1 is None:
                console.print("[red]Please generate an array first![/]")
                continue
            console.print(Panel(f"[cyan]Even Numbers:[/] {filter_even(arr1)}\n[cyan]Odd Numbers:[/] {filter_odd(arr1)}", title="Filtered Values"))

        elif choice == "4":
            rows = int(Prompt.ask("Rows for 2D array"))
            cols = int(Prompt.ask("Columns for 2D array"))
            arr2d = generate_2d_array(rows, cols)
            sums = row_col_sum(arr2d)
            console.print(Panel(f"[cyan]Array:[/]\n{arr2d}\nRow sums: {sums['row_sum']}\nColumn sums: {sums['col_sum']}", title="Row & Column Sums"))

        elif choice == "5":
            rows = int(Prompt.ask("Rows for 2D array"))
            cols = int(Prompt.ask("Columns for 2D array"))
            arr2d = generate_2d_array(rows, cols)
            r1 = int(Prompt.ask("Swap row index 1"))
            r2 = int(Prompt.ask("Swap row index 2"))
            arr2d = swap_rows(arr2d, r1, r2)
            c1 = int(Prompt.ask("Swap column index 1"))
            c2 = int(Prompt.ask("Swap column index 2"))
            arr2d = swap_columns(arr2d, c1, c2)
            console.print(Panel(f"[cyan]Modified Array:[/]\n{arr2d}", title="Swapped Array"))

        elif choice == "6":
            rows = int(Prompt.ask("Rows"))
            cols = int(Prompt.ask("Columns"))
            arr2d = generate_2d_array(rows, cols)
            new_shape = tuple(map(int, Prompt.ask("Enter new shape (e.g., 2,2,5)").split(',')))
            reshaped = reshape_array(arr2d, new_shape)
            console.print(Panel(f"[cyan]Reshaped Array:[/]\n{reshaped}", title="Reshaped"))

        elif choice == "7":
            size = int(Prompt.ask("Enter size for arrays"))
            arr1 = generate_1d_array(size)
            arr2 = generate_1d_array(size)
            console.print(Panel(f"[cyan]Array 1:[/] {arr1}\n[cyan]Array 2:[/] {arr2}", title="Arrays"))
            console.print(Panel(f"[cyan]Stacked Arrays:[/]\n{stack_arrays(arr1, arr2)}", title="Stacked"))
            console.print(Panel(f"[cyan]Concatenated Arrays:[/]\n{concatenate_arrays(arr1, arr2)}", title="Concatenated"))

        elif choice == "0":
            console.print("[green]Exiting... Goodbye![/]")
            break
        else:
            console.print("[red]Invalid choice! Try again.[/]")

if __name__ == "__main__":
    main()
