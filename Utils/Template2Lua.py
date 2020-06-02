outputFile = open("RoomTemplateOut.txt", "w")
outputFile.write("{\n")

with open("RoomTemplates.txt") as templateFile:
    for line in templateFile:
        line = line.strip()
        if line == "":
            outputFile.write("}\n")
            outputFile.write("\n")
            outputFile.write("{\n")
            pass
        else:
            lineFormatted = "".join(map(lambda x: f"{x}, ", line))
            templateLine =  f"\t{{ {lineFormatted} }},\n"
            outputFile.write(templateLine)
            
outputFile.write("}")
outputFile.close()