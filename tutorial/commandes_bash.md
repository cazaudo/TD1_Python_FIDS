Voici un mini-tutoriel pour maîtriser les commandes **find**, **wc** et **awk**.

## ---

**🔍 La commande find (Trouver des fichiers)**

Elle sert à chercher des fichiers ou dossiers selon des critères précis (nom, taille, date).

> * **Chercher par nom dans le dossier courant :**  
>   find . \-name "rapport.txt"  
> * **Chercher sans distinction de majuscules :**  
>   find . \-iname "\*.md"  
> * **Trouver uniquement les dossiers :**  
>   find /chemin \-type d  
> * **Trouver les fichiers de plus de 100 Mo :**  
>   find . \-type f \-size \+100M

## ---

**🔢 La commande wc (Compter les éléments)**

Elle permet de compter les lignes, les mots et les octets d'un fichier ou d'un flux textuel.

> * **Compter le nombre de lignes :**  
>   wc \-l fichier.txt  
> * **Compter le nombre de mots :**  
>   wc \-w fichier.txt  
> * **Compter les caractères :**  
>   wc \-m fichier.txt

## ---

**✂️ La commande awk (Extraire et traiter des données)**

Elle analyse les fichiers texte ligne par ligne, découpés en colonnes (séparées par défaut par des espaces). $1 est la première colonne, $2 la deuxième, etc.

> * **Afficher la première colonne d'un fichier :**  
>   awk '{print $1}' données.txt  
> * **Filtrer selon une condition (ex: afficher si la colonne 3 dépasse 50\) :**  
>   awk '$3 \> 50 {print $1}' notes.txt

## ---

**🚀 Combinaisons puissantes (Pipelines)**

Le vrai pouvoir de Bash réside dans l'association de ces commandes avec le symbole | (pipe).

> * **Compter le nombre total de fichiers PHP dans un projet :**  
>   find . \-type f \-name "\*.php" | wc \-l  
> * **Trouver les gros fichiers et n'afficher que leur nom et taille :**  
>   ls \-lh | awk '$5 \~ /M/ {print "Fichier lourd : " $9 " (" $5 ")"}'

> 
