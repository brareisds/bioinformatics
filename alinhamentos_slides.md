# Metodologia

## Organismos utilizados 
| Organismo | Domínio | Ambiente | OGT | Accession NCBI |
|---|---|---|---|---|
| *Thermocrinis ruber* | Bacteria | Hipertermófilo | > 80°C | GCA_000512735.1 |
| *Thermotoga maritima* | Bacteria | Hipertermófilo | > 80°C | GCA_000008545.1 |
| *Pyrococcus furiosus* | Archaea | Hipertermófilo | > 80°C | GCA_000007305.1 |
| *Thermococcus litoralis* | Archaea | Hipertermófilo | > 80°C | GCA_000246985.3 |
| *Escherichia fergusonii* | Bacteria | Mesófilo | 20–45°C | GCA_000026225.1 |
| *Methanococcus maripaludis* | Archaea | Mesófilo | 20–45°C | GCA_002945325.1 |
| *Psychrobacter arcticus* | Bacteria | Psicrófilo | < 20°C | GCA_000012305.1 |
| *Methanococcoides burtonii* | Archaea | Psicrófilo | < 20°C | GCA_000013725.1 |
> Millán Arias P et al. *Environment and taxonomy shape the genomic signature of prokaryotic extremophiles.* Sci Rep. 2023;13:16105. https://doi.org/10.1038/s41598-023-42518-y


## 1. Alinhamento Múltiplo

### Genes Selecionados

| Gene | KO Number | Função resumida |
|------|-----------|----------------|
| dnaK | K04043 | Chaperona Hsp70: dobramento e estabilização de proteínas no frio |
| groEL | K04077 | Chaperonina: remonta proteínas desnaturadas pelo calor |
| gyrA | K02469 | DNA girase (sub. A): regula superenrolamento do DNA no frio |
| deaD | K05592 | RNA helicase DEAD-box: desfaz estruturas secundárias de RNA no frio |
| reverse gyrase | K03170 | Topoisomerase exclusiva de hipertermófilos: superenrolamento positivo do DNA |



## Mapeamento KEGG - Presença e Ausência dos Genes 

| Organismo | Ambiente | dnaK | groEL | gyrA | rev. gyrase | deaD |
|-----------|----------|:----:|:-----:|:----:|:-----------:|:----:|
| *T. ruber* | Hipertermófilo | ✓ | ✓ | ✓ | ✗ | ✓ |
| *T. maritima* | Hipertermófilo | ✓ | ✓ | ✓ | ✓ | ✗ |
| *P. furiosus* | Hipertermófilo | ✗ | ✗ | ✗ | ✓ | ✗ |
| *T. litoralis* | Hipertermófilo | ✗ | ✗ | ✗ | ✓ | ✓ |
| *E. fergusonii* | Mesófilo | ✓ | ✓ | ✓ | ✗ | ✓ |
| *M. maripaludis* | Mesófilo | ✗ | ✗ | ✗ | ✗ | ✓ |
| *P. arcticus* | Psicrófilo | ✓ | ✓ | ✓ | ✗ | ✗ |
| *M. burtonii* | Psicrófilo | ✓ | ✗ | ✓ | ✗ | ✗ |



## Organismos em cada Alinhamento

| Gene | Hipertermófilos | Mesófilos | Psicrófìlos | N |
|------|----------------|-----------|-------------|---|
| gyrA | *T. ruber*, *T. maritima* | *E. fergusonii* | *P. arcticus*, *M. burtonii* | 5 |
| revgyrase | *T. maritima*, *P. furiosus*, *T. litoralis* | — | — | 3 |
| dnaK | *T. ruber*, *T. maritima* | *E. fergusonii* | *P. arcticus*, *M. burtonii* | 5 |
| groEL | *T. ruber*, *T. maritima* | *E. fergusonii* | *P. arcticus* | 4 |
| deaD | *T. ruber*, *T. litoralis* | *E. fergusonii*, *M. maripaludis* | — | 4 |

> **Nota:** gyrA, dnaK e groEL cobrem os 3 ambientes térmicos, deaD cobre hipertermófilos e mesófilos.



## Fluxo da Metodologia 

```
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  1. KEGG Mapping                                                        │
 │     Identificação dos KO numbers e verificação de presença/ausência                      │       de cada gene em cada organismo
 │     · Verificação de presença/ausência em cada organismo               │
 │     · Identificação dos accessions NCBI via páginas de entrada KEGG    │
 └────────────────────────────────┬────────────────────────────────────────┘
                                  ▼
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  2. Download das Sequências (NCBI Protein)                              │
 │    Sequências proteicas baixadas via Biopython (Entrez.efetch)
        no formato FASTA, com accessions identificados no KEGG                                                               │
 └────────────────────────────────┬────────────────────────────────────────┘
                                  ▼
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  3. Alinhamento Múltiplo — MAFFT --auto                                 │
 │     · Algoritmo selecionado automaticamente: L-INS-i                   │
 │       (iterative refinement + Smith-Waterman local pairwise)           │
 │     · Matriz de substituição: BLOSUM62                                 │
 │     · Saída: 5 arquivos .fasta alinhados                               │
 └─────────────────────────────────────────────────────────────────────────┘
                                ▼
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  4. Análise                                                             │
 │     Classificação de posições conservadas vs. discriminantes e 
   cálculo do perfil químico  por grupo ambiental                                                           
 └─────────────────────────────────────────────────────────────────────────┘
```

## Análise das Posições do Alinhamento


| Tipo | Definição | Interpretação biológica |
|------|-----------|------------------------|
| **Conservada** | Mesmo aminoácido em todos os organismos, independente do ambiente | Posição essencial para a função, qualquer mutação seria deletéria |
| **Discriminante** | Cada grupo ambiental tem aminoácidos *completamente distintos* dos outros grupos | Candidata a refletir adaptação imposta pelo nicho térmico |


### Resumo por gene

| Gene | Total (aa) | Conservadas | % Conservadas | Discriminantes | Grupos ambientais |
|------|:----------:|:-----------:|:-------------:|:------------:|:-----------------:|
| gyrA | 1019 | 210 | 20,6% | 55 | Hipert. / Mesóf. / Psicrófilo |
| dnaK | 670 | 226 | 33,7% | 32 | Hipert. / Mesóf. / Psicrófilo |
| groEL | 553 | 254 | 45,9% | 46 | Hipert. / Mesóf. / Psicrófilo |
| deaD | 732 | 89 | 12,2% | 190 | Hipert. / Mesóf. |

