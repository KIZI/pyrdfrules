from rich.console import Console
from rich.table import Table

def confusion_matrix(tp, fp, tn, fn):
    """
    Draw a confusion matrix.
    """
    
    Table.grid_style = "bold"
    
    table = Table(title="Confusion Matrix")
    
    table.add_column("", justify="center", style="white", no_wrap=True)
    table.add_column("In KG", justify="center", style="green", no_wrap=True)
    table.add_column("Not in KG", justify="center", style="red", no_wrap=True)
    table.add_row("Predicted", str(tp), str(fp))
    table.add_row("Not predicted", str(fn), str(tn))
    
    console = Console()
    console.print(table)