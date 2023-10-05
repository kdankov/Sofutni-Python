def concatenate(*args, **kwargs):
    res = ''

    for word in args:
        res += word

    for key, value in kwargs.items():
        if key in res:
            res = res.replace(key, value)

    return res


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))