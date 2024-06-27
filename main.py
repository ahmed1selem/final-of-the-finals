import time
from item import paragraph
from fastapi import FastAPI, Body
import uvicorn


globL_time=time
start=globL_time.time()
if __name__ == '__main__':
    x = paragraph("https://www.theguardian.com/football/article/2024/jun/25/juventus-women-lead-race-to-sign-hanna-bennison-from-everton")

    start_time = time.time()  # Start time before get_cleaned()
    cleaned_text = x.get_cleaned()
    end_time = time.time()  # End time after get_cleaned()
    clean_time = end_time - start_time
    print(f"Cleaned Text:\n{cleaned_text}")
    print(f"Time to clean: {clean_time:.4f} seconds\n")  # Print time with 4 decimal places

    start_time = time.time()  # Start time before get_title()
    title = x.get_title()
    end_time = time.time()  # End time after get_title()
    title_time = end_time - start_time
    print(f"Title: {title}")
    print(f"Time to get title: {title_time:.4f} seconds\n")  # Print time with 4 decimal places

    start_time = time.time()  # Start time before get_cat()
    category = x.get_cat()
    end_time = time.time()  # End time after get_cat()
    cat_time = end_time - start_time
    print(f"Category: {category}")
    print(f"Time to get category: {cat_time:.4f} seconds\n")  # Print time with 4 decimal places
    start_time = time.time()  # Start time before get_cat()
    img = x.get_img()
    end_time = time.time()  # End time after get_cat()
    cat_time = end_time - start_time
    print(f"Category: {img}")
    print(f"Time to get category: {cat_time:.4f} seconds\n")  # Print time with 4 decimal places

    start_time = time.time()  # Start time before get_summary()
    summary = x.get_summary()
    end_time = time.time()  # End time after get_summary()
    summary_time = end_time - start_time
    print(f"Summary:\n{summary}")
    print(f"Time to get summary: {summary_time:.4f} seconds")  # Print time with 4 decimal places
end=globL_time.time()

print("Total Time",end-start)



# app = FastAPI()
#
# @app.post("/generate_paragraph")
# async def generate_paragraph(url: str = Body(...)):
#     start_time = time.time()
#     x = paragraph("https://www.bbc.com/arabic/articles/cw0vr5g2qz9o")
#
#     cleaned_text = x.get_cleaned()
#     title = x.get_title()
#     category = x.get_cat()
#     summary = x.get_summary()
#
#     end_time = time.time()
#     total_time = end_time - start_time
#
#     return {
#         "cleaned_text": cleaned_text,
#         "title": title,
#         "category": category,
#         "summary": summary,
#         "total_time": total_time
#     }
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000)
