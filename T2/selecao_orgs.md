# Análise Filogenética - Trabalho 2

## Organismos selecionados

Os organismos foram selecionados a partir de:

- **Millán Arias et al. (2023)**: Supplementary Table S1, que reúne ~700 genomas procarióticos com temperatura ótima de crescimento (OGT) conhecida. Quatro dos seis organismos foram retirados diretamente dessa tabela.
- **Literatura de extremófilos**: Dois organismos foram adicionados para garantir representação de dois filos distintos em todas as categorias térmicas.

O critério de seleção foi garantir dois organismos de filos diferentes para cada categoria térmica (hipertermófilo, mesófilo e psicrófilo), permitindo avaliar se o agrupamento filogenético reflete o ambiente compartilhado ou o parentesco evolutivo.

| Organismo | Filo | Categoria | OGT | Assembly NCBI | 
|---|---|---|---|---|
| *Thermocrinis ruber* | Aquificae | Hipertermófilo | >80°C | GCA_000512735.1 
| *Thermotoga maritima* | Thermotogae | Hipertermófilo | >80°C | GCA_000008545.1 
| *Escherichia fergusonii* | Proteobacteria | Mesófilo | 20–45°C | GCA_000026225.1 
| *Bacillus subtilis* | Firmicutes | Mesófilo | 25–35°C | GCA_000009045.1 
| *Psychrobacter arcticus* | Proteobacteria | Psicrófilo | <20°C | GCA_000012305.1 
| *Exiguobacterium sibiricum* | Firmicutes | Psicrófilo | −5°C | GCA_000026245.1 

---

## Distâncias de divergência evolutiva entre os pares

Para garantir que qualquer agrupamento observado nas árvores dos genes de temperatura não possa ser atribuído a parentesco evolutivo recente, as distâncias de divergência entre os dois organismos de cada categoria foram estimadas com o **TimeTree** (https://timetree.org).

### Como o TimeTree calcula o tempo

O TimeTree funciona em três etapas. Primeiro, dado o par de organismos consultado, o sistema localiza o ancestral comum mais recente (MRCA) dos dois na árvore cronológica da vida (TTOL — Timetree of Life). Quando um dos organismos não está diretamente na TTOL, o NCBI Taxonomy é consultado para identificar o parente mais próximo disponível, que é usado como substituto. Por fim, o tempo de divergência do MRCA é recuperado do banco do TimeTree, que agrega resultados de múltiplos estudos filogenéticos publicados, o valor reportado é a mediana entre esses estudos, acompanhada de um intervalo de confiança.


### Resultados

| Categoria | Par | Divergência (mediana) | IC |
|---|---|---|---|
| Hipertermófilo | *T. ruber* (Aquificae) × *T. maritima* (Thermotogae) | **~4,18 Ga (bilhões de anos)** | 3,64 – 4,19 Ga |
| Mesófilo | *E. fergusonii* (Proteobacteria) × *B. subtilis* (Firmicutes) | **~3,13 Ga (bilhões de anos)** | 1,01 – 3,19 Ga |
| Psicrófilo | *P. arcticus* (Proteobacteria) × *E. sibiricum* (Firmicutes) | **~3,13 Ga (bilhões de anos)** | 1,01 – 3,19 Ga |

> Ga = Giga-annum = bilhão de anos. Unidade padrão em geologia e biologia evolutiva para escalas de tempo geológico.

Os pares de mesófilo e psicrófilo apresentam a mesma distância porque compartilham o mesmo par de filos — Proteobacteria × Firmicutes.
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
| *E. fergusonii* | ✓ | ✓ | ✓ | ✓ |
| *B. subtilis* | ✓ | ✓ | ✓ | ✓ |
| *P. arcticus* | ✓ | ✓ | ✓ | ✗ |
| *E. sibiricum* | ✓ | ✓ | ✓ | ✓ |

> ✗ Ausência confirmada no mapeamento KEGG — organismos excluídos do alinhamento de deaD.

---

## Genes identificados no KEGG

Os genes foram identificados diretamente no KEGG a partir da busca pelos termos *dnaK*, *groEL*, *gyrA* e *deaD* em cada genoma. A presença dos genes foi confirmada pelo KO correspondente e, posteriormente, as sequências nucleotídicas CDS foram obtidas diretamente pela API REST do KEGG.

### Genes selecionados

| Organismo | dnaK | groEL | gyrA | deaD |
|---|---|---|---|---|
| *Thermocrinis ruber* | [trd:THERU_01435](https://www.kegg.jp/entry/trd:THERU_01435) | [trd:THERU_06905](https://www.kegg.jp/entry/trd:THERU_06905) | [trd:THERU_01910](https://www.kegg.jp/entry/trd:THERU_01910) | [trd:THERU_06610](https://www.kegg.jp/entry/trd:THERU_06610) |
| *Thermotoga maritima* | [tma:TM0373](https://www.kegg.jp/entry/tma:TM0373) | [tma:TM0506](https://www.kegg.jp/entry/tma:TM0506) | [tma:TM1084](https://www.kegg.jp/entry/tma:TM1084) | — |
| *Escherichia fergusonii* | [efe:EFER_0010](https://www.kegg.jp/entry/efe:EFER_0010) | [efe:EFER_4195](https://www.kegg.jp/entry/efe:EFER_4195) | [efe:EFER_0934](https://www.kegg.jp/entry/efe:EFER_0934) | [efe:EFER_3141](https://www.kegg.jp/entry/efe:EFER_3141) |
| *Bacillus subtilis* | [bsu:BSU25470](https://www.kegg.jp/entry/bsu:BSU25470) | [bsu:BSU06030](https://www.kegg.jp/entry/bsu:BSU06030) | [bsu:BSU00070](https://www.kegg.jp/entry/bsu:BSU00070) | [bsu:BSU04580](https://www.kegg.jp/entry/bsu:BSU04580) |
| *Psychrobacter arcticus* | [par:Psyc_2132](https://www.kegg.jp/entry/par:Psyc_2132) | [par:Psyc_0553](https://www.kegg.jp/entry/par:Psyc_0553) | [par:Psyc_1543](https://www.kegg.jp/entry/par:Psyc_1543) | — |
| *Exiguobacterium sibiricum* | [esi:Exig_0781](https://www.kegg.jp/entry/esi:Exig_0781) | [esi:Exig_2768](https://www.kegg.jp/entry/esi:Exig_2768) | [esi:Exig_0006](https://www.kegg.jp/entry/esi:Exig_0006) | [esi:Exig_0618](https://www.kegg.jp/entry/esi:Exig_0618) |

### Obtenção das sequências nucleotídicas

Após a identificação dos genes, as sequências nucleotídicas codificantes (CDS) foram obtidas diretamente por meio da API REST do KEGG. Para cada gene foi realizada uma requisição utilizando o identificador KEGG correspondente:

```
https://rest.kegg.jp/get/<gene_id>/ntseq
```

Por exemplo, para o gene *deaD* de *Thermocrinis ruber*:

```
https://rest.kegg.jp/get/trd:THERU_06610/ntseq
```

Esse endpoint retorna diretamente a sequência nucleotídica codificante associada ao gene.

