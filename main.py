names = ["alfred", "tabitha", "william", "aria"]
def capital_letter(name: str) -> str:
    return name.capitalize()

print(list(map(capital_letter, names)))