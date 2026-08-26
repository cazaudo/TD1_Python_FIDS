compteur_appels = 0
# Dictionnaire servant de cache pour la mémoïsation
memoire = {}

def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci de façon récursive."""
    global compteur_appels
    compteur_appels += 1

    # Point d'arrêt idéal 1 : Observer l'évolution de 'n' et de la pile d'appels
    print(f"Appel n°{compteur_appels} avec n = {n}")

    # Cas de base
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Cas récursif (Génère deux nouveaux appels)
    # Point d'arrêt idéal 2 : Suivre le retour des fonctions
    resultat = fibonacci(n - 1) + fibonacci(n - 2)

    return resultat

def fibonacci_memo(n):
    """Calcule le n-ième nombre de Fibonacci de façon optimisée."""
    global compteur_appels
    compteur_appels += 1

    print(f"Appel n°{compteur_appels} avec n = {n}")

    # 1. Vérification du cache : Si le calcul existe déjà, on le renvoie
    if n in memoire:
        return memoire[n]

    # Cas de base
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Cas récursif
    resultat = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    # 2. Stockage dans le cache avant de retourner le résultat
    memoire[n] = resultat
    return resultat


if __name__ == "__main__":
    valeur_cible = 4
    print(f"--- Début du calcul optimisé de Fibonacci({valeur_cible}) ---")

    use_memo = False

    if use_memo:
        terme_final = fibonacci_memo(valeur_cible)
    else:
        terme_final = fibonacci(valeur_cible)

    print("\n--- Résultat ---")
    print(f"Fibonacci({valeur_cible}) = {terme_final}")
    print(f"Nombre total d'appels effectués : {compteur_appels}")
    print(f"Contenu final de la mémoire : {memoire}")
