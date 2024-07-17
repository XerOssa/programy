import os

BASE_DIR = 'D:/ROBOTA/GEOPARTNER/dw513/pomiary/ro_sspw'

measurement_files = []

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith('.txt'):
            measurement_files.append(os.path.join(root, file))

measurements = []

for file in measurement_files:
    with open(file) as stream:
        content = stream.read()
        cleaned_lines = ["\t".join(line.split()) for line in content.split('\n')]
        measurements.append("\n".join(cleaned_lines))

output_filename = 'D:/ROBOTA/GEOPARTNER/dw513/pomiary/ro_sspw/zbiorczy1706.txt'
with open(output_filename, 'w') as writer:
    writer.write("\n\n".join(measurements)) 

print("Zapisano do pliku:", output_filename)
