formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# for each {} in the original string will be replaced by formatter itself,
# which is "{} {} {} {}". So there will be 16 {} in the string
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a wonbat",
    "or a song about China"
))
