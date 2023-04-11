import csv

input_file = "entrada.txt"
output_file = "salida.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
    tsv_reader = csv.reader(infile, delimiter="\t")  # Cambia "\t" a " " si los datos están separados por espacios
    csv_writer = csv.writer(outfile)
    
    for row in tsv_reader:
        csv_writer.writerow(row)