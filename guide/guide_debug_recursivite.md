
# **Guide d'exercice pour analyser la récursivité dans PyCharm**

## Fibonacci simple

Commençons par nous intéresser à la fonction fibonacci simple, sans mémoïsation (``use_memo = False``)

### **1\. Analyser la Pile d'Appels (Call Stack) 🥞**

La pile d'appels montre l'empilement des fonctions en attente de résolution.

> * **Action :** Placez un point d'arrêt à la ligne ``if n <= 0:``. Lancez le débogueur.  
> * **Observation :** Regardez l'onglet **Frames** tout à gauche de la fenêtre de debug.  
> * **Navigation :** Au début, vous ne verrez qu'un appel. Cliquez sur le bouton **Resume Program** (Flèche verte ⏯️) plusieurs fois. Vous allez voir la pile se remplir : fibonacci:15, demo\_recursivite, fibonacci:21, demo\_recursivite, etc.  
> * **Le truc en plus :** Cliquez sur les différentes lignes de cet onglet **Frames**. PyCharm vous fait voyager dans le temps en vous montrant la valeur exacte de n pour *cet appel spécifique* de la fonction.

### **2\. Suivre le compteur avec les Watchers 👓**

> * **Action :** Pendant que le programme est en pause, ajoutez la variable globale compteur\_appels dans vos **Watches** (comme vu précédemment).  
> * **Observation :** À chaque fois que vous appuyez sur **F9** (Resume) pour aller au prochain point d'arrêt, vous verrez le compteur grimper. Pour valeur\_cible \= 4, vous constaterez que la fonction est appelée **9 fois** au total pour un résultat final de 3\. C'est une excellente démonstration visuelle de l'inefficacité de la récursivité brute \!

### **3\. Utiliser le "Step Out" (Shift \+ F8) ↩️**

Quand on est perdu au fond de 5 niveaux de récursivité, on veut souvent remonter d'un cran.

> * **Action :** Une fois arrêté au cœur d'un appel (par exemple quand n \= 1), cliquez sur l'icône de la flèche qui monte **Step Out** (Shift \+ F8).  
> * **Observation :** PyCharm exécute immédiatement le reste de la fonction actuelle et s'arrête pile au moment où il revient à la fonction parente (à la ligne 21).

## Fibonacci avec mémoïsation

La mémoïsation consiste à utiliser un dictionnaire pour stocker les résultats des calculs déjà effectués. Ainsi, si la fonction est appelée une deuxième fois avec le même paramètre, elle renvoie directement le résultat stocké au lieu de relancer des appels récursifs.

### **Étape A : Suivre le dictionnaire en temps réel**

> 1. Placez un point d'arrêt à la ligne 14 ``if n in memoire:``  
> 2. Lancez le script en mode **Debug**.  
> 3. Dans l'onglet **Variables** (en bas), faites un clic droit sur la variable memoire et choisissez **Add to Watches**.

### **Étape B : Observer l'interception du doublon (Le moment magique)**

> 1. Appuyez sur **F9 (Resume Program)** pour faire défiler les premiers appels.  
> 2. Regardez votre Watcher memoire se remplir progressivement (il va stocker 1: 1, puis 2: 1, puis 3: 2).  
> 3. Au **5ème appel**, le programme s'arrête et vous affiche **n \= 2**.  
> 4. Regardez vos Watchers :  
   * memoire contient déjà la clé {2: 1}.  
   * compteur\_appels vaut 5\.  
> 5. Appuyez sur **F8 (Step Over)** pour avancer d'une ligne. Vous constatez que le débogueur entre directement dans le bloc if et exécute return memoire\[n\].

**Le gain est visible immédiatement :** La fonction ne va pas recalculer fibonacci(1) et fibonacci(0) pour ce n=2. Elle coupe court à la récursivité. Le programme se termine juste après, totalisant **5 appels au lieu de 9**.

Dernière astuce : Les points d'arrêt de ligne vs. de retour**

Dans un code récursif, il est parfois difficile de savoir quelle valeur une fonction renvoie réellement à sa fonction parente.

> * Lorsque vous êtes arrêté sur la ligne return resultat (ligne 26), regardez l'onglet **Variables**.  
> * PyCharm ajoute automatiquement une ligne spéciale appelée **Return value** tout en haut de la liste. Elle vous montre la valeur exacte qui s'apprête à être renvoyée, vous évitant d'avoir à deviner le flux de retour de la récursivité.
