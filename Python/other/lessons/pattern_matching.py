def parse_names(value: str | tuple | list | dict) -> str:
    match value:
        case surname, name, second_name:
            pass
        case {'surname': surname, 'name': name, 'second_name': second_name} if len(value) == 3:
            pass
        case str() if len(value.split()) == 3:
            surname, name, second_name = value.split()
            return f'surname {surname}, name {name}, second_name {second_name}'
        case _:
            return "Error"

    return f'surname {surname}, name {name}, second_name {second_name}'


if __name__ == '__main__':
    assert parse_names(('Іванько', 'Іван', 'Іванович')) == 'surname Іванько, name Іван, second_name Іванович'
    assert parse_names(['Іванько', 'Іван', 'Іванович']) == 'surname Іванько, name Іван, second_name Іванович'
    assert parse_names({'surname': "Іванько",
                        'name': "Іван",
                        'second_name': "Іванович"}) == 'surname Іванько, name Іван, second_name Іванович'
    assert parse_names("Іванько Іван Іванович") == 'surname Іванько, name Іван, second_name Іванович'

    assert parse_names(('Іванько', 'Іван')) == "Error"
    assert parse_names(['Іванько', 'Іван']) == "Error"
    assert parse_names({'surname': "Іванько", 'name': "Іван"}) == "Error"
    assert parse_names("Іванько Іван") == "Error"
    assert parse_names("Іванько Іван Іванько Іван") == "Error"

