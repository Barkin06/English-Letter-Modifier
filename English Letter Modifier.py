import os

def replace_turkish_chars(text):
    """Replace Turkish characters in a string with their English counterparts."""
    replacements = {
        "İ": "I",
        "ı": "i",
        "ş": "s",
        "ü": "u",
        "ö": "o",
        "ç": "c",
        "Ğ": "G",
        "ğ": "g",
        "Ş": "S",
        "Ü": "U",
        "Ö": "O",
        "Ç": "C",
    }
    for turkish_char, english_char in replacements.items():
        text = text.replace(turkish_char, english_char)
    return text

def print_filenames_with_english_chars(path):
    """Print the filenames in a directory with Turkish characters replaced by English characters."""
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_file():
            filename = entry.name
            filename = filename.replace("ı", "i").replace("İ", "I")
            english_filename = replace_turkish_chars(filename)
            print(f"{filename} -> {english_filename}")

#Dont forget to change path with yours

path = r"C:\Users\Salih\Dropbox\PC\Desktop\ASDF"
print_filenames_with_english_chars(path)
