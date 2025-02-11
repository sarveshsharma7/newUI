import streamlit as st
import time
import pandas as pd
from io import BytesIO

def run_model_1(pdf_file, excel_file):
    time.sleep(2)  # Simulating processing time
    return "Model_1_Result.csv", pd.DataFrame({"Output": ["Result 1"]})

def run_model_2():
    time.sleep(2)
    return "Model_2_Result.csv", pd.DataFrame({"Output": ["Result 2"]})

def run_model_3():
    time.sleep(2)
    return "Model_3_Result.csv", pd.DataFrame({"Output": ["Result 3"]})

st.title("File Processing Pipeline")

pdf_file = st.file_uploader("Upload PDF File", type=["pdf"])
excel_file = st.file_uploader("Upload Excel File", type=["xls", "xlsx"])

if st.button("Run Models"):
    if pdf_file and excel_file:
        status_box = st.empty()
        
        status_box.text("Translating files")
        file1_name, df1 = run_model_1(pdf_file, excel_file)
        
        status_box.text("Extracting key value pairs")
        file2_name, df2 = run_model_2()
        
        status_box.text("Genrating final output")
        file3_name, df3 = run_model_3()
        
        status_box.text("Processing Completed!")
        
        def convert_df_to_csv(df):
            output = BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)
            return output
        
        st.download_button("Download Translated File", convert_df_to_csv(df1), file1_name, "text/csv")
        st.download_button("Download Key Value Pairs", convert_df_to_csv(df2), file2_name, "text/csv")
        st.download_button("Download Populated Excel File", convert_df_to_csv(df3), file3_name, "text/csv")
    else:
        st.warning("Please upload both PDF and Excel files to proceed.")
