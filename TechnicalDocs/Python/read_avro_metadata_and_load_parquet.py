import sys
import fastavro
import pandas as pd

def read_avro_metadata(avro_filename):
    with open(avro_filename, 'rb') as avro_file:
        reader = fastavro.reader(avro_file)
        metadata = reader.metadata
    return metadata

def load_parquet_file(parquet_filename):
    df = pd.read_parquet(parquet_filename)
    return df

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python read_avro_metadata_and_load_parquet.py <avro_filename>")
        sys.exit(1)

    avro_filename = sys.argv[1]
    
    # Read Avro metadata
    metadata = read_avro_metadata(avro_filename)
    print("Avro Metadata:", metadata)
    
    # Assuming the Parquet filename is stored in the Avro metadata under a specific key
    # Replace 'parquet_filename_key' with the actual key name that holds the Parquet filename
    parquet_filename_key = 'parquet_filename'  # This should be the key in the metadata where the Parquet filename is stored
    if parquet_filename_key in metadata:
        parquet_filename = metadata[parquet_filename_key]
        print(f"Loading Parquet file: {parquet_filename}")
        
        # Load the Parquet file into a DataFrame
        df = load_parquet_file(parquet_filename)
        print(df.head())
    else:
        print(f"Metadata key '{parquet_filename_key}' not found in Avro metadata")
