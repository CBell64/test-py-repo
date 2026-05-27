import csv

# Define file names
input_csv = "books.csv"
output_txt = "book_stats.txt"


def process_books(file_name):
    # This 2D array will store our records: [[title, author, year, pages], ...]
    books_2d_array = []

    try:
        with open(file_name, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip the header row if your CSV has one.
            # If your CSV doesn't have a header, comment out the next line.
            header = next(reader)

            for row in reader:
                # Ensure the row has the expected number of fields
                if len(row) == 4:
                    title = row[0].strip()
                    author = row[1].strip()
                    # Convert fields to proper data types
                    year = int(row[2].strip())
                    pages = int(row[3].strip())

                    # Append the record as a list into our 2D array
                    books_2d_array.append([title, author, year, pages])

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None

    if not books_2d_array:
        print("No data found in the CSV file.")
        return None

    # --- Calculations ---
    total_books = len(books_2d_array)
    total_years = 0
    total_pages = 0

    # Initialize tracking variables with the first book's data
    book_most_pages = books_2d_array[0]
    book_least_pages = books_2d_array[0]

    # Iterate through the 2D array
    for book in books_2d_array:
        # Accumulate totals for averages
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
        f"Average Publication Year: {avg_year:.3f}",
        f"Average Number of Pages: {avg_pages:.2f}",
        f"Book with Most Pages: Title: {book_most_pages[0]}, Author: {book_most_pages[1]}, Year: {book_most_pages[2]}, Pages: {book_most_pages[3]}",
        f"Book with Least Pages: Title: {book_least_pages[0]}, Author: {book_least_pages[1]}, Year: {book_least_pages[2]}, Pages: {book_least_pages[3]}",
    ]

    # --- Output to Terminal ---
    print("\n--- Summary Statistics ---")
    for line in output_lines:
        print(line)

    # --- Output to File ---
    with open(output_txt, mode="w", encoding="utf-8") as out_file:
        for line in output_lines:
            out_file.write(line + "\n")

    print(f"\nResults have been successfully saved to '{output_txt}'.")


# Run the program
if __name__ == "__main__":
    process_books(input_csv)