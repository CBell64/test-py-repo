import csv
import os

def analyze_books(file_path, output_path):
    # Initialize trackers and metrics accumulators
    total_year = 0
    total_pages = 0
    count = 0
    
    max_book = None
    min_book = None
    
    # DYNAMIC PATH FIX: Find the exact folder where this script lives
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_csv_path = os.path.join(script_dir, file_path)
    full_output_path = os.path.join(script_dir, output_path)
    
    # Process the CSV file using the absolute path we just calculated
    with open(full_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
        # DictReader maps fields out dynamically according to the file header labels
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            # Data Type Conversion Phase: Cast numeric inputs to integers
            title = row['book title'].strip()
            author = row['author name'].strip()
            year = int(row['year published'])
            pages = int(row['number of pages'])
            
            # Map tracking references to a structured dictionary representation
            current_book = {
                'title': title,
                'author': author,
                'year': year,
                'pages': pages
            }
            
            # Accumulate totals for calculation vectors
            total_year += year
            total_pages += pages
            count += 1
            
            # Store data context for the book containing the most pages
            if max_book is None or pages > max_book['pages']:
                max_book = current_book
                
            # Store data context for the book containing the fewest pages
            if min_book is None or pages < min_book['pages']:
                min_book = current_book
                
    # Summary Calculations Phase
    avg_year = total_year / count if count > 0 else 0
    avg_pages = total_pages / count if count > 0 else 0
    
    # Construct a clean text block layout for uniform formatting across environments
    report_lines = [
        "===============================================",
        "           BOOK ANALYSIS REPORT                ",
        "===============================================",
        f"Total Books Processed:       {count}",
        f"Average Year of Publication:  {avg_year:.1f}",
        f"Average Number of Pages:     {avg_pages:.1f}",
        "-----------------------------------------------",
        "BOOK WITH THE MOST PAGES:",
        f"  Title:    {max_book['title'] if max_book else 'N/A'}",
        f"  Author:   {max_book['author'] if max_book else 'N/A'}",
        f"  Year:     {max_book['year'] if max_book else 'N/A'}",
        f"  Pages:    {max_book['pages'] if max_book else 'N/A'}",
        "-----------------------------------------------",
        "BOOK WITH THE FEWEST PAGES:",
        f"  Title:    {min_book['title'] if min_book else 'N/A'}",
        f"  Author:   {min_book['author'] if min_book else 'N/A'}",
        f"  Year:     {min_book['year'] if min_book else 'N/A'}",
        f"  Pages:    {min_book['pages'] if min_book else 'N/A'}",
        "==============================================="
    ]
    
    report_output = "\n".join(report_lines)
    
    # Target 1: Push structured presentation to stdout terminal
    print(report_output)
    
    # Target 2: Commit identical presentation output to disk storage file
    with open(full_output_path, mode='w', encoding='utf-8') as out_file:
        out_file.write(report_output)

if __name__ == "__main__":
    # Call the function with just the raw file names
    analyze_books("books.csv", "book_analysis_report.txt")