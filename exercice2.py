#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values=[]
        print("faire entrer 10 valeur :")
        while len(values)<10 :
            values.append(input("donner une valeur "))

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words=[]
        print("donner 2 mots pour voir si ils sont des anagrammes")
        words.append(input("donner un mots "))
        words.append(input("donner un autre mots"))
        if sorted(words[0])==sorted(words[1]) :
            return True
        else:return False


def contains_doubles(items: list) -> bool:
    ensemble =set(list)
    return len(ensemble)!=len(list)



def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    liste_1 = list(student_grades.keys())
    liste_2 = list(student_grades.values())
    note = []
    for i in liste_2:
        note.append(sum(i) / len(i))
    index_max = note.index(max(note))

    return {liste_1[index_max] : max(note)}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = {}
    for letter in sentence:
        frequency[letter] = sentence.count(letter)

    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)
    for keys in sorted_keys:
        if frequency[keys] >5:
            print(f"le caractere '{keys}' est repeter {frequency[keys]} fois ")

    return frequency


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name=input("donner le nom de la recette :\n")
    ingredients=input("donner les ingredients de la recette separer par une , ").split(",")
    return {name : ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("donner le nom d'une recette :\n")
    if name in ingredients :
        print(ingredients[name])
    else:
        print("la recette demander n'existe pas ")
        print(f"les recettes existantes sont :{list(ingredients.keys())}")
        print_recipe(ingredients)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
