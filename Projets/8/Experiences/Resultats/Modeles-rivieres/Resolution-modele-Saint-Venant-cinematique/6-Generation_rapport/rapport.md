**Analyse de sensibilité**  

Nom de l'utilisateur : Jean-Baptiste Gaillot  
Date : 2026-07-31  
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

`resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif`

### Signatures et corps des fonctions

<div style="height: 5px;"></div>
```py
def resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif(
    A_entree : list,
    Q_entree : list
    ) -> np.ndarray:
    
    
    global type_donnee
    type_donnee = type(A_entree[0])
    A = np.array(A_entree, dtype = type_donnee)
    Q = np.array(Q_entree, dtype = type_donnee)
    
    
    # Fixation de certaines variables
    nombre_minute = 1
    L_s = np.array(100.0, dtype = type_donnee)
    L_t = np.array(nombre_minute * 60.0, dtype = type_donnee)
    K = len(A) - 2
    Delta_s = np.r_[0, (2 * np.arange(1, K + 1) - 1) * L_s / (2 * K + 1), L_s]
    Delta_s = np.array(Delta_s, dtype = type_donnee)
    b = np.array([10.0] * (K + 2), dtype = type_donnee)
    r = np.array([0.035] * (K + 2), dtype = type_donnee)
    S_0 = np.array([0.01] * (K + 2), dtype = type_donnee)
    q = np.array([[0.0] * (K + 2)] * nombre_minute, dtype = type_donnee)
    Delta_t = 0.5
    
    
    t_actuel = np.array(0.0, dtype = type_donnee)
    n = 0


    while t_actuel <= L_t:
        
        
        A_precedent = A.copy()
        Q_precedent = Q.copy()


        q_n = q[calculer_indice_minute(t_actuel, q), :]


        for k in range(1, K + 1):
            

            # Calcul de A
            A[k] = (
                A_precedent[k] 
                - (Delta_t / Delta_s[k]) * (Q_precedent[k] - Q_precedent[k - 1])
                + Delta_t * q_n[k]
                )


            # Calcul de Q
            Q[k] = (
                A[k]
                * calculer_R_k(A, b, k) ** np.array(2.0 / 3.0, dtype = type_donnee)
                * np.sqrt(S_0[k])
                / r[k]
                )


        A[K + 1] = A[K]
        Q[K + 1] = Q[K]
        
        
        t_actuel += Delta_t
        n += 1
    
    
    A_sortie = A
    Q_sortie = Q


    return A_sortie, Q_sortie

```




### Information sur les variables d'entrée

| Nom de l'entrée compacte | Type du tenseur | Ordre du tenseur | Dimension du tenseur | Domaine |
| --- | --- | --- | --- | --- |
| `A_entree` | Vecteur | `1` | `[9]` | `[10.0, 50.0]` |
| `Q_entree` | Vecteur | `1` | `[9]` | `[0.0, 100.0]` |


### Information sur les variables de sortie

| Nom de la sortie compacte | Type du tenseur | Ordre du tenseur | Dimensions du tenseur |
| --- | --- | --- | --- |
| `A_sortie` | Vecteur | `1` | `[9]` |
| `Q_sortie` | Vecteur | `1` | `[9]` |


## Valeurs d'entrées et pseudo-aléatoire

### Type de génération des valeurs d'entrée
Générateur = `morris`.  



### Reproductibilité des résultats

Graine du générateur = `1`.

### Ensembles de valeurs d'entrée

Nombre d'ensembles de valeurs d'entrée approximatif = `10000`.  
Nombre d'ensembles de valeurs d'entrée = `10013`.

| `A_entree_0` | `A_entree_1` | `A_entree_2` | `A_entree_3` | `A_entree_4` | `A_entree_5` | `A_entree_6` | `A_entree_7` | `A_entree_8` | `Q_entree_0` | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `10.0` | `10.0` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `50.0` | `100.0` | 8 autres... |
| `10.0` | `10.0` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `50.0` | `100.0` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `50.0` | `100.0` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `50.0` | `100.0` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `23.333333333333336` | `100.0` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `36.666666666666664` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `10.0` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `10.0` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `36.666666666666664` | `10.0` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `36.666666666666664` | `23.333333333333336` | `10.0` | `10.0` | `10.0` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `36.666666666666664` | `50.0` | `10.0` | `10.0` | `10.0` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `36.666666666666664` | `36.666666666666664` | `50.0` | `10.0` | `10.0` | `10.0` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `36.666666666666664` | `36.666666666666664` | `50.0` | `10.0` | `10.0` | `10.0` | `10.0` | `36.666666666666664` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `36.666666666666664` | `36.666666666666664` | `50.0` | `10.0` | `10.0` | `10.0` | `10.0` | `10.0` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `36.666666666666664` | `36.666666666666664` | `50.0` | `36.666666666666664` | `10.0` | `10.0` | `10.0` | `10.0` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `36.666666666666664` | `36.666666666666664` | `50.0` | `36.666666666666664` | `10.0` | `10.0` | `36.666666666666664` | `10.0` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `36.666666666666664` | `36.666666666666664` | `50.0` | `36.666666666666664` | `10.0` | `10.0` | `36.666666666666664` | `10.0` | `23.333333333333336` | `33.333333333333336` | 8 autres... |
| `10.0` | `23.333333333333336` | `50.0` | `23.333333333333336` | `23.333333333333336` | `36.666666666666664` | `50.0` | `23.333333333333336` | `10.0` | `0.0` | 8 autres... |
| 9993 autres... | 9993 autres... | 9993 autres... | 9993 autres... | 9993 autres... | 9993 autres... | 9993 autres... | 9993 autres... | 9993 autres... | 9993 autres... | ... |


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

| Fonction →<br><br>↓ Backend | `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Fonction →<br><br>↓ Backend | `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif` |
| --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Cartes d'intensité des erreurs en forme spatialisée et non compacte

#### Fonction = `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif`

##### Backend = `ieee`

###### Nom de la sortie non compacte = `A_sortie`

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
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=A_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

</div>



###### Nom de la sortie non compacte = `Q_sortie`

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
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Type de graphique →<br><br>↓ `precision_numpy` | moyenne<br>des erreurs relatives | médiane<br>des erreurs relatives | minimum<br>des erreurs relatives | maximum<br>des erreurs relatives | coefficient de variation<br>des erreurs relatives |
| --- | --- | --- | --- | --- | --- |
| `16` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=16/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `32` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=moyenne/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=mediane/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=minimum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=maximum/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_spatial_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom_compact=Q_sortie/precision_numpy=32/type_graphique=coefficient_variation/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `64` | *Référence* | *Référence* | *Référence* | *Référence* | *Référence* |

</div>

</div>



### Cartes d'intensité des erreurs en forme discretisée et non compacte

#### Fonction = `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif`

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

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `A_entree_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=A_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=A_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=A_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=Q_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=Q_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=Q_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `A_entree_4` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=A_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=A_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=A_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=Q_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=Q_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=Q_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `A_entree_7` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=A_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=A_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=A_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=Q_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=Q_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=Q_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `Q_entree_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=A_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=A_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=A_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=Q_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=Q_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=Q_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `Q_entree_4` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=A_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=A_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=A_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=Q_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=Q_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=Q_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |
| `Q_entree_7` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=A_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=A_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=A_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=Q_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=Q_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=Q_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `A_entree_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=A_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=A_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=A_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=Q_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=Q_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_1/sortie_nom=Q_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `A_entree_4` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=A_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=A_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=A_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=Q_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=Q_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_4/sortie_nom=Q_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `A_entree_7` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=A_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=A_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=A_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=Q_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=Q_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=A_entree_7/sortie_nom=Q_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `Q_entree_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=A_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=A_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=A_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=Q_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=Q_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_1/sortie_nom=Q_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `Q_entree_4` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=A_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=A_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=A_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=Q_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=Q_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_4/sortie_nom=Q_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |
| `Q_entree_7` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=A_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=A_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=A_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=Q_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=Q_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_discret_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/entree_nom=Q_entree_7/sortie_nom=Q_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Barres des erreurs en forme non compacte

#### Fonction = `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif`

<div class="type-erreur-switch">
<div class="type-erreur-switch-controle">
<div class="type-erreur-switch-titre">Type d'erreur</div>
<div class="type-erreur-switch-segmente">
<button class="type-erreur-switch-option type-erreur-switch-option-actif" data-type-erreur="erreur_absolue" onclick="basculerTypeErreur(this)">absolue</button>
<button class="type-erreur-switch-option" data-type-erreur="erreur_relative" onclick="basculerTypeErreur(this)">relative</button>
</div>
</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_absolue">

| Nom de la sortie non compacte →<br><br>↓ Backend | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_1/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_4/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_7/type_erreur=erreur_absolue.png" style="width:400px; height:auto;"> |

</div>

<div class="type-erreur-panneau" data-type-erreur="erreur_relative" style="display:none;">

| Nom de la sortie non compacte →<br><br>↓ Backend | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_1/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_4/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Erreur_barre_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_7/type_erreur=erreur_relative.png" style="width:400px; height:auto;"> |

</div>

</div>



### Enveloppes de quantiles du nombre de chiffres significatifs en forme non compacte

#### Fonction = `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif`

|  Nom de la sortie non compacte →<br><br>↓ Backend | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `ieee` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_4/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=A_sortie_7/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_1/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_4/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_numerique/Enveloppe_quantile_chiffre_significatif_non_compact/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/backend=ieee/sortie_nom=Q_sortie_7/type_graphique=nombre_chiffres_significatifs_base_2.png" style="width:400px; height:auto;"> |


## Analyse paramétrique
Pour cette analyse, les paramètres fixés sont : `backend = ieee` et `precision_numpy = 64`.

### Nuages de points du comportement

#### Fonction = `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif`

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée non compacte | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `A_entree_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_1/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_1/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_1/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_1/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_1/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_1/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `A_entree_4` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_4/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_4/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_4/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_4/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_4/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_4/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `A_entree_7` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_7/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_7/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_7/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_7/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_7/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=A_entree_7/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `Q_entree_1` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_1/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_1/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_1/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_1/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_1/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_1/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `Q_entree_4` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_4/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_4/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_4/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_4/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_4/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_4/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `Q_entree_7` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_7/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_7/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_7/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_7/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_7/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Nuage_comportement/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/entree_nom=Q_entree_7/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |


### Indices de Morris

| Nom de la sortie non compacte →<br><br>↓ Fonction | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/sortie_nom=A_sortie_1.png" style="width:600px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/sortie_nom=A_sortie_4.png" style="width:600px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/sortie_nom=A_sortie_7.png" style="width:600px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/sortie_nom=Q_sortie_1.png" style="width:600px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/sortie_nom=Q_sortie_4.png" style="width:600px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/sortie_nom=Q_sortie_7.png" style="width:600px; height:auto;"> |


### Indices de Morris en forme spatialisée

#### Fonction = `resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif`

##### Type de graphique = moyenne normalisée des effets élémentaires

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée compacte | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `A_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `Q_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |


##### Type de graphique = moyenne en valeur absolue normalisée des effets élémentaires

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée compacte | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `A_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `Q_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=moyenne_valeur-absolue_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |


##### Type de graphique = écart-type normalisé des effets élémentaires

| Nom de la sortie non compacte →<br><br>↓ Nom de l'entrée compacte | `A_sortie_1` | `A_sortie_4` | `A_sortie_7` | `Q_sortie_1` | `Q_sortie_4` | `Q_sortie_7` |
| --- | --- | --- | --- | --- | --- | --- |
| `A_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=A_entree/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |
| `Q_entree` | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=A_sortie_7.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_1.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_4.png" style="width:400px; height:auto;"> | <img src="/Repertoire_racine/Resultats/5-Creation_graphiques/Analyse_parametrique/Indice_morris_spatial/fonction=resoudre_saint_venant_cinematique_volume_fini_upwind_conservatif/type_graphique=ecart-type_effet-elementaire/entree_nom_compact=Q_entree/sortie_nom=Q_sortie_7.png" style="width:400px; height:auto;"> |



