import speech_recognition as sr
import pygame

# List of song names
song_names = ["Ev", "Gi", "Me"]
current_song_index = 0

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(song_names[current_song_index] + '.mp3')
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(song_names)
    stop_music()
    play_music()

def main():
    recognizer = sr.Recognizer()
    music_playing = False

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)

            recognized_text = recognizer.recognize_google(audio).lower()

            print("You said:", recognized_text)

            if "music" in recognized_text and not music_playing:
                print("Playing music...")
                play_music()
                music_playing = True
            elif "stop" in recognized_text and music_playing:
                print("Stopping music...")
                stop_music()
                music_playing = False
            elif "next" in recognized_text and music_playing:
                print("Playing next song...")
                play_next_song()

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
