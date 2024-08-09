def string(str):
    return max(str, key=len)
print(string(["gio", "nika", "lazare"]))