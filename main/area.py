def calculatearea(a, b):
    print("__name__ ==", __name__)
    return a * b


if __name__ == "__main__":
    print("I'm in main")
    c = calculatearea(3, 4)
    print("area: ", c)
