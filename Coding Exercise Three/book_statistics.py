import csv
import os

# --- STEP 1: AUTOMATIC FILE CREATION ---
# This eliminates the "file not found" error by writing the CSV data automatically if it doesn't exist.
input_csv = "books.csv"
output_txt = "book_stats.txt"

sample_csv_content = """title,author,year,pages
The Hobbit,J.R.R. Tolkien,1937,310
The Catcher in the Rye,J.D. Salinger,1951,220
The Great Gatsby,F. Scott Fitzgerald,1925,180
The Lord of the Rings: The Fellowship of the Ring,J.R.R. Tolkien,1954,492
"""

if not os.path.exists(input_csv):
    with open(input_csv, mode="w", encoding="utf-8") as f:
        f.write(sample_csv_content)
    print(f"--> Notice: '{input_csv}' was missing, so it was automatically created for you at:")
    print(f"    {os.path.abspath(input_csv)}\n")


# --- STEP 2: MAIN PROGRAM LOGIC ---
def process_books(file_name):
    # This 2D array will store our records: [[title, author, year, pages], ...]
    books_2d_array = []

    try:
        with open(file_name, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            # Skip the header row (title,author,year,pages)
            header = next(reader)

            for row in reader:
                if len(row) == 4:
                    title = row[0].strip()
                    author = row[1].strip()
                    # Convert fields to proper data types (integers)
                    year = int(row[2].strip())
                    pages = int(row[3].strip())

                    # Append the record as a list into our 2D array
                    books_2d_array.append([title, author, year, pages])

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' still could not be accessed.")
        return

    if not books_2d_array:
        print("No data found in the CSV file.")
        return

    # --- Calculations ---
    total_books = len(books_2d_array)
    total_years = 0
    total_pages = 0

    # Initialize tracking variables with the first book's data
    book_most_pages = books_2d_array[0]
    book_least_pages = books_2d_array[0]

    # Loop through the 2D array to find stats
    for book in books_2d_array:
        total_years += book[2]
        total_pages += book[3]

        # Check for book with most pages
        if book[3] > book_most_pages[3]:
            book_most_pages = book

        # Check for book with fewest pages
        if book[3] < book_least_pages[3]:
            book_least_pages = book

    # Calculate averages
    avg_year = total_years / total_books
    avg_pages = total_pages / total_books

    # --- Format Output Strings ---
    output_lines = [
        f"Average Publication Year: {avg_year}",
        f"Average Number of Pages: {avg_pages}",
        f"Book with Most Pages: Title: {book_most_pages[0]}, Author: {book_most_pages[1]}, Year: {book_most_pages[2]}, Pages: {book_most_pages[3]}",
        f"Book with Least Pages: Title: {book_least_pages[0]}, Author: {book_least_pages[1]}, Year: {book_least_pages[2]}, Pages: {book_least_pages[3]}"
    ]

    # --- Output to Terminal ---
    print("--- Terminal Output ---")
    for line in output_lines:
        print(line)

    # --- Output to File ---
    with open(output_txt, mode="w", encoding="utf-8") as out_file:
        for line in output_lines:
            out_file.write(line + "\n")

    print("\n------------------------------------------------")
    print(f"Results have also been successfully saved to file: '{output_txt}'")


# Run the program
if __name__ == "__main__":
    process_books(input_csv)