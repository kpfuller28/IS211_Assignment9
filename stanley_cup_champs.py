
from bs4 import BeautifulSoup
import urllib.request


def main():
    url = "https://en.wikipedia.org/wiki/List_of_Stanley_Cup_champions"
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')
    soup = BeautifulSoup(response, 'lxml')

    # Find all tables with the "wikitable" class and select the third one (index 2)
    tables = soup.find_all('table', {"class": "wikitable"})
    stanley_cup_table = tables[2]  # Third table on the page

    rows = stanley_cup_table.find_all('tr')

    # Initialize a dictionary to store rowspan values for year, winning team, and runner-up
    rowspan_tracker = {}

    # Print header for table
    print(f"{'Year':<10} {'Winning Team':<30} {'Runner-up':<30}")
    print("-" * 70)

    # Loop through rows and handle rowspans
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all(['th', 'td'])
        data = []

        # Go through each cell
        for idx, cell in enumerate(cells):
            # Check for rowspan attribute
            rowspan = cell.get('rowspan')
            if rowspan:
                rowspan_tracker[idx] = (cell.text.strip(), int(rowspan) - 1)
                data.append(cell.text.strip())
            elif idx in rowspan_tracker:
                # Use value from rowspan_tracker if available
                data.append(rowspan_tracker[idx][0])
                rowspan_tracker[idx] = (rowspan_tracker[idx][0], rowspan_tracker[idx][1] - 1)
                if rowspan_tracker[idx][1] == 0:
                    del rowspan_tracker[idx]
            else:
                data.append(cell.text.strip())

        # Extract only the columns for Year, Winning Team, and Runner-up, adjusting based on cell content
        if len(data) >= 3:
            year = data[0]
            winning_team = data[1]
            runner_up = data[4]
            print(f"{year:<10} {winning_team:<30} {runner_up:<30}")



main()


if __name__ == "__main__":
    pass
