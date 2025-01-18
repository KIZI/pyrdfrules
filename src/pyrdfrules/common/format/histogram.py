from typing import List, Tuple


def draw_histogram(frequencies: dict[str, int], total: int|None = None) -> None:
    from rich import print
    from rich.table import Table

    max_freq = max(frequencies.values()) if total is None else total
    
    table = Table(title="Histogram")

    table.add_column("Instances")
    table.add_column("Name", justify="left")
    table.add_column("Chart")

    
    for key, freq in frequencies.items():
        table.add_row(str(freq), key, f"[bold magenta]{'█' * int(40 * freq / max_freq)}[/]")
        
    print(table)

    
    pass