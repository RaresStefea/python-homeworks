from __future__ import annotations


def eliminate_dupes(lista: list) -> list:
    return list(set(lista))


def oldest_person(lista: list[tuple[str, int]]) -> str:
    max_age = 0
    name = "Nothing!"
    for name_t, age_t in lista:
        if age_t > max_age:
            max_age = age_t
            name = name_t
    return name


def freq(tuplu: tuple[int]) -> int:
    max_freq = 0
    max_value = 0
    for i in tuplu:
        if tuplu.count(i) > max_freq:
            max_freq = tuplu.count(i)
            max_value = i
    return max_value


def text_appear(text: str) -> None:
    lista = text.split()
    max_occur = 0
    max_word = "Nothing!"
    for i in lista:
        if lista.count(i) > max_occur:
            max_occur = lista.count(i)
            max_word = i
    print("Max word is {0}, appearing {1} times".format(max_word, max_occur))


def switch_dict(dicti: dict) -> dict:
    newdicti = {}
    for name, age in dicti.items():
        newdicti[age] = name
    return newdicti


def first_elem(elem: tuple) -> int:
    return elem[0]


def merger(list1: list[tuple], list2: list[tuple]) -> list[tuple]:
    new_list = list1 + list2
    new_list.sort(key=first_elem)
    return new_list


def dicti_ops(people: dict[dict[str, int | str, str]]) -> tuple[str, int]:
    oldest_person_name = "Nothing!"
    oldest_person_age = 0

    for name, info in people.items():
        if info.get("age") > oldest_person_age:
            oldest_person_age = info.get("age")
            oldest_person_name = name
        if info.get("city") == "New York":
            print(name)

    return oldest_person_name, oldest_person_age
