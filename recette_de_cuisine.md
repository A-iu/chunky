# Recette de cuisine
## Étape 0 : on bosse Unix for poets
https://www.cs.upc.edu/~padro/Unixforpoets.pdf

## Étape 1 : on a viré les maj de début de phrase
- à la main !
texte_base.txt => texte_sans_maj

## Étape 2 : on fait la liste des chunks (pas trop en fait)
- on vire les virgules, les guillemets, les points
tr -d ',".“”!:'  < texte_sans_maj.txt > texte_sans_ponctuation

- on ajoute un espace après le d', l' etc. (puisqu'autorisé dans le lexique)
sed 's/’/’ /g' texte_sans_ponctuation > texte_avec_espace_apostrophe

- on ajoute un espace avant et après -t- (puisqu'autorisé dans le lexique)
sed 's/-t-/ -t- /g' texte_avec_espace_apostrophe > texte_avec_espace_t_euphonique

- on remplace les espaces par des lignes
tr ' ' '\n' < texte_avec_espace_t_euphonique > liste_tokens

- on trie et on vire les doublons
sort -u liste_tokens > liste_triee