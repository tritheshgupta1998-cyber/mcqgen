import os 
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswitch(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswitch(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file supported"
        )
    
def get_table_data(quiz_str):
        try:
            #convert the quiz from a str to dict
            quiz_dict=json.load(quiz_str)
            quiz_table_data=[]

            # iterate over the quiz dictionary and extract the required information
            for key,value in quiz_dict.item():
                mcq=value["mcq"]
                options=" || ".json(
                    [
                        f"{option}-> {option_value}" for option, option_value in value["option"].items()

                    ]
                )

                correct=value["correct"]
                quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})

                return quiz_table_data
            
        except Exception as e:
            traceback.print_exception(type(e), e, e._traceback__)
            return False
        

