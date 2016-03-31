def without(str, index):
    return str[:index] + str[index+1:]

def permutations(str):
    perms = []

    def permutations_helper(str, so_far=""):
        if len(str) == 0:
            perms.append(so_far)

        for i,letter in enumerate(str):
            permutations_helper( without(str,i), so_far + letter )

    permutations_helper(str)

    return perms

def test(str):
    perms = permutations(str)
    print("'{}' has {} perms: {}".format(str, len(perms), perms))

if __name__ == '__main__':
    test("")
    test("a")
    test("ab")
    test("abc")
    test("abcd")