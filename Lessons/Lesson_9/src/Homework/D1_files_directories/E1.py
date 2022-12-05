import os
import pprint

# Write a function that receives a directory path, searches there for csv files,
# and if csv files exist - return the following data for each: filename, amount of columns, amount of rows.
# You can assume that all the csv files are in the correct format.

# Make sure you handle properly a case in which the provided path does not exist.
# In addition, you should take into account that there can be inner folders with files,
# and you should find them all. Test your code with this folder.

# Hint: check out os.walk function to iterate directory

def get_csv_md(fpath: str, delimiter: str = ",") -> dict[str, int]:
    with open(fpath, "r") as fh:
        content = fh.readline()
        row_cnt = 0
        col_cnt = len(content.split(",")) if len(content.split(",")) > 1 else len(content.split(delimiter))
        for _ in fh:
            row_cnt += 1
    return {"rows": row_cnt, "cols": col_cnt} if delimiter in content else {}


def search(fpath: str, csv_delimiter: str = ",") -> dict[str, dict[str, int]]:
    ret_dict = {}
    for root, dirs, files in os.walk(fpath):
        for file_name in files:
            _, ext = os.path.splitext(file_name)
            if ext == ".csv":
                full_path = os.path.join(root, file_name)
                meta_data_dict = get_csv_md(full_path, csv_delimiter)
                if meta_data_dict:
                    ret_dict[file_name] = meta_data_dict
    return ret_dict if ret_dict else None

if __name__ == "__main__":
    csv_separator = '-'
    a = search("/Users/danielraz/EduLabs-FullStack-Course/Lessons/Lesson_9/src/Lesson_Code/files/data", csv_separator)
    pprint.pprint(a)
