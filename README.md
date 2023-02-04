# python-csvtojson Converter

A simple Python script to convert a CSV file to JSON.

## Usage

1. Save the script to a file, for example, `csvtojson.py`.
2. Run the script in a terminal or command prompt, passing the path to the CSV file as an argument:

    ```
    python csv_to_json.py example.csv
    ```

3. The script will create a new file with a `.json` extension in the same directory as the CSV file.

## Configuration

By default, the script assumes that the first row of the CSV file contains the header row, and that each subsequent row represents a single entry in the data. The keys for each entry are taken from the header row, and the values are taken from the corresponding row in the data. The resulting JSON file will have one JSON object per line, with each object representing a single entry in the data.

## Limitations

The script does not handle errors, such as missing or incorrectly formatted CSV files. It is intended for use with well-formed CSV files.

