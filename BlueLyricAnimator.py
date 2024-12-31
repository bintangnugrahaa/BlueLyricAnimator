import time
import sys

# Updated lyrics
lyrics = [
    ("I imagine we fell in love", 0.10),
    ("I'll nap under moonlight skies with you", 0.12),
    ("I think I'll picture us, you with the waves", 0.11),
    ("The ocean's colors on your face", 0.10),
    ("I'll leave my heart with your air", 0.12),
    ("So let me fly with you", 0.11),
    ("Will you be forever with me?", 0.12),
    "",
    ("My love will always stay by you", 0.10),
    ("I'll keep it safe, so don't you worry a thing, I'll tell you I love you more", 0.12),
    ("It's stuck with you forever, so promise you won't let it go", 0.11),
    ("I'll trust the universe will always bring me to you", 0.10),
]

# Delays between lines
delays = [8.8, 8.8, 8.1, 8.1, 8.1, 8.1, 8.8, 8.8, 8.8, 8.1, 8.8, 8.8]

def animate_text(text, char_delay):
    """Function to animate text, displaying each character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    """Main function to display lyrics with delays between each line."""
    for i, (text, char_delay) in enumerate(lyrics):
        animate_text(text, char_delay)
        if i < len(lyrics) - 1:
            # Calculate the time until the next line should start
            next_line_delay = max(0, delays[i] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()
