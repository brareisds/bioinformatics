# Análise Filogenética - Trabalho 2

## Organismos selecionados

Os organismos foram selecionados a partir de:

- **Millán Arias et al. (2023)**: Supplementary Table S1, que reúne ~700 genomas procarióticos com temperatura ótima de crescimento (OGT) conhecida. Quatro dos sete organismos foram retirados diretamente dessa tabela. (os mesmos do trabalho 1)
- **Literatura de extremófilos**: Três organismos foram adicionados além da tabela original para garantir diversidade filogenética entre as bactérias hipertermófilas e termófilas.

| Organismo | Domínio | Filo | Categoria | OGT | Assembly NCBI | Fonte |
|---|---|---|---|---|---|---|
| *Thermocrinis ruber* | Bacteria | Aquificae | Hipertermófilo | >80°C | GCA_000512735.1 | Millán Arias |
| *Thermotoga maritima* | Bacteria | Thermotogae | Hipertermófilo | >80°C | GCA_000008545.1 | Millán Arias |
| *Aquifex aeolicus* | Bacteria | Aquificae | Hipertermófilo | ~95°C | GCA_000008625.1 | Literatura |
| *Thermus thermophilus* | Bacteria | Deinococcus-Thermus | Termófilo | ~65°C | GCA_000196015.1 | Literatura |
| *Escherichia fergusonii* | Bacteria | Pseudomonadota | Mesófilo | 20–45°C | GCA_000026225.1 | Millán Arias |
| *Psychrobacter arcticus* | Bacteria | Pseudomonadota | Psicrófilo | <20°C | GCA_000012305.1 | Millán Arias |
| *Psychromonas ingrahamii* | Bacteria | Pseudomonadota | Psicrófilo | −12°C | GCA_000015285.1 | Millán Arias |

---

## Genes analisados

Os quatro genes foram selecionados no Trabalho 1 com base em Verma et al. (2024) por seu envolvimento direto em respostas ao estresse térmico.

| Gene | KO Number | Função |
|---|---|---|
| dnaK | K04043 | Chaperona Hsp70 — dobramento e estabilização de proteínas |
| groEL | K04077 | Chaperonina Hsp60 — remontagem de proteínas desnaturadas |
| gyrA | K02469 | DNA girase subunidade A — regulação do superenrolamento do DNA |
| deaD | K05592 | RNA helicase DEAD-box — resolução de estruturas de RNA no frio |

---

## Presença dos genes por organismo

| Organismo | dnaK | groEL | gyrA | deaD |
|---|---|---|---|---|
| *T. ruber* | ✓ | ✓ | ✓ | ✓ |
| *T. maritima* | ✓ | ✓ | ✓ | ✗ |
| *A. aeolicus* | ✓ | ✓ | ✓ | * |
| *T. thermophilus* | ✓ | ✓ | ✓ | ✓ |
| *E. fergusonii* | ✓ | ✓ | ✓ | ✓ |
| *P. arcticus* | ✓ | ✓ | ✓ | ✗ |
| *P. ingrahamii* | ✓ | ✓ | ✓ | ✓ |

> * O gene deaD de *A. aeolicus* (aq_613) está anotado funcionalmente no KEGG mas sem KO number atribuído (K05592). Foi incluído na análise com base na anotação funcional e nomenclatura do gene.
>
> ✗ Ausência confirmada no mapeamento KEGG — organismos excluídos do alinhamento de deaD.

---

## Genes identificados no KEGG

Os genes foram identificados diretamente no KEGG a partir da busca pelos termos *dnaK*, *groEL*, *gyrA* e *deaD* em cada genoma. A presença dos genes foi confirmada pelo KO correspondente e, posteriormente, as sequências nucleotídicas CDS foram obtidas diretamente pela API REST do KEGG.

### Genes selecionados

| Organismo                 | dnaK                                                         | groEL                                                        | gyrA                                                         | deaD                                                         |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| *Thermocrinis ruber*      | [trd:THERU_01435](https://www.kegg.jp/entry/trd:THERU_01435) | [trd:THERU_06905](https://www.kegg.jp/entry/trd:THERU_06905) | [trd:THERU_01910](https://www.kegg.jp/entry/trd:THERU_01910) | [trd:THERU_06610](https://www.kegg.jp/entry/trd:THERU_06610) |
| *Thermotoga maritima*     | [tma:TM0373](https://www.kegg.jp/entry/tma:TM0373)           | [tma:TM0506](https://www.kegg.jp/entry/tma:TM0506)           | [tma:TM1084](https://www.kegg.jp/entry/tma:TM1084)           | —                                                            |
| *Aquifex aeolicus*        | [aae:aq_996](https://www.kegg.jp/entry/aae:aq_996)           | [aae:aq_2200](https://www.kegg.jp/entry/aae:aq_2200)         | [aae:aq_980](https://www.kegg.jp/entry/aae:aq_980)           | [aae:aq_613](https://www.kegg.jp/entry/aae:aq_613)           |
| *Thermus thermophilus*    | [tth:TT_C1127](https://www.kegg.jp/entry/tth:TT_C1127)       | [tth:TT_C1714](https://www.kegg.jp/entry/tth:TT_C1714)       | [tth:TT_C0990](https://www.kegg.jp/entry/tth:TT_C0990)       | [tth:TT_C1895](https://www.kegg.jp/entry/tth:TT_C1895)       |
| *Escherichia fergusonii*  | [efe:EFER_0010](https://www.kegg.jp/entry/efe:EFER_0010)     | [efe:EFER_4195](https://www.kegg.jp/entry/efe:EFER_4195)     | [efe:EFER_0934](https://www.kegg.jp/entry/efe:EFER_0934)     | [efe:EFER_3141](https://www.kegg.jp/entry/efe:EFER_3141)     |
| *Psychrobacter arcticus*  | [par:Psyc_2132](https://www.kegg.jp/entry/par:Psyc_2132)     | [par:Psyc_0553](https://www.kegg.jp/entry/par:Psyc_0553)     | [par:Psyc_1543](https://www.kegg.jp/entry/par:Psyc_1543)     | —                                                            |
| *Psychromonas ingrahamii* | [pin:Ping_0917](https://www.kegg.jp/entry/pin:Ping_0917)     | [pin:Ping_0844](https://www.kegg.jp/entry/pin:Ping_0844)     | [pin:Ping_1114](https://www.kegg.jp/entry/pin:Ping_1114)     | [pin:Ping_3203](https://www.kegg.jp/entry/pin:Ping_3203)     |

### Obtenção das sequências nucleotídicas

Após a identificação dos genes, as sequências nucleotídicas codificantes (CDS) foram obtidas diretamente por meio da API REST do KEGG. Para cada gene foi realizada uma requisição utilizando o identificador KEGG correspondente:

```text
https://rest.kegg.jp/get/<gene_id>/ntseq
```

Por exemplo, para o gene *deaD* de *Thermocrinis ruber*:

```text
https://rest.kegg.jp/get/trd:THERU_06610/ntseq
```

Esse endpoint retorna diretamente a sequência nucleotídica codificante associada ao gene


