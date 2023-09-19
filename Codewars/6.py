def generate_hashtag(s: str) -> str:
    if len(('').join(s.split(' '))) > 148 or s == "":
        return False
    splitted = s.split(' ')
    for i in range(len(splitted)):
        splitted[i] = splitted[i].capitalize()
    return f"#{(''.join(splitted))}"

print(generate_hashtag('Codewars      '))
print(generate_hashtag('g LYeNhIsbF DOaexflBCAi ywkICiWCVCi DuoBQljSuhr RLLBkkieXWV Hvc golBq   QdpCoADn TR noSNglrpvwX EEEzUCLXeBm XeeBppDDJZK Ubbxn Sqnlw maAPQsrbeHk sjKDxnaNDhz acb NxbJCPD'))
