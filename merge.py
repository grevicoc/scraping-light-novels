from PyPDF2 import PdfMerger
import os

folder_path = "C:\Programming\Projects\scraping-light-novels\light_novel_pdfs"
files_in_numbers = [int(f.strip(".pdf")) for f in os.listdir(folder_path)]
sorted_files_in_numbers = sorted(files_in_numbers)
# print(sorted_files_in_numbers)

all_pdfs = [os.path.join(folder_path, str(f) + ".pdf") for f in sorted_files_in_numbers]
batch_size = 50
chapter_start = 951

for i in range(0, len(all_pdfs), batch_size):
    batch_pdfs = all_pdfs[i:i + batch_size]
    # print(batch_pdfs)
    # continue
    
    output_file = f"Overgeared {chapter_start}-{chapter_start+batch_size-1}.pdf"
    
    # Merge PDFs
    merger = PdfMerger()
    for pdf in batch_pdfs:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
    
    print(f"{output_file} sucessfully created.")
    chapter_start += batch_size
