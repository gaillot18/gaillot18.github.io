####################################################################################################
#
####################################################################################################
def automate_cellulaire_2d_1(M_entree):
    
    
    type_donnee = type(M_entree[0][0])
        
        
    I = len(M_entree)
    J = len(M_entree[0])
    
    
    if type_donnee is float:
        M_temporaire = [[0.0 for _ in range(J)] for _ in range(I)]
        M_sortie = [[0.0 for _ in range(J)] for _ in range(I)]
    else:
        M_temporaire = [[type_donnee(0.0) for _ in range(J)] for _ in range(I)]
        M_sortie = [[type_donnee(0.0) for _ in range(J)] for _ in range(I)]
    
    
    for n in range(1):
        for i in range(I):
            for j in range(J):
                
                
                voisin_gauche = (j - 1) % J
                voisin_droite = (j + 1) % J
                voisin_bas = (i - 1) % I
                voisin_haut = (i + 1) % I
                
                
                if type_donnee is float:
                    M_temporaire[i][j] = (
                        0.3 * M_entree[i][voisin_gauche] +
                        0.3 * M_entree[i][voisin_droite] +
                        0.2 * M_entree[voisin_haut][j] +
                        0.2 * M_entree[voisin_bas][j]
                    )
                else:
                    M_temporaire[i][j] = (
                        type_donnee(0.3) * type_donnee(M_entree[i][voisin_gauche]) +
                        type_donnee(0.3) * type_donnee(M_entree[i][voisin_droite]) +
                        type_donnee(0.2) * type_donnee(M_entree[voisin_haut][j]) +
                        type_donnee(0.2) * type_donnee(M_entree[voisin_bas][j])
                    )
        
        
        for i in range(I):
            for j in range(J):
                M_sortie[i][j] = M_temporaire[i][j]
                
        
        return M_sortie
####################################################################################################





####################################################################################################
#
####################################################################################################
def automate_cellulaire_2d_2(M_entree):
    
    
    type_donnee = type(M_entree[0][0])
    
    
    I = len(M_entree)
    J = len(M_entree[0])
    
    
    if type_donnee is float:
        M_temporaire = [[0.0 for _ in range(J)] for _ in range(I)]
        M_sortie = [[0.0 for _ in range(J)] for _ in range(I)]
    else:
        M_temporaire = [[type_donnee(0.0) for _ in range(J)] for _ in range(I)]
        M_sortie = [[type_donnee(0.0) for _ in range(J)] for _ in range(I)]
    
    
    for n in range(1):
        for i in range(I):
            for j in range(J):
                
                
                voisin_gauche = (j - 1) % J
                voisin_droite = (j + 1) % J
                voisin_bas = (i - 1) % I
                voisin_haut = (i + 1) % I
                
                
                if type_donnee is float:
                    M_temporaire[i][j] = (
                        0.3 * (
                            M_entree[i][voisin_gauche] + M_entree[i][voisin_droite]
                            ) +
                        0.2 * (
                            M_entree[voisin_haut][j] + M_entree[voisin_bas][j]
                            )
                    )
                else:
                    M_temporaire[i][j] = (
                        type_donnee(0.3) * (
                            type_donnee(M_entree[i][voisin_gauche]) + type_donnee(M_entree[i][voisin_droite])
                            ) +
                        type_donnee(0.2) * (
                            type_donnee(M_entree[voisin_haut][j]) + type_donnee(M_entree[voisin_bas][j])
                            )
                    )
        
        
        for i in range(I):
            for j in range(J):
                M_sortie[i][j] = M_temporaire[i][j]
                
        
        return M_sortie
####################################################################################################