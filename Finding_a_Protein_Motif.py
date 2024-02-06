import urllib.request

def get_id_list(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        full_id_list = sorted([line.strip() for line in lines])
        id_list = sorted([line for line in lines if "_" not in line])
        strip_list = [line.split("_")[0] for line in lines if "_" in line]
        
        final_list = id_list + strip_list
        final_list = sorted([line.strip() for line in final_list])

        return final_list, full_id_list 

def download_txt_file(url, file_path):
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"ID: {file_path}\nFile downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

def get_fasta_sequence(url, file_path):
    download_txt_file(url, file_path)
    with open(file_path, "r") as file:
        lines = file.readlines()
        sequence = "".join([line.strip() for line in lines[1:]])
        return sequence

def find_protein_motif(sequence):
    motif = "N{P}[ST]{P}"
    motif_positions = []
    for i in range(len(sequence) - 3):
        if sequence[i] == "N" and sequence[i + 1] != "P" and sequence[i + 2] in ["S", "T"] and sequence[i + 3] != "P":
            motif_positions.append(i + 1)
    return motif_positions

prot_dict = {}
id_list, full_id_list = get_id_list(r"c:\Users\colto\Downloads\rosalind_mprt.txt")

for id, full_id in zip(id_list, full_id_list):
    url = f"http://www.uniprot.org/uniprot/{id}.fasta"
    file_path = f"c:\\Users\\colto\\Downloads\\{id}.fasta"
    prot_dict[full_id] = get_fasta_sequence(url, file_path)

for id, sequence in prot_dict.items():
    motif_positions = find_protein_motif(sequence)
    if motif_positions:
        output_file_path = "c:\\Users\\colto\\Downloads\\motif_positions.txt"
        with open(output_file_path, "w") as output_file:
            output_file.write(f"{id}\n")
            output_file.write(" ".join(map(str, motif_positions)))
            output_file.write("\n")
            print(f"{id} written to motif_positions.txt")
