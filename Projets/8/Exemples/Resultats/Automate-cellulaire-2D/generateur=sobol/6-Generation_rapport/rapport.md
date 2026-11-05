**Analyse de sensibilité**  

Nom de l'utilisateur : Jean-Baptiste Gaillot  
Date : 2026-07-25  
Commentaire : /  

# Paramètres

## Backends

| Backend | Type du backend | Paramètre du backend | Activation | Précision du backend |
| --- | --- | --- | --- | --- |
| `ieee` | Déterministe | `precision_numpy` | Oui | `[16, 32, 64]` |
| `mca` | Stochastique | `precision_binary64` | Oui | `[10, 23, 52]` |
| `bitmask` | Stochastique | `precision_binary64` | Oui | `[10, 23, 52]` |
| `vprec` | Déterministe | `precision_binary64` | Non | / |
| `cancellation` | Stochastique | `tolerance` | Non | / |


La référence est : `backend = ieee` et `precision_numpy = 64`.

## Fonctions

### Noms des fonctions

`automate_cellulaire_2d_1`

`automate_cellulaire_2d_2`



### Information sur les variables d'entrée

| Nom de l'entrée compacte | Type du tenseur | Ordre du tenseur | Dimension du tenseur | Domaine |
| --- | --- | --- | --- | --- |
| `M_entree` | Matrice | `2` | `[3, 3]` | `[0.0, 1.0]` |


### Information sur les variables de sortie

| Nom de la sortie compacte | Type du tenseur | Ordre du tenseur | Dimensions du tenseur |
| --- | --- | --- | --- |
| `M_sortie` | Matrice | `2` | `[3, 3]` |


## Valeurs d'entrées et pseudo-aléatoire

### Type de génération des valeurs d'entrée
Générateur = `sobol`.  



### Reproductibilité des résultats

Graine du générateur = `1`.

### Ensembles de valeurs d'entrée

Nombre d'ensembles de valeurs d'entrée approximatif = `4000`.  
Nombre d'ensembles de valeurs d'entrée = `5120`.

| `M_entree_0_0` | `M_entree_0_1` | `M_entree_0_2` | `M_entree_1_0` | `M_entree_1_1` | `M_entree_1_2` | `M_entree_2_0` | `M_entree_2_1` | `M_entree_2_2` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `0.15546531789004803` | `0.588747326284647` | `0.607532175257802` | `0.2423999896273017` | `0.8456894652917981` | `0.2625605845823884` | `0.6753896083682775` | `0.3766634128987789` | `0.7314463797956705` |
| `0.49098370876163244` | `0.588747326284647` | `0.607532175257802` | `0.2423999896273017` | `0.8456894652917981` | `0.2625605845823884` | `0.6753896083682775` | `0.3766634128987789` | `0.7314463797956705` |
| `0.15546531789004803` | `0.9820169974118471` | `0.607532175257802` | `0.2423999896273017` | `0.8456894652917981` | `0.2625605845823884` | `0.6753896083682775` | `0.3766634128987789` | `0.7314463797956705` |
| `0.15546531789004803` | `0.588747326284647` | `0.4405437568202615` | `0.2423999896273017` | `0.8456894652917981` | `0.2625605845823884` | `0.6753896083682775` | `0.3766634128987789` | `0.7314463797956705` |
| `0.15546531789004803` | `0.588747326284647` | `0.607532175257802` | `0.20179095026105642` | `0.8456894652917981` | `0.2625605845823884` | `0.6753896083682775` | `0.3766634128987789` | `0.7314463797956705` |
| `0.15546531789004803` | `0.588747326284647` | `0.607532175257802` | `0.2423999896273017` | `0.3854847699403763` | `0.2625605845823884` | `0.6753896083682775` | `0.3766634128987789` | `0.7314463797956705` |
| `0.15546531789004803` | `0.588747326284647` | `0.607532175257802` | `0.2423999896273017` | `0.8456894652917981` | `0.46254704613238573` | `0.6753896083682775` | `0.3766634128987789` | `0.7314463797956705` |
| `0.15546531789004803` | `0.588747326284647` | `0.607532175257802` | `0.2423999896273017` | `0.8456894652917981` | `0.2625605845823884` | `0.4323244160041213` | `0.3766634128987789` | `0.7314463797956705` |
| `0.15546531789004803` | `0.588747326284647` | `0.607532175257802` | `0.2423999896273017` | `0.8456894652917981` | `0.2625605845823884` | `0.6753896083682775` | `0.19038886204361916` | `0.7314463797956705` |
| `0.15546531789004803` | `0.588747326284647` | `0.607532175257802` | `0.2423999896273017` | `0.8456894652917981` | `0.2625605845823884` | `0.6753896083682775` | `0.3766634128987789` | `0.4861564636230469` |
| `0.15546531789004803` | `0.9820169974118471` | `0.4405437568202615` | `0.20179095026105642` | `0.3854847699403763` | `0.46254704613238573` | `0.4323244160041213` | `0.19038886204361916` | `0.4861564636230469` |
| `0.49098370876163244` | `0.588747326284647` | `0.4405437568202615` | `0.20179095026105642` | `0.3854847699403763` | `0.46254704613238573` | `0.4323244160041213` | `0.19038886204361916` | `0.4861564636230469` |
| `0.49098370876163244` | `0.9820169974118471` | `0.607532175257802` | `0.20179095026105642` | `0.3854847699403763` | `0.46254704613238573` | `0.4323244160041213` | `0.19038886204361916` | `0.4861564636230469` |
| `0.49098370876163244` | `0.9820169974118471` | `0.4405437568202615` | `0.2423999896273017` | `0.3854847699403763` | `0.46254704613238573` | `0.4323244160041213` | `0.19038886204361916` | `0.4861564636230469` |
| `0.49098370876163244` | `0.9820169974118471` | `0.4405437568202615` | `0.20179095026105642` | `0.8456894652917981` | `0.46254704613238573` | `0.4323244160041213` | `0.19038886204361916` | `0.4861564636230469` |
| `0.49098370876163244` | `0.9820169974118471` | `0.4405437568202615` | `0.20179095026105642` | `0.3854847699403763` | `0.2625605845823884` | `0.4323244160041213` | `0.19038886204361916` | `0.4861564636230469` |
| `0.49098370876163244` | `0.9820169974118471` | `0.4405437568202615` | `0.20179095026105642` | `0.3854847699403763` | `0.46254704613238573` | `0.6753896083682775` | `0.19038886204361916` | `0.4861564636230469` |
| `0.49098370876163244` | `0.9820169974118471` | `0.4405437568202615` | `0.20179095026105642` | `0.3854847699403763` | `0.46254704613238573` | `0.4323244160041213` | `0.3766634128987789` | `0.4861564636230469` |
| `0.49098370876163244` | `0.9820169974118471` | `0.4405437568202615` | `0.20179095026105642` | `0.3854847699403763` | `0.46254704613238573` | `0.4323244160041213` | `0.19038886204361916` | `0.7314463797956705` |
| `0.49098370876163244` | `0.9820169974118471` | `0.4405437568202615` | `0.20179095026105642` | `0.3854847699403763` | `0.46254704613238573` | `0.4323244160041213` | `0.19038886204361916` | `0.4861564636230469` |
| 5100 autres... | 5100 autres... | 5100 autres... | 5100 autres... | 5100 autres... | 5100 autres... | 5100 autres... | 5100 autres... | 5100 autres... |


