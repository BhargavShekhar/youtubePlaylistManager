import os
import time
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    os.system('cls')

    if not videos:
        print("No videos available.")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

    print()
    input("Press enter to continue...")


def add_video(videos):
    os.system('cls')

    name = input("Enter video name: ")
    time = input("Enter video length: ")

    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_videos(videos):
    list_all_videos(videos)

    idx = int(input("Enter the video number to update: "))

    if 1 <= idx <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video length: ")
        videos[idx-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid video number selected")


def delete_videos(videos):
    list_all_videos(videos)

    idx = int(input("Enter the video number to update: "))

    if 1 <= idx <= len(videos):
        del videos[idx-1]
        save_data_helper(videos)
    else:
        print("Invalid video number selected")


def main():
    videos = load_data()

    while True:
        os.system('cls')

        print('------Welcome TO Youtube Manager------')
        print("1. List all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")
        choice = input("Enter Your Choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice!!")

        # time.sleep(2)

if __name__ == "__main__":
    main()