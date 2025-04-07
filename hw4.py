def rep_char(c, n):
    return c * n

def draw_welcome_box(name):
    msg1 = f"Hello {name}."
    msg2 = "Welcome to Seoul."

    nstr = max(len(msg1), len(msg2))
    line = rep_char('-', nstr)

    print(line)
    print(msg1)
    print(msg2)
    print(line)

def main():
    name = input("Input his/her name: ")
    draw_welcome_box(name)

if __name__ == "__main__":
    main()
