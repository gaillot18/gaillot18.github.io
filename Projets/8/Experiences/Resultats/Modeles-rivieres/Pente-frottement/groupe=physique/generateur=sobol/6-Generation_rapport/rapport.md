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

`calculer_S_f_1_p`

`calculer_S_f_2_p`

`calculer_S_f_3_p`

### Signatures et corps des fonctions

<div style="height: 5px;"></div>
```py
def calculer_S_f_1_p(
    b,
    r,
    h,
    u
    ):

    
    S_f = (
        r ** 2 * (b + 2 * h) ** (4 / 3) * u * abs(u)
    ) / (
        b ** (4 / 3) * h ** (4 / 3)
    )

    
    return S_f

```


```py
def calculer_S_f_2_p(
    b,
    r,
    h,
    u
    ):

    
    S_f = (
        r ** 2 * (b + 2 * h) ** (4 / 3) * u * abs(u)
    ) / (
        (b * h) ** (4 / 3)
    )

    
    return S_f

```


```py
def calculer_S_f_3_p(
    b,
    r,
    h,
    u
    ):

    
    S_f = (
        r ** 2
    ) * (
        ((b + 2 * h) / (b * h)) ** (4 / 3)
    ) * (
        u * abs(u)
    )

    
    return S_f

```




### Information sur les variables d'entrée

| Nom de l'entrée compacte | Type du tenseur | Ordre du tenseur | Dimension du tenseur | Domaine |
| --- | --- | --- | --- | --- |
| `b` | Scalaire | `0` | / | `[5.0, 15.0]` |
| `r` | Scalaire | `0` | / | `[0.025, 0.045]` |
| `h` | Scalaire | `0` | / | `[1.0, 5.0]` |
| `u` | Scalaire | `0` | / | `[0.0, 5.0]` |


### Information sur les variables de sortie

| Nom de la sortie compacte | Type du tenseur | Ordre du tenseur | Dimensions du tenseur |
| --- | --- | --- | --- |
| `S_f` | Scalaire | `0` | / |


## Valeurs d'entrées et pseudo-aléatoire

### Type de génération des valeurs d'entrée
Générateur = `sobol`.  



### Reproductibilité des résultats

Graine du générateur = `1`.

### Ensembles de valeurs d'entrée

Nombre d'ensembles de valeurs d'entrée approximatif = `1000000`.  
Nombre d'ensembles de valeurs d'entrée = `1310720`.

| `b` | `r` | `h` | `u` |
| --- | --- | --- | --- |
| `6.55465317890048` | `0.036774946525692936` | `3.430128701031208` | `1.2119999481365085` |
| `13.456894652917981` | `0.036774946525692936` | `3.430128701031208` | `1.2119999481365085` |
| `6.55465317890048` | `0.030251211691647767` | `3.430128701031208` | `1.2119999481365085` |
| `6.55465317890048` | `0.036774946525692936` | `3.70155843347311` | `1.2119999481365085` |
| `6.55465317890048` | `0.036774946525692936` | `3.430128701031208` | `1.8833170644938946` |
| `6.55465317890048` | `0.030251211691647767` | `3.70155843347311` | `1.8833170644938946` |
| `13.456894652917981` | `0.036774946525692936` | `3.70155843347311` | `1.8833170644938946` |
| `13.456894652917981` | `0.030251211691647767` | `3.430128701031208` | `1.8833170644938946` |
| `13.456894652917981` | `0.030251211691647767` | `3.70155843347311` | `1.2119999481365085` |
| `13.456894652917981` | `0.030251211691647767` | `3.70155843347311` | `1.8833170644938946` |
| `14.88037240691483` | `0.02627763131633401` | `2.6972698867321014` | `3.8660809257999063` |
| `5.757029661908746` | `0.02627763131633401` | `2.6972698867321014` | `3.8660809257999063` |
| `14.88037240691483` | `0.044716176744550466` | `2.6972698867321014` | `3.8660809257999063` |
| `14.88037240691483` | `0.02627763131633401` | `1.6462399773299694` | `3.8660809257999063` |
| `14.88037240691483` | `0.02627763131633401` | `2.6972698867321014` | `3.309651492163539` |
| `14.88037240691483` | `0.044716176744550466` | `1.6462399773299694` | `3.309651492163539` |
| `5.757029661908746` | `0.02627763131633401` | `1.6462399773299694` | `3.309651492163539` |
| `5.757029661908746` | `0.044716176744550466` | `2.6972698867321014` | `3.309651492163539` |
| `5.757029661908746` | `0.044716176744550466` | `1.6462399773299694` | `3.8660809257999063` |
| `5.757029661908746` | `0.044716176744550466` | `1.6462399773299694` | `3.309651492163539` |
| 1310700 autres... | 1310700 autres... | 1310700 autres... | 1310700 autres... |


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

