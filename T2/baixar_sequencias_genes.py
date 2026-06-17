import requests
import os
import time

# IDs KEGG dos genes
genes_kegg = {

    "T_ruber": {
        "dnaK":  "trd:THERU_01435",
        "groEL": "trd:THERU_06905",
        "gyrA":  "trd:THERU_01910",
        "deaD":  "trd:THERU_06610",
    },

    "T_maritima": {
        "dnaK":  "tma:TM0373",
        "groEL": "tma:TM0506",
        "gyrA":  "tma:TM1084",
        "deaD":  None,
    },

    "E_fergusonii": {
        "dnaK":  "efe:EFER_0010",
        "groEL": "efe:EFER_4195",
        "gyrA":  "efe:EFER_0934",
        "deaD":  "efe:EFER_3141",
    },

    "P_arcticus": {
        "dnaK":  "par:Psyc_2132",
        "groEL": "par:Psyc_0553",
        "gyrA":  "par:Psyc_1543",
        "deaD":  None,
    },

    "A_aeolicus": {
        "dnaK":  "aae:aq_996",
        "groEL": "aae:aq_2200",
        "gyrA":  "aae:aq_980",
        "deaD":  "aae:aq_613",
    },

    "T_thermophilus": {
        "dnaK":  "tth:TT_C1127",
        "groEL": "tth:TT_C1714",
        "gyrA":  "tth:TT_C0990",
        "deaD":  "tth:TT_C1895",
    },

    "P_ingrahamii": {
        "dnaK":  "pin:Ping_0917",
        "groEL": "pin:Ping_0844",
        "gyrA":  "pin:Ping_1114",
        "deaD":  "pin:Ping_3203",
    },
}


def baixar_ntseq(kegg_id):
    url = f"https://rest.kegg.jp/get/{kegg_id}/ntseq"

    r = requests.get(url, timeout=30)

    if r.status_code != 200:
        raise RuntimeError(
            f"Erro HTTP {r.status_code} para {kegg_id}"
        )

    texto = r.text.strip()

    if not texto.startswith(">"):
        raise RuntimeError(
            f"Resposta inesperada para {kegg_id}"
        )

    return texto


os.makedirs("sequencias_nt", exist_ok=True)

por_gene = {
    "dnaK": [],
    "groEL": [],
    "gyrA": [],
    "deaD": [],
}

falhas = []

print("=" * 60)
print("Baixando sequências do KEGG")
print("=" * 60)

for organismo, genes in genes_kegg.items():

    print(f"\n{organismo}")

    for gene, kegg_id in genes.items():

        if kegg_id is None:
            print(f"  {gene}: ausente")
            continue

        print(f"  {gene} ({kegg_id})... ", end="", flush=True)

        try:

            fasta = baixar_ntseq(kegg_id)

            linhas = fasta.splitlines()

            sequencia = "".join(
                linha.strip()
                for linha in linhas
                if not linha.startswith(">")
            )

            fasta_final = (
                f">{organismo}_{gene}\n"
                f"{sequencia}"
            )

            por_gene[gene].append(fasta_final)

            print("✓")

        except Exception as e:

            print(f"✗ {e}")

            falhas.append(
                (organismo, gene, str(e))
            )

        time.sleep(0.5)

print("\n" + "=" * 60)
print("Salvando FASTAs")
print("=" * 60)

for gene, seqs in por_gene.items():

    if not seqs:
        continue

    arquivo = f"sequencias_nt/{gene}_sequencias.fasta"

    with open(arquivo, "w") as f:
        f.write("\n\n".join(seqs))

    print(
        f"{gene}: {len(seqs)} sequências -> {arquivo}"
    )

if falhas:

    print("\nFalhas encontradas:")

    for org, gene, erro in falhas:

        print(
            f"  {org} / {gene}: {erro}"
        )

print("\nConcluído.")