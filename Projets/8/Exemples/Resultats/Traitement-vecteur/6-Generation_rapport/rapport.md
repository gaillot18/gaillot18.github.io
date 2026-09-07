**Analyse de sensibilité**  

Nom de l'utilisateur : Jean-Baptiste Gaillot  
Date : 2026-07-26  
Commentaire : /  

# Paramètres

## Backends

| Backend | Type du backend | Paramètre du backend | Activation | Précision du backend |
| --- | --- | --- | --- | --- |
| `ieee` | Déterministe | `precision_numpy` | Oui | `[16, 32, 64]` |
| `mca` | Stochastique | `precision_binary64` | Oui | `[10, 23, 32]` |
| `bitmask` | Stochastique | `precision_binary64` | Oui | `[10, 23, 32]` |
| `vprec` | Déterministe | `precision_binary64` | Non | / |
| `cancellation` | Stochastique | `tolerance` | Non | / |


La référence est : `backend = ieee` et `precision_numpy = 64`.

## Fonctions

### Noms des fonctions

`traitement_vecteur`



### Information sur les variables d'entrée

| Nom de l'entrée compacte | Type du tenseur | Ordre du tenseur | Dimension du tenseur |
| --- | --- | --- | --- |
| `alpha` | Scalaire | `0` | / |
| `v` | Vecteur | `1` | `[5]` |


### Information sur les variables de sortie

| Nom de la sortie compacte | Type du tenseur | Ordre du tenseur | Dimensions du tenseur |
| --- | --- | --- | --- |
| `sigma` | Scalaire | `0` | / |
| `pi` | Scalaire | `0` | / |
| `w` | Vecteur | `1` | `[5]` |


## Valeurs d'entrées et pseudo-aléatoire

### Type de génération des valeurs d'entrée
Générateur = `manuel`.  



### Reproductibilité des résultats

Graine du générateur = `1`.

### Ensembles de valeurs d'entrée

Nombre d'ensembles de valeurs d'entrées = `4`.

| `alpha` | `v_0` | `v_1` | `v_2` | `v_3` | `v_4` |
| --- | --- | --- | --- | --- | --- |
| `2.0` | `1.375` | `2.0` | `-0.75` | `1.25` | `1.125` |
| `0.5` | `0.0` | `1.875` | `0.25` | `2.25` | `-1.5` |
| `1.0` | `1.5` | `0.75` | `-0.875` | `-2.25` | `1.25` |
| `-1.0` | `1.625` | `-2.0` | `0.5` | `-1.5` | `1.375` |


### Nombre d'exécutions
Nombre d'exécutions pour les backends déterministes = `1`.  
Nombre d'exécutions pour les backends stochastiques = `4`.




# Résultats


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

| Fonction →<br><br>↓ Backend | `traitement_vecteur` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=traitement_vecteur/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=traitement_vecteur/backend=mca/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=traitement_vecteur/backend=bitmask/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Fonction →<br><br>↓ Backend | `traitement_vecteur` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=traitement_vecteur/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=traitement_vecteur/backend=mca/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=traitement_vecteur/backend=bitmask/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Barres des erreurs en forme non compacte

#### Fonction = `traitement_vecteur`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `sigma` | `pi` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=ieee/sortie_nom=sigma/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=ieee/sortie_nom=pi/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=mca/sortie_nom=sigma/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=mca/sortie_nom=pi/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=bitmask/sortie_nom=sigma/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=bitmask/sortie_nom=pi/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `sigma` | `pi` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=ieee/sortie_nom=sigma/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=ieee/sortie_nom=pi/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=mca/sortie_nom=sigma/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=mca/sortie_nom=pi/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=bitmask/sortie_nom=sigma/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=traitement_vecteur/backend=bitmask/sortie_nom=pi/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Enveloppes de quantiles du nombre de chiffres significatifs en forme non compacte

#### Fonction = `traitement_vecteur`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `sigma` | `pi` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=traitement_vecteur/backend=ieee/sortie_nom=sigma/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=traitement_vecteur/backend=ieee/sortie_nom=pi/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=traitement_vecteur/backend=mca/sortie_nom=sigma/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=traitement_vecteur/backend=mca/sortie_nom=pi/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `bitmask` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=traitement_vecteur/backend=bitmask/sortie_nom=sigma/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=traitement_vecteur/backend=bitmask/sortie_nom=pi/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


## Analyse paramétrique
Pour cette analyse, les paramètres fixés sont : `backend = ieee` et `precision_numpy = 64`.

### Nuages de points du comportement

#### Fonction = `traitement_vecteur`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `sigma` | `pi` |
| --- | --- | --- |
| `alpha` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=traitement_vecteur/entree_nom=alpha/sortie_nom=sigma.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=traitement_vecteur/entree_nom=alpha/sortie_nom=pi.png" style="width:400px; height:auto;"> |