Le nombre d'ensembles de valeurs d'entrées non compactes est > 20 : on affiche seulement les 20 premières lignes.

### Nombre d'exécutions
Nombre d'exécutions pour les backends déterministes = `1`.  
Nombre d'exécutions pour les backends stochastiques = `100`.




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

| Fonction →<br><br>↓ Backend | `automate_cellulaire_2d_1` | `automate_cellulaire_2d_2` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_1/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_2/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_1/backend=mca/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_2/backend=mca/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Fonction →<br><br>↓ Backend | `automate_cellulaire_2d_1` | `automate_cellulaire_2d_2` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_1/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_2/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_1/backend=mca/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_2/backend=mca/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Cartes d'intensité des erreurs en forme spatialisée et non compacte

#### Fonction = `automate_cellulaire_2d_1`

##### Backend = `ieee`

###### Nom de la sortie non compacte = `M_sortie`

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
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

</div>



##### Backend = `mca`

###### Nom de la sortie non compacte = `M_sortie`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs absolues | médiane<br>des erreurs absolues | minimum<br>des erreurs absolues | maximum<br>des erreurs absolues | coefficient de variation<br>des erreurs absolues |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



##### Backend = `bitmask`

###### Nom de la sortie non compacte = `M_sortie`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs absolues | médiane<br>des erreurs absolues | minimum<br>des erreurs absolues | maximum<br>des erreurs absolues | coefficient de variation<br>des erreurs absolues |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `automate_cellulaire_2d_2`

##### Backend = `ieee`

###### Nom de la sortie non compacte = `M_sortie`

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
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom_compact=M_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

</div>



##### Backend = `mca`

###### Nom de la sortie non compacte = `M_sortie`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs absolues | médiane<br>des erreurs absolues | minimum<br>des erreurs absolues | maximum<br>des erreurs absolues | coefficient de variation<br>des erreurs absolues |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



##### Backend = `bitmask`

###### Nom de la sortie non compacte = `M_sortie`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs absolues | médiane<br>des erreurs absolues | minimum<br>des erreurs absolues | maximum<br>des erreurs absolues | coefficient de variation<br>des erreurs absolues |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_binary64` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `10` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=10/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `23` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=23/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `52` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom_compact=M_sortie/precision_binary64=52/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Cartes d'intensité des erreurs en forme discretisée et non compacte

