**Analyse de sensibilité**  

Nom de l'utilisateur : Jean-Baptiste Gaillot  
Date : 2026-07-31  
Commentaire : /  

# Paramètres

## Backends

| Backend | Type du backend | Paramètre du backend | Activation | Précision du backend |
| --- | --- | --- | --- | --- |
| `ieee` | Déterministe | `precision_numpy` | Oui | `[16, 32, 64]` |
| `mca` | Stochastique | `precision_binary64` | Oui | `[10, 23, 52]` |
| `bitmask` | Stochastique | `precision_binary64` | Non | / |
| `vprec` | Déterministe | `precision_binary64` | Non | / |
| `cancellation` | Stochastique | `tolerance` | Non | / |


La référence est : `backend = ieee` et `precision_numpy = 64`.

## Fonctions

### Noms des fonctions

`calculer_Id_pow_sqrt`

`calculer_Id_sqrt_pow`

### Signatures et corps des fonctions

<div style="height: 5px;"></div>
```py
def calculer_Id_pow_sqrt(x):
    
    
    Id = pow(math.sqrt(x), 2)
    
    
    return Id

```


```py
def calculer_Id_sqrt_pow(x):
    
    
    Id = math.sqrt(pow(x, 2))
    
    
    return Id

```




### Information sur les variables d'entrée

| Nom de l'entrée compacte | Type du tenseur | Ordre du tenseur | Dimension du tenseur | Domaine |
| --- | --- | --- | --- | --- |
| `x` | Scalaire | `0` | / | `[0.0, 16.0]` |


### Information sur les variables de sortie

| Nom de la sortie compacte | Type du tenseur | Ordre du tenseur | Dimensions du tenseur |
| --- | --- | --- | --- |
| `Id` | Scalaire | `0` | / |


## Valeurs d'entrées et pseudo-aléatoire

### Type de génération des valeurs d'entrée
Générateur = `sobol`.  



### Reproductibilité des résultats

Graine du générateur = `1`.

### Ensembles de valeurs d'entrée

Nombre d'ensembles de valeurs d'entrée approximatif = `10000`.  
Nombre d'ensembles de valeurs d'entrée = `16384`.

| `x` |
| --- |
| `2.4874450862407684` |
| `9.419957220554352` |
| `2.4874450862407684` |
| `9.419957220554352` |
| `13.414155468344688` |
| `1.6649624556303024` |
| `13.414155468344688` |
| `1.6649624556303024` |
| `9.813529282808304` |
| `13.747073233127594` |
| `9.813529282808304` |
| `13.747073233127594` |
| `6.775578543543816` |
| `5.495980903506279` |
| `6.775578543543816` |
| `5.495980903506279` |
| `4.079725593328476` |
| `15.003647208213806` |
| `4.079725593328476` |
| `15.003647208213806` |
| 16364 autres... |


Le nombre d'ensembles de valeurs d'entrées non compactes est > 20 : on affiche seulement les 20 premières lignes.

### Nombre d'exécutions
Nombre d'exécutions pour les backends déterministes = `1`.  
Nombre d'exécutions pour les backends stochastiques = `1000`.




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

| Fonction →<br><br>↓ Backend | `calculer_Id_pow_sqrt` | `calculer_Id_sqrt_pow` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_pow_sqrt/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_sqrt_pow/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_pow_sqrt/backend=mca/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_sqrt_pow/backend=mca/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Fonction →<br><br>↓ Backend | `calculer_Id_pow_sqrt` | `calculer_Id_sqrt_pow` |
| --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_pow_sqrt/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_sqrt_pow/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_pow_sqrt/backend=mca/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_Id_sqrt_pow/backend=mca/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Cartes d'intensité des erreurs en forme discretisée et non compacte

#### Fonction = `calculer_Id_pow_sqrt`

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_pow_sqrt/backend=ieee/entree_nom=x/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_pow_sqrt/backend=ieee/entree_nom=x/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_pow_sqrt/backend=mca/entree_nom=x/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_pow_sqrt/backend=mca/entree_nom=x/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_Id_sqrt_pow`

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_sqrt_pow/backend=ieee/entree_nom=x/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_sqrt_pow/backend=ieee/entree_nom=x/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_sqrt_pow/backend=mca/entree_nom=x/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_Id_sqrt_pow/backend=mca/entree_nom=x/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Barres des erreurs en forme non compacte

#### Fonction = `calculer_Id_pow_sqrt`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `Id` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_pow_sqrt/backend=ieee/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_pow_sqrt/backend=mca/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `Id` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_pow_sqrt/backend=ieee/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_pow_sqrt/backend=mca/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_Id_sqrt_pow`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `Id` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_sqrt_pow/backend=ieee/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_sqrt_pow/backend=mca/sortie_nom=Id/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `Id` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_sqrt_pow/backend=ieee/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_Id_sqrt_pow/backend=mca/sortie_nom=Id/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Enveloppes de quantiles du nombre de chiffres significatifs en forme non compacte

#### Fonction = `calculer_Id_pow_sqrt`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `Id` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_Id_pow_sqrt/backend=ieee/sortie_nom=Id/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_Id_pow_sqrt/backend=mca/sortie_nom=Id/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_Id_sqrt_pow`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `Id` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_Id_sqrt_pow/backend=ieee/sortie_nom=Id/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |
| `mca` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_Id_sqrt_pow/backend=mca/sortie_nom=Id/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


## Analyse paramétrique
Pour cette analyse, les paramètres fixés sont : `backend = ieee` et `precision_numpy = 64`.

### Nuages de points du comportement

#### Fonction = `calculer_Id_pow_sqrt`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_Id_pow_sqrt/entree_nom=x/sortie_nom=Id.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_Id_sqrt_pow`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `Id` |
| --- | --- |
| `x` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_Id_sqrt_pow/entree_nom=x/sortie_nom=Id.png" style="width:400px; height:auto;"> |


### Matrices de similitude

| Nom de la sortie non compacte →<br><br>↓ Type de graphique | `Id` |
| --- | --- |
| Moyenne des similitudes absolues | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=Id/type_graphique=erreur_absolue.png" style="width:400px; height:auto;"> |
| Moyenne des similitudes relatives | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=Id/type_graphique=erreur_relative.png" style="width:400px; height:auto;"> |



