"""
CLI for the Wiki Route application
"""

from wiki_path_finder import find_shortest_path

def main():
    print("Wiki Route")
    start_title = input("enter the title of the starting Wiki article: ")
    end_title = input("enter the title of the ending Wiki article: ")

    print("finding the shortest path...")
    path = find_shortest_path(start_title, end_title)

    if path:
        print("shortest path found!")
        for title in path:
            print(f"-> {title}")
    else:
        print("sorry, no path was found between the two given articles")

if __name__ == "__main__":
    main()