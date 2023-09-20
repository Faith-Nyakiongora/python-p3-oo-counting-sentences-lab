import re


class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self.value = value

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        return False

    def count_sentences(self):
        if not self.value:
            return 0

        # Split the string on punctuation marks and filter out empty strings
        sentences = [s.strip() for s in re.split(r"[.!?]", self.value) if s.strip()]
        return len(sentences)