| Fonction →<br><br>↓ Backend | `calculer_S_f_1_p` | `calculer_S_f_2_p` | `calculer_S_f_3_p` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_1_p/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_2_p/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_3_p/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Fonction →<br><br>↓ Backend | `calculer_S_f_1_p` | `calculer_S_f_2_p` | `calculer_S_f_3_p` |
| --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_1_p/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_2_p/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=calculer_S_f_3_p/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Cartes d'intensité des erreurs en forme discretisée et non compacte

#### Fonction = `calculer_S_f_1_p`

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
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=h/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=u/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=h/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_1_p/backend=ieee/entree_nom=u/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_2_p`

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
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=h/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=u/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=h/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_2_p/backend=ieee/entree_nom=u/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_3_p`

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
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=h/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=u/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=b/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=r/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=h/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=calculer_S_f_3_p/backend=ieee/entree_nom=u/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Barres des erreurs en forme non compacte

#### Fonction = `calculer_S_f_1_p`

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
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_1_p/backend=ieee/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_1_p/backend=ieee/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_2_p`

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
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_2_p/backend=ieee/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_2_p/backend=ieee/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



#### Fonction = `calculer_S_f_3_p`

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
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_3_p/backend=ieee/sortie_nom=S_f/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=calculer_S_f_3_p/backend=ieee/sortie_nom=S_f/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Enveloppes de quantiles du nombre de chiffres significatifs en forme non compacte

#### Fonction = `calculer_S_f_1_p`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_S_f_1_p/backend=ieee/sortie_nom=S_f/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_2_p`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_S_f_2_p/backend=ieee/sortie_nom=S_f/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_3_p`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `S_f` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=calculer_S_f_3_p/backend=ieee/sortie_nom=S_f/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


## Analyse paramétrique
Pour cette analyse, les paramètres fixés sont : `backend = ieee` et `precision_numpy = 64`.

### Nuages de points du comportement

#### Fonction = `calculer_S_f_1_p`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_p/entree_nom=b/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_p/entree_nom=r/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_p/entree_nom=h/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_1_p/entree_nom=u/sortie_nom=S_f.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_2_p`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_p/entree_nom=b/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_p/entree_nom=r/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_p/entree_nom=h/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_2_p/entree_nom=u/sortie_nom=S_f.png" style="width:400px; height:auto;"> |


#### Fonction = `calculer_S_f_3_p`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `S_f` |
| --- | --- |
| `b` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_p/entree_nom=b/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `r` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_p/entree_nom=r/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `h` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_p/entree_nom=h/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `u` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=calculer_S_f_3_p/entree_nom=u/sortie_nom=S_f.png" style="width:400px; height:auto;"> |


### Matrices de similitude

| Nom de la sortie non compacte →<br><br>↓ Type de graphique | `S_f` |
| --- | --- |
| Moyenne des similitudes absolues | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=S_f/type_graphique=erreur_absolue.png" style="width:400px; height:auto;"> |
| Moyenne des similitudes relatives | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_similitude/sortie_nom=S_f/type_graphique=erreur_relative.png" style="width:400px; height:auto;"> |


### Matrices de Sobol

| Nom de la sortie non compacte →<br><br>↓ Fonction | `S_f` |
| --- | --- |
| `calculer_S_f_1_p` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=calculer_S_f_1_p/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `calculer_S_f_2_p` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=calculer_S_f_2_p/sortie_nom=S_f.png" style="width:400px; height:auto;"> |
| `calculer_S_f_3_p` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Matrice_sobol/fonction=calculer_S_f_3_p/sortie_nom=S_f.png" style="width:400px; height:auto;"> |


### Barres de Sobol

| Nom de la sortie non compacte →<br><br>↓ Fonction | `S_f` |
| --- | --- |
| `calculer_S_f_1_p` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=calculer_S_f_1_p/sortie_nom=S_f.png" style="width:800px; height:auto;"> |
| `calculer_S_f_2_p` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=calculer_S_f_2_p/sortie_nom=S_f.png" style="width:800px; height:auto;"> |
| `calculer_S_f_3_p` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Barre_sobol/fonction=calculer_S_f_3_p/sortie_nom=S_f.png" style="width:800px; height:auto;"> |



