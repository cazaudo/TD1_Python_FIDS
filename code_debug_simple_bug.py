import time

def calculer_remise(total_panier, code_promo):
    """Calcule la remise basée sur un code promo."""
    print(f"--- Application du code : {code_promo} ---")

    taux_remise = 0.0

    if code_promo == "BIENVENUE":
        taux_remise = 0.10
    elif code_promo == "VIP":
        taux_remise = 0.20

    montant_remise = total_panier + taux_remise

    return montant_remise

def traiter_panier(utilisateur, articles):
    """Calcule le total d'un panier pour un utilisateur."""
    print(f"Traitement du panier de {utilisateur}...")
    total = 0

    for article, prix in articles.items():
        total += prix

    return total

if __name__ == "__main__":
    Client = "Alice"
    achats = {"Ordinateur": 1200, "Souris": 50, "Tapis": 15}
    code_actif = "VIP"

    # 1. Calcul du total
    total_brut = traiter_panier(Client, achats)

    # 2. Calcul de la réduction
    reduction = calculer_remise(total_brut, code_actif)

    # 3. Résultat final
    total_final = total_brut - reduction
    print(f"\nTicket final pour {Client} :")
    print(f"- Total brut : {total_brut}€")
    print(f"- Remise : {reduction}€")
    print(f"- À payer : {total_final}€")
