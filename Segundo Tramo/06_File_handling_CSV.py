""" - - - - - - - - - - - - - - -
 Manejo de *.csv files
- - - - - - - - - - - - - - - - """

#Tambien hay un modulo para operaciones con csv
import csv

csv_file = open("./my_file.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["Alumno", "T.P.1", "T.P.2", "Evaluación final", "Estado"])
csv_writer.writerow(["Fabrina Rovaretti", "7", "9", "10", "PROMOCIONADO"])
csv_writer.writerow(["Bel Corzo", "5", "6", "4", "APROBADO"])

csv_file.close()

with open("./my_file.csv") as my_other_file:
    for lines in my_other_file.readlines():
        print(lines)