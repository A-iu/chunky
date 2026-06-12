# Recette de cuisine

## Étape 1 : on a viré les maj de début de phrase

## Étape 2 : on fait la liste des chunks
- on vire les virgules, les guillemets, les points
tr -d ',".“”!:'  < texte_sans_maj.txt > texte_sans_ponctuation

- on ajoute un espace après le d' 
sed 's/’/’ /g' texte_sans_ponctuation > texte_avec_espace_apostrophe

- on ajoute un espace après le d' 
sed 's/-t-/ -t- /g' texte_avec_espace_apostrophe > texte_avec_espace_t_euphonique

- on remplace les espaces par des lignes
tr ' ' '\n' < texte_avec_espace_t_euphonique > liste_tokens

- on trie et on vire les doublons
sort -u liste_tokens > liste_triee