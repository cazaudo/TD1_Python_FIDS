## **Guide d'exercice avec le Débogueur PyCharm**

Pour lancer le mode debug, faites un **clic droit dans le code** et choisissez **Debug 'code\_debug'** (ou cliquez sur l'icône de l'insecte vert en haut à droite).

## **1\. Les Points d'Arrêt (Breakpoints)**

> * **Action :** Cliquez dans la marge gauche à côté de la ligne ``reduction = calculer_remise(total_brut, code_actif)`` (ligne 41). Un point rouge apparaît.  
> * **Observation :** Relancez le débogueur (bouton **Rerun 'code_debug'**). Le programme s'arrête pile sur cette ligne. Le script est "gelé".

## **2\. L'inspection et les Points d'Arrêt Conditionnels**

> * **Action :** Faites un **clic droit sur le point rouge** de la ligne 26 (total \+= prix).  
> * **Condition :** Dans la case *Condition*, écrivez prix \< 20\. Relancez le débogueur.  
> * **Observation :** Le programme ignore l'ordinateur et la souris. Il s'arrête directement lorsque la boucle traite le "Tapis" (15€).

## **3\. Le Pas à Pas (Stepping)**

Une fois arrêté sur la ligne reduction \= calculer\_remise(...) :

> * **Step Into (F7) :** Cliquez sur la flèche qui pointe vers le bas. Vous "entrez" à l'intérieur de la fonction calculer\_remise.  
> * **Step Over (F8) :** Cliquez sur la flèche courbe. Vous avancez ligne par ligne sans entrer dans les sous-fonctions.

## **4\. Modifier une variable à la volée**

> * **Action :** Avancez (F8) jusqu'à la ligne 8 ``taux_remise = 0.0`` Installez-vous sur la ligne suivante.  
> * **Modification :** Dans l'onglet **Variables** en bas, faites un clic droit sur code\_promo, choisissez **Set Value...** et remplacez "VIP" par "BIENVENUE".  
> * **Observation :** Continuez l'exécution (F8). Le bloc if code\_promo \== "BIENVENUE": va s'exécuter à la place du bloc VIP. Vous avez modifié le comportement du code en direct.

## **5\. Evaluer des expressions**

Deux solutions sont possibles : 

> 1. Appuyez sur **Alt \+ F8** (ou **Option \+ F8** sur Mac). Une fenêtre contextuelle s'ouvre. Vous pouvez aussi faire un clic droit directement sur une variable dans votre code et choisir **Evaluate Expression...**.

> 2. Utiliser la console accessible depuis la console Python

A noter que que toutes les fonctions Python intégrées sont accessibles dans les deux cas.


## **6\. Découvrons enfin les **Watchers** (ou *Expressions à surveiller*), qui complètent parfaitement l'outil *Evaluate Expression*. Au lieu de taper manuellement un calcul à chaque pause, vous demandez à PyCharm de recalculer et d'afficher automatiquement vos expressions personnalisées à chaque ligne franchie.

Voici comment configurer et exploiter les Watchers avec notre script de démonstration.

## **1\. Ouvrir l'onglet "Watches"**

> 1. Assurez-vous que votre programme est en pause (par exemple, mettez un point d'arrêt à la ligne ``total \+= prix`` dans la boucle du panier).  
> 2. Regardez la fenêtre du débogueur en bas de PyCharm.  
> 3. À côté de l'onglet **Variables**, vous trouverez l'onglet **Watches** (représenté parfois par une icône de lunettes 👓).  
>    *(Si l'onglet n'est pas visible, cliquez sur la petite icône \+ ou le menu d'affichage de la zone des variables pour l'activer).*

## ---

**2\. Ajouter une expression à surveiller**

Il existe deux méthodes très simples pour ajouter un calcul :

## **Méthode 1 : Depuis l'onglet Watches**

> 1. Dans l'onglet **Watches**, cliquez sur le bouton **\+** (Add).  
> 2. Tapez la formule que vous voulez suivre. Par exemple : total \* 1.20 (pour voir le total TTC fictif avec 20% de TVA).  
> 3. Appuyez sur **Entrée**.

## **Méthode 2 : Depuis le code ou l'onglet Variables (Plus rapide)**

> 1. Dans l'onglet **Variables**, faites un clic droit sur la variable prix.  
> 2. Choisissez **Add to Watches**.  
> 3. PyCharm l'ajoute instantanément à votre liste de surveillance.

## ---

**3\. Exercice pratique : Suivre l'évolution dans la boucle**

Configurons des Watchers pertinents pour observer la création du panier d'Alice :

> 1. Ajoutez ces trois expressions dans vos **Watches** :  
   * article.upper() (pour voir le nom du produit en majuscules)  
   * total >= 1000 (un booléen qui passera à True dès que le panier dépassera 1000€)  
   * prix * 0.90 (pour simuler une réduction immédiate de 10% sur l'article en cours)  
> 2. Appuyez maintenant sur **F8** (Step Over) à plusieurs reprises pour avancer pas à pas dans la boucle for.

## **Ce que vous allez observer :**

À chaque fois que le débogueur passe à la ligne suivante, la valeur de vos expressions change en direct sous vos yeux dans l'onglet **Watches** :

> * Au premier tour (Ordinateur), total \>= 1000 affiche True.  
> * Au deuxième tour (Souris), article.upper() passe instantanément de "ORDINATEUR" à "SOURIS".

A noter enfin que si vous venez de tester un calcul complexe dans la fenêtre **Evaluate Expression** (Alt+F8) et que le résultat est intéressant, vous n'avez pas besoin de le retaper. Cliquez simplement sur le bouton **Add to Watches** présent directement en bas à droite de cette fenêtre pour l'envoyer dans votre liste de surveillance permanente.
