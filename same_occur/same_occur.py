
def same_occur(string):
    chars_count = dict()

    for i in range(len(string)):
        chars_count[string[i]] = (chars_count.get(string[i]) or 0) + 1

    first_count = chars_count[string[0]]
    used = False

    for key in chars_count:
        if first_count != chars_count[key]:
            if used:
                return "NO"
            else:
                if (first_count + 1) == chars_count[key] or (first_count - 1) == chars_count[key] or chars_count[key] == 1 or first_count == 1:
                    used = True
                else:
                    return "NO"

    return "YES"


