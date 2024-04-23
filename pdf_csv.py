# import fitz
# import pandas as pd

# # Open the PDF
# pdf = fitz.open(r"assets\redemption_details.pdf")

# # Initialize an empty list to store DataFrames from all pages
# all_dfs = []

# # Loop through each page in the PDF
# for page_number in range(len(pdf)):
#     pdf_page = pdf[page_number]
#     pdf_tabs = pdf_page.find_tables()

#   # Check if any tables are found on the current page
#     if pdf_tabs:
#         pdf_tab = pdf_tabs[0]  # Assuming you want the first table on each page
#         pdf_df = pdf_tab.to_pandas()
#         all_dfs.append(pdf_df)

# # Combine all DataFrames into a single one (optional)
# if all_dfs:
#     final_df = pd.concat(all_dfs, ignore_index=True)
#     print(final_df)

#     # Save the final DataFrame to CSV (adjust filename)
#     final_df.to_csv("assets\redemption.csv", index =False)
#     print("Converted all pages to combined_redemption_details.csv")
# else:
#     print("No tables found in the PDF")


import fitz
import pandas as pd

# Open the PDF
pdf = fitz.open(r"assets\redemption_details.pdf")

# Initialize an empty list to store DataFrames from all pages
all_dfs = []

# Loop through each page in the PDF
for page_number in range(len(pdf)):
    pdf_page = pdf[page_number]
    pdf_tabs = pdf_page.find_tables()

    # Check if any tables are found on the current page
    if pdf_tabs:
        pdf_tab = pdf_tabs[0]  # Assuming you want the first table on each page
        pdf_df = pdf_tab.to_pandas()
        all_dfs.append(pdf_df)

# Combine all DataFrames into a single one (optional)
if all_dfs:
    final_df = pd.concat(all_dfs, ignore_index=True)
    print(final_df)

    # Save the final DataFrame to CSV (adjust filename)
    final_df.to_csv(r"assets\redemption.csv", index=False)  # Corrected file path
    print("Converted all pages to redemption.csv")
else:
    print("No tables found in the PDF")