#### Fonction = `automate_cellulaire_2d_1`

##### Backend = `ieee`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



##### Backend = `mca`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



##### Backend = `bitmask`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `automate_cellulaire_2d_2`

##### Backend = `ieee`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



##### Backend = `mca`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



##### Backend = `bitmask`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Barres des erreurs en forme non compacte

#### Fonction = `automate_cellulaire_2d_1`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `automate_cellulaire_2d_2`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_0_0/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_1_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_2_2/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_0_0/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_1_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_2_2/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Enveloppes de quantiles du nombre de chiffres significatifs en forme non compacte

#### Fonction = `automate_cellulaire_2d_1`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_0_0/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_1_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=ieee/sortie_nom=M_sortie_2_2/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_0_0/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_1_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=mca/sortie_nom=M_sortie_2_2/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_0_0/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_1_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_1/backend=bitmask/sortie_nom=M_sortie_2_2/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


#### Fonction = `automate_cellulaire_2d_2`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_0_0/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_1_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=ieee/sortie_nom=M_sortie_2_2/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_0_0/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_1_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=mca/sortie_nom=M_sortie_2_2/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_0_0/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_1_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=automate_cellulaire_2d_2/backend=bitmask/sortie_nom=M_sortie_2_2/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


## Analyse paramétrique
Pour cette analyse, les paramètres fixés sont : `backend = ieee` et `precision_numpy = 64`.

### Nuages de points du comportement

#### Fonction = `automate_cellulaire_2d_1`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_1/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |


#### Fonction = `automate_cellulaire_2d_2`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree_0_0` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_0_0/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_0_0/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_0_0/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |
| `M_entree_1_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_1_1/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_1_1/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_1_1/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |
| `M_entree_2_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_2_2/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_2_2/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=automate_cellulaire_2d_2/entree_nom=M_entree_2_2/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |


### Matrices de similitude

| Nom de la sortie non compacte →<br><br>↓ Type de graphique | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| Moyenne des similitudes absolues | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=M_sortie_0_0/type_graphique=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=M_sortie_1_1/type_graphique=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=M_sortie_2_2/type_graphique=erreur_absolue.png" style="width:400px; height:auto;"> |
| Moyenne des similitudes relatives | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=M_sortie_0_0/type_graphique=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=M_sortie_1_1/type_graphique=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=M_sortie_2_2/type_graphique=erreur_relative.png" style="width:400px; height:auto;"> |


### Matrices de Sobol

| Nom de la sortie non compacte →<br><br>↓ Fonction | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `automate_cellulaire_2d_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=automate_cellulaire_2d_1/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=automate_cellulaire_2d_1/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=automate_cellulaire_2d_1/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |
| `automate_cellulaire_2d_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=automate_cellulaire_2d_2/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=automate_cellulaire_2d_2/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=automate_cellulaire_2d_2/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |


### Barres de Sobol

| Nom de la sortie non compacte →<br><br>↓ Fonction | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `automate_cellulaire_2d_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=automate_cellulaire_2d_1/sortie_nom=M_sortie_0_0.png" style="width:800px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=automate_cellulaire_2d_1/sortie_nom=M_sortie_1_1.png" style="width:800px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=automate_cellulaire_2d_1/sortie_nom=M_sortie_2_2.png" style="width:800px; height:auto;"> |
| `automate_cellulaire_2d_2` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=automate_cellulaire_2d_2/sortie_nom=M_sortie_0_0.png" style="width:800px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=automate_cellulaire_2d_2/sortie_nom=M_sortie_1_1.png" style="width:800px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=automate_cellulaire_2d_2/sortie_nom=M_sortie_2_2.png" style="width:800px; height:auto;"> |


### Indices de Sobol en forme spatialisée

#### Fonction = `automate_cellulaire_2d_1`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_sobol_spatial/fonction=automate_cellulaire_2d_1/entree_nom_compact=M_entree/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_sobol_spatial/fonction=automate_cellulaire_2d_1/entree_nom_compact=M_entree/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_sobol_spatial/fonction=automate_cellulaire_2d_1/entree_nom_compact=M_entree/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |


#### Fonction = `automate_cellulaire_2d_2`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée compacte | `M_sortie_0_0` | `M_sortie_1_1` | `M_sortie_2_2` |
| --- | --- | --- | --- |
| `M_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_sobol_spatial/fonction=automate_cellulaire_2d_2/entree_nom_compact=M_entree/sortie_nom=M_sortie_0_0.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_sobol_spatial/fonction=automate_cellulaire_2d_2/entree_nom_compact=M_entree/sortie_nom=M_sortie_1_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_sobol_spatial/fonction=automate_cellulaire_2d_2/entree_nom_compact=M_entree/sortie_nom=M_sortie_2_2.png" style="width:400px; height:auto;"> |



