# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:59:00 2025

@author: shruti
"""

import pandas as pd

class CSVTransformer:
    def __init__(self, input_file, sequence_file, output_file):
        self.input_file = input_file
        self.sequence_file = sequence_file
        self.output_file = output_file

    def load_csv(self):
        return pd.read_csv(self.input_file)

    def save_csv(self, df):
        df.to_csv(self.output_file, index=False)

    def remove_row(self, df, index):
        if 0 <= index < len(df):
            df = df.drop(index) 
            df = df.reset_index(drop=True)
        return df

    def remove_column(self, df, index):
        if 0 <= index < df.shape[1]:
            col_name = df.columns[index]
            df.drop(columns=[col_name], inplace=True)
        return df

    def transpose(self, df):
        df_transposed = df.transpose()
        df_transposed = df_transposed.reset_index()
        new_column_names = df_transposed.iloc[0].tolist()
        df_transposed.columns = new_column_names  
        df_transposed = df_transposed.iloc[1:].reset_index(drop=True)
        print(df_transposed)
        return df_transposed
    
    def transformer(self,df):
        with open(self.sequence_file, 'r') as f:
            for line in f:
                command = line.strip()
                if "rmrow" in command:
                    index = int(command[6])
                    df = self.remove_row(df, index)
                elif "rmcol" in command:
                    index = int(command[6])
                    df = self.remove_column(df, index)
                elif command == "transpose":
                    df = self.transpose(df)
            return df
        

    def run(self):
        df = self.load_csv()
        df = self.transformer(df)
        self.save_csv(df)

if __name__ == "__main__":
    processor = CSVTransformer("data.csv", "sequence.txt", "output.csv")
    processor.run()
