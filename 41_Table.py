
# Creating Table
from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title='User Data')


table.add_column('ID', justify='right', style='cyan', no_wrap=True)
table.add_column('Name', style='magenta')  
table.add_column('Age', justify='right', style='green')


table.add_row('1', 'Sushil', '21')
table.add_row('2', 'Sailendra', '21')
table.add_row('3', 'Ashish', '22')

console.print(table)
