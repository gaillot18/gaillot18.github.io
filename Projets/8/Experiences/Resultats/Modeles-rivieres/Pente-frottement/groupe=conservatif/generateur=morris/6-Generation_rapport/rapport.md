**Analyse de sensibilité**  

Nom de l'utilisateur : Jean-Baptiste Gaillot  
Date : 2026-07-30  
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

`calculer_S_f_1_c`

`calculer_S_f_2_c`

`calculer_S_f_3_c`

### Signatures et corps des fonctions

<div style="height: 5px;"></div>
```py
def calculer_S_f_1_c(
    b,
    r,
    A,
    Q
    ):

    
    S_f = (
        r ** 2
    ) * (
        (b + 2 * A / b) ** (4 / 3)
    ) * (
        Q * abs(Q)
    ) / (
        A ** (10 / 3)
    )

    
    return S_f

```


```py
def calculer_S_f_2_c(
    b,
    r,
    A,
    Q
    ):
    
    
    S_f = (
        (
            ((b + 2 * A / b) / A) ** (4 / 3)
        ) * (
            r ** 2 * Q * abs(Q) / A ** 2
        )
    )
    
    
    return S_f

```


```py
def calculer_S_f_3_c(
    b,
    r,
    A,
    Q
    ):
    
    
    S_f = (
        (
            r ** 2
        ) * (
            ((b ** 2 + 2 * A) / b) ** (4 / 3)
        ) * (
            Q * abs(Q) / A ** (10 / 3)
        )
    )
    
    
    return S_f

```




### Information sur les variables d'entrée

| Nom de l'entrée compacte | Type du tenseur | Ordre du tenseur | Dimension du tenseur | Domaine |
| --- | --- | --- | --- | --- |
| `b` | Scalaire | `0` | / | `[5.0, 15.0]` |
| `r` | Scalaire | `0` | / | `[0.025, 0.045]` |
| `A` | Scalaire | `0` | / | `[5.0, 75.0]` |
| `Q` | Scalaire | `0` | / | `[0.0, 375.0]` |


### Information sur les variables de sortie

| Nom de la sortie compacte | Type du tenseur | Ordre du tenseur | Dimensions du tenseur |
| --- | --- | --- | --- |
| `S_f` | Scalaire | `0` | / |


## Valeurs d'entrées et pseudo-aléatoire

### Type de génération des valeurs d'entrée
Générateur = `morris`.  



### Reproductibilité des résultats

Graine du générateur = `1`.

### Ensembles de valeurs d'entrée

Nombre d'ensembles de valeurs d'entrée approximatif = `1000000`.  
Nombre d'ensembles de valeurs d'entrée = `1000000`.

| `b` | `r` | `A` | `Q` |
| --- | --- | --- | --- |
| `11.666666666666666` | `0.03833333333333333` | `28.333333333333336` | `0.0` |
| `5.0` | `0.03833333333333333` | `28.333333333333336` | `0.0` |
| `5.0` | `0.025` | `28.333333333333336` | `0.0` |
| `5.0` | `0.025` | `75.0` | `0.0` |
| `5.0` | `0.025` | `75.0` | `250.0` |
| `8.333333333333334` | `0.03166666666666667` | `75.0` | `375.0` |
| `8.333333333333334` | `0.03166666666666667` | `75.0` | `125.00000000000001` |
| `15.0` | `0.03166666666666667` | `75.0` | `125.00000000000001` |
| `15.0` | `0.03166666666666667` | `28.333333333333336` | `125.00000000000001` |
| `15.0` | `0.045` | `28.333333333333336` | `125.00000000000001` |
| `5.0` | `0.045` | `51.666666666666664` | `250.0` |
| `5.0` | `0.045` | `51.666666666666664` | `0.0` |
| `11.666666666666666` | `0.045` | `51.666666666666664` | `0.0` |
| `11.666666666666666` | `0.045` | `5.0` | `0.0` |
| `11.666666666666666` | `0.03166666666666667` | `5.0` | `0.0` |
| `5.0` | `0.03833333333333333` | `51.666666666666664` | `0.0` |
| `5.0` | `0.025` | `51.666666666666664` | `0.0` |
| `5.0` | `0.025` | `51.666666666666664` | `250.0` |
| `11.666666666666666` | `0.025` | `51.666666666666664` | `250.0` |
| `11.666666666666666` | `0.025` | `5.0` | `250.0` |
| 999980 autres... | 999980 autres... | 999980 autres... | 999980 autres... |


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

| Fonction →<br><br>↓ Backend | `calculer_S_f_1_c` | `calculer_S_f_2_c` | `calculer_S_f_3_c` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_1_c/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_2_c/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_3_c/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Fonction →<br><br>↓ Backend | `calculer_S_f_1_c` | `calculer_S_f_2_c` | `calculer_S_f_3_c` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_1_c/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_2_c/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_3_c/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Cartes d'intensité des erreurs en forme discretisée et non compacte

#### Fonction = `calculer_S_f_1_c`

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=A/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=Q/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=A/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_c/backend=ieee/entree_nom=Q/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_2_c`

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=A/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=Q/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=A/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_c/backend=ieee/entree_nom=Q/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_3_c`

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=A/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=Q/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=A/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_c/backend=ieee/entree_nom=Q/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Barres des erreurs en forme non compacte

#### Fonction = `calculer_S_f_1_c`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_1_c/backend=ieee/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_1_c/backend=ieee/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_2_c`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_2_c/backend=ieee/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_2_c/backend=ieee/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_3_c`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_3_c/backend=ieee/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_3_c/backend=ieee/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Enveloppes de quantiles du nombre de chiffres significatifs en forme non compacte

#### Fonction = `calculer_S_f_1_c`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_S_f_1_c/backend=ieee/sortie_nom=S_f/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_2_c`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_S_f_2_c/backend=ieee/sortie_nom=S_f/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_3_c`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_S_f_3_c/backend=ieee/sortie_nom=S_f/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


## Analyse paramétrique
Pour cette analyse, les paramètres fixés sont : `backend = ieee` et `precision_numpy = 64`.

### Nuages de points du comportement

#### Fonction = `calculer_S_f_1_c`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_c/entree_nom=b/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_c/entree_nom=r/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_c/entree_nom=A/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_c/entree_nom=Q/sortie_nom=S_f.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_2_c`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_c/entree_nom=b/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_c/entree_nom=r/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_c/entree_nom=A/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_c/entree_nom=Q/sortie_nom=S_f.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_3_c`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_c/entree_nom=b/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_c/entree_nom=r/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `A` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_c/entree_nom=A/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `Q` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_c/entree_nom=Q/sortie_nom=S_f.png" style="width:400px; height:auto;"> |


### Matrices de similitude

| Nom de la sortie non compacte →<br><br>↓ Type de graphique | `S_f` |
| --- | --- |
| Moyenne des similitudes absolues | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=S_f/type_graphique=erreur_absolue.png" style="width:400px; height:auto;"> |
| Moyenne des similitudes relatives | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=S_f/type_graphique=erreur_relative.png" style="width:400px; height:auto;"> |


### Indices de Morris

| Nom de la sortie non compacte →<br><br>↓ Fonction | `S_f` |
| --- | --- |
| `calculer_S_f_1_c` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=calculer_S_f_1_c/sortie_nom=S_f.png" style="width:600px; height:auto;"> |
| `calculer_S_f_2_c` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=calculer_S_f_2_c/sortie_nom=S_f.png" style="width:600px; height:auto;"> |
| `calculer_S_f_3_c` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=calculer_S_f_3_c/sortie_nom=S_f.png" style="width:600px; height:auto;"> |



