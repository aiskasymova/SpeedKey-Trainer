from collections import defaultdict


class User:
    def __init__(self, file_name):
        self.list_of_sentences = []
        self.prompt = self.get_sentence(file_name)
        self.prompt_ptr = 0
        self.input = ''
        self.start_time = 0
        self.time_taken = 0
        self.timer_started = False
        self.end = False
        self.accuracy = 0
        self.wpm = 0
        self.result = ''
        self.error_count = 0
        self.heat_map = defaultdict(int)

    def get_sentence(self, file_name):
        if len(self.list_of_sentences) == 0:
            self.read_file(file_name)

        return ' '.join(self.list_of_sentences.pop(0)) if len(self.list_of_sentences) > 0 else ''

    def read_file(self, file_name):
        with open(file_name) as words:
            for line in words:
                line_words = line.split()
                self.list_of_sentences += [line_words[i:i + 6] for i in range(0, len(line_words), 6)]

    # [['word1', 'word2']['word1', 'word2']]

    def read_letter(self, event, letter):
        if self.prompt_ptr < len(self.prompt) and self.prompt[self.prompt_ptr] == letter:
            try:
                self.input += event.unicode
                self.prompt_ptr += 1
            except:
                pass
        else:
            self.error_count += 1
            self.heat_map[letter] += 1
