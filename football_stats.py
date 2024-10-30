from bs4 import BeautifulSoup
import urllib.request


def main():
    url="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')
    soup = BeautifulSoup(response, features='lxml')

    statTable = soup.find('tbody')
    trs = statTable.find_all('tr')
    print(f"{'Name':<25} {'Position':<10} {'Team':<10} {'TDs':<5}")
    print("-" * 55)
    for i in range(20):
        statLine = trs[i]
        # print(statLine)
        # print('----------------------')
        name = statLine.find(class_="CellPlayerName--long").find('a').contents[0].strip()
        position = statLine.find(class_="CellPlayerName-position").contents[0].strip()
        team = statLine.find(class_="CellPlayerName-team").contents[0].strip()
        touchdowns = statLine.find_all(class_="TableBase-bodyTd TableBase-bodyTd--number")[7].contents[0].strip()
        print(f"{name:<25} {position:<10} {team:<10} {touchdowns:<5}")





if __name__ == "__main__":
    pass

main()
