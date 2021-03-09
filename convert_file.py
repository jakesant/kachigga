from docx2pdf import convert

def con_file(file, output_path):
    output_file = file[:-4] + "pdf"
    output_path += "\\" + output_file
    convert(file, output_path = output_path)