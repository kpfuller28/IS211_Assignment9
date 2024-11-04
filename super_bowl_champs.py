from bs4 import BeautifulSoup
import urllib.request


def main():
    url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
    with urllib.request.urlopen(url) as response:
        response = response.read().decode("utf-8")
    soup = BeautifulSoup(response, "lxml")

    tables = soup.find_all("table", {"class": "wikitable"})
    superBowlTable = tables[1]
    rows = superBowlTable.find_all("tr")
    teams = {}

    for row in rows:
        cell = row.find_all("td")
        cellData = [
            value.find("a").contents[0]
            for value in cell
            if value.find("a") and value.find("a").contents[0] != "OT"
        ]
        if len(cellData) > 0:
            winner = cellData[2]
            loser = cellData[3]

            if winner in teams:
                teams[winner]["wins"] += 1
                teams[winner]["appearances"] += 1
            else:
                teams[winner] = {"wins": 1, "appearances": 1}
            if loser in teams:
                teams[loser]["appearances"] += 1
            else:
                teams[loser] = {"wins": 0, "appearances": 1}
    displayTeams = sorted(
        teams.items(), reverse=True, key=lambda x: (x[1]["wins"], x[1]["appearances"])
    )
    print(f"{'Team':<30}{'Super Bowl Wins':<20}{'Appearances':<15}")
    for team in displayTeams:
        print(f"{team[0]:<30}{team[1]['wins']:<20}{team[1]['appearances']:<15}")


main()


if __name__ == "__main__":
    pass
