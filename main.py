from typing import Optional

class FileWordAnalyzer:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    def read_words(self) -> list:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read().split()
        except FileNotFoundError:
            print("File not found.")
            return []

    def find_longest_word(self) -> Optional[str]:
        words = self.read_words()
        longest_word: Optional[str] = None

        for word in words:
            if longest_word is None or len(word) > len(longest_word):
                longest_word = word

        return longest_word


if __name__ == "__main__":
    analyzer = FileWordAnalyzer("sample.txt")
    print(analyzer.find_longest_word())
