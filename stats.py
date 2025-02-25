from collections import Counter

def count_words(text) :
    split_text = text.split()
    return len(split_text)

def count_char(text) :
    count = Counter(text.lower())
    new_dict = {
        "a": count["a"],
        "b": count["b"],
        "c": count["c"],
        "d": count["d"],
        "e": count["e"],
        "f": count["f"],
        "g": count["g"],
        "h": count["h"],
        "i": count["i"],
        "j": count["j"],
        "k": count["k"],
        "l": count["l"],
        "m": count["m"],
        "n": count["n"],
        "o": count["o"],
        "p": count["p"],
        "q": count["q"],
        "r": count["r"],
        "s": count["s"],
        "t": count["t"],
        "u": count["u"],
        "v": count["v"],
        "w": count["w"],
        "x": count["x"],
        "y": count["y"],
        "z": count["z"],
    }
    return new_dict

def sort_dict(dict) :
    myKeys = list(dict.keys())
    myKeys.sort(reverse=False)
    sorted_dict = { i : dict[i] for i in myKeys}
    return sorted_dict