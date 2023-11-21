def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = [x for x in result if x.lower() in 'aeouiy']
        return vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
