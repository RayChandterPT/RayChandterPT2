import pygame

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist

    def play_music(self):
        pygame.mixer.init()

        for song in self.playlist:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()

            print(f"Now playing: {song}")

            while pygame.mixer.music.get_busy():
                continue

def main():
    playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]

    player = MusicPlayer(playlist)
    player.play_music()

if __name__ == "__main__":
    main()
