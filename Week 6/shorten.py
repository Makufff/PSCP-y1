"""Shorten"""
class NumberGrouper:
    """NumberGrouper Class"""
    def __init__(self):
        """init function"""
        self.group = ""
        self.continuity = False
        self.previous_num = None

    def get_input(self):
        """เบื่อ input แล้ว เลยอยาก get_input"""
        return input()

    def process_number(self, current):
        """ทำงานได้ก็พอแล้ว"""
        if self.previous_num is None:
            self.group = current
        elif int(current) - int(self.previous_num) == 1:
            if not self.continuity:
                self.group += "-"
                self.continuity = True
        else:
            if self.group.endswith("-"):
                self.group += self.previous_num
            if self.group:
                self.group += ", "
            self.group += current
            self.continuity = False
        self.previous_num = current

    def shorten(self):
        """สั้นสุดๆๆ"""
        first_num = self.get_input()
        if first_num == "-1":
            print("")
            return

        self.process_number(first_num)

        while True:
            num = self.get_input()
            if num == "-1":
                break
            self.process_number(num)

        if self.group.endswith("-"):
            self.group += self.previous_num
        print(self.group)

def main():
    """มี main ไว้ทำเท่"""
    grouper = NumberGrouper()
    grouper.shorten()

if __name__ == "__main__":
    main()
