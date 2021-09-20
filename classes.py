class mobile:
    def __init__(self, brandname, color, IsJack):
        self.brandname = brandname
        self.color = color
        self.IsJeck = IsJack

    def calling(self):
        print("calling")

    def pictureClick(self):
        print("picture clicked")

    def message(self):
        print("message sent")


def main():
    m1 = mobile("Realme", "blue", True)
    print(m1.brandname)
    print(m1.color)
    print(m1.IsJeck)
    m1.calling()
    m1.pictureClick()
    m1.message()
    print("------------------------")
    m2 = mobile("Apple", "White", False)
    print(m2.brandname)
    print(m2.color)
    print(m2.IsJeck)
    m2.calling()
    m2.pictureClick()
    m2.message()


if __name__ == "__main__":
    main()
