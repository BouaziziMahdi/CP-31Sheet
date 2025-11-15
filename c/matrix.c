#include<stdio.h>

//saisir la matrice
void  saisir(int M[20][20] ,int L ,int C){
    for(int i=0;i<L;i++){
        for (int j=0; j<C; j++){
            printf("introduire un entier \n");
            scanf("%i",&M[i][j]);
        }
    }
}

//afficher la matrice
void affiCher(int M[20][20] ,int L ,int C){
   for(int i=0;i<L;i++){
        for (int j=0; j<C; j++){
            printf(" %i  |",M[i][j]);
        }
    }
    printf("\n");
}

//somme des elements de la matrice
void sumMatrix(int M1[20][20] , M2[20][20] , M3[20][20] , int L, int C) {
   
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            M3[i][j]= M1[i][j]+ M2[i][j];
        }
    }
}

//produit des elements de la matrice
void prodMatrix(int M[20][20],int M1[20][20], int L, int C,int M3[20]) {
    for (int i = 0; i < L; i++) {
        M3[i]=0;
        for (int j = 0; j < C; j++) {
            M3[i] += M[i][j] * M1[i][j];
        }
    }
    printf("le produit des elements de la matriCe est %i \n", prod);
    return prod;
}

//afficher la produit des elements de la matrice
void afficherProdMatrix(int M[20][20], int L, int C) {
    int prod = prodMatrix(M, L, C);
    printf("le produit des elements de la matriCe est %i \n", prod);
}

//programme principal 
void main(){
    int M[20][20];
    int L,;
    do{
        printf("introduire le nombre de lignes \n");
        scanf("%i",&L);
    }while(L<=0 || L>20);
    do{
        printf("introduire le nombre de Colonnes \n");
        scanf("%i",&C);
    }while(C<=0|| C>20);
    saisir(M,L,C);
    affiCher (M,L,C);
    sumMatrix(M,L,C);
    prodMatrix(M,L,C);
    afficherProdMatrix(M,L,C);
}