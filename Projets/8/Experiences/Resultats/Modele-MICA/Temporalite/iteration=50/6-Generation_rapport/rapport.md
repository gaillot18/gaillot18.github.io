**Analyse de sensibilité**  

Nom de l'utilisateur : Jean-Baptiste Gaillot  
Date : 2026-07-25  
Commentaire : /  

# Paramètres

## Backends

| Backend | Type du backend | Paramètre du backend | Activation | Précision du backend |
| --- | --- | --- | --- | --- |
| `ieee` | Déterministe | `precision_numpy` | Oui | `[16, 32, 64]` |
| `mca` | Stochastique | `precision_binary64` | Non | / |
| `bitmask` | Stochastique | `precision_binary64` | Non | / |
| `vprec` | Déterministe | `precision_binary64` | Non | / |
| `cancellation` | Stochastique | `tolerance` | Non | / |


La référence est : `backend = ieee` et `precision_numpy = 64`.

## Fonctions

### Noms des fonctions

`mica`



### Information sur les variables d'entrée

| Nom de l'entrée compacte | Type du tenseur | Ordre du tenseur | Dimension du tenseur | Domaine |
| --- | --- | --- | --- | --- |
| `hauteur_eau_entree` | Matrice | `2` | `[15, 15]` | `[0.0, 0.01]` |


### Information sur les variables de sortie

| Nom de la sortie compacte | Type du tenseur | Ordre du tenseur | Dimensions du tenseur |
| --- | --- | --- | --- |
| `hauteur_eau_sortie` | Matrice | `2` | `[15, 15]` |
| `vitesse_manning_sortie` | Matrice | `2` | `[15, 15]` |


## Valeurs d'entrées et pseudo-aléatoire

### Type de génération des valeurs d'entrée
Générateur = `sobol`.  



### Reproductibilité des résultats

Graine du générateur = `1`.

### Ensembles de valeurs d'entrée

Nombre d'ensembles de valeurs d'entrée approximatif = `800`.  
Nombre d'ensembles de valeurs d'entrée = `904`.

| `hauteur_eau_entree_0_0` | `hauteur_eau_entree_0_1` | `hauteur_eau_entree_0_2` | `hauteur_eau_entree_0_3` | `hauteur_eau_entree_0_4` | `hauteur_eau_entree_0_5` | `hauteur_eau_entree_0_6` | `hauteur_eau_entree_0_7` | `hauteur_eau_entree_0_8` | `hauteur_eau_entree_0_9` | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.008836614908650517` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.006159772276878357` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.0047040082886815075` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024027036875486373` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.002732319151982665` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.006660487065091729` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006940273065119982` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.007181999608874321` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.003932493655011058` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.0018486454524099826` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| `0.0015546531789004804` | `0.00588747326284647` | `0.006075321752578021` | `0.0024239998962730168` | `0.008456894652917981` | `0.002625605845823884` | `0.006753896083682776` | `0.0037666341289877892` | `0.007314463797956705` | `0.004909837087616324` | 215 autres... |
| 884 autres... | 884 autres... | 884 autres... | 884 autres... | 884 autres... | 884 autres... | 884 autres... | 884 autres... | 884 autres... | 884 autres... | ... |


Le nombre de noms d'entrées non compactes est > 10 : on affiche seulement les 10 premières colonnes.

Le nombre d'ensembles de valeurs d'entrées non compactes est > 20 : on affiche seulement les 20 premières lignes.

### Nombre d'exécutions
Nombre d'exécutions pour les backends déterministes = `1`.  
Nombre d'exécutions pour les backends stochastiques = `1`.




# Résultats

## Analyse du domaine


<img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_domaine/1.png" style="width:600px; height:auto;">

## Analyse numérique

### Cartes d'intensité des erreurs en forme compacte

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Fonction →<br><br>↓ Backend | `mica` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=mica/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Fonction →<br><br>↓ Backend | `mica` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=mica/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Cartes d'intensité des erreurs en forme spatialisée et non compacte

#### Fonction = `mica`

##### Backend = `ieee`

###### Nom de la sortie non compacte = `hauteur_eau_sortie`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs absolues | médiane<br>des erreurs absolues | minimum<br>des erreurs absolues | maximum<br>des erreurs absolues | coefficient de variation<br>des erreurs absolues |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=hauteur_eau_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

</div>



###### Nom de la sortie non compacte = `vitesse_manning_sortie`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs absolues | médiane<br>des erreurs absolues | minimum<br>des erreurs absolues | maximum<br>des erreurs absolues | coefficient de variation<br>des erreurs absolues |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=mica/backend=ieee/sortie_nom_compact=vitesse_manning_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

</div>



### Enveloppes de quantiles du nombre de chiffres significatifs en forme non compacte

#### Fonction = `mica`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `hauteur_eau_sortie_7_7` | `vitesse_manning_sortie_7_7` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=mica/backend=ieee/sortie_nom=hauteur_eau_sortie_7_7/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=mica/backend=ieee/sortie_nom=vitesse_manning_sortie_7_7/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


## Analyse paramétrique
Pour cette analyse, les paramètres fixés sont : `backend = ieee` et `precision_numpy = 64`.

### Nuages de points du comportement

#### Fonction = `mica`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `hauteur_eau_sortie_7_7` | `vitesse_manning_sortie_7_7` |
| --- | --- | --- |
| `hauteur_eau_entree_7_7` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=mica/entree_nom=hauteur_eau_entree_7_7/sortie_nom=hauteur_eau_sortie_7_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=mica/entree_nom=hauteur_eau_entree_7_7/sortie_nom=vitesse_manning_sortie_7_7.png" style="width:400px; height:auto;"> |



