"# QASystem-Using-LlamaIdex-and-Google_Gemini" 

Steps followed to develop this application : (Editor used - VSCODE)
1.  Initialized a git repository :(Names of folder written in .giignore are ignored)
git init
(Recommended : venv,.env  => This shouldn't be shared with others)

2.  Initially, Go to View -> Command Palette -> Python: Select Interpreter ->  Select ('base') environment
    eg : (base) C:\Users\jashw\Documents\BTECH CSE CORE\GenAI\QASystem>
    NOTE : Install Anaconda from https://www.anaconda.com/download

3.  Created a virtual environment : 
conda create -p venv python=3.9 -y

4. Activate the created virtual environment to manage usage of different packages
conda activate "path of venv folder"
eg : conda activate "C:\Users\jashw\Documents\BTECH CSE CORE\GenAI\QASystem\venv"

5.  Go to View -> Command Palette -> Python: Select Interpreter ->  Select Recommended environment
    eg : (c:\Users\jashw\Documents\BTECH CSE CORE\GenAI\QASystem\venv) C:\Users\jashw\Documents\BTECH CSE CORE\GenAI\QASystem>

6. Create a folder "notebook" -> Create a jupyter notebook "experiments.ipynb" => to run experiments or trial runs before proceeding to main application
    6.1 To run experiments,download the kernel:
        conda install ipykernel --update-deps --force-reinstall

7. Create a Google Gemini API key through : https://aistudio.google.com/u/2/apikey => Create API key, The API key is securely stored in .env file.

8. Create a .env file then store the Google Gemini API key(.env is a portable environment hidden file,used for storing for confidential information)

9. Check if all required packages are present in the current environment(Refer requirement.txt to meet the requirements of the project)
    #To check if a package is present in our environment use:
    pip list
    pip show packagename      (eg : pip show python dot-env)
    
10. Install all the packages and modules in the requirements.txt :
pip install -r requirements.txt

    Note: #To delete all the packages installed in the current environment :
          pip freeze > req.txt
          pip uninstall -r req.txt -y

11. Run all the experiments in notebook -> experiments.ipynb to get a good understanding of the application and its requirements

12. Create a file template.py with all files that the application needs
    eg : list of files:
        "QAWithContext/__init__.py",
        "QAWithContext/data_ingestion.py",
        "QAWithContext/embedding.py",
        "QAWithContext/model_api.py",
        "StreamlitApp.py",
        "setup.py",
        "exception.py",
13. Check logger.py and exception.py files and their working
14. Proceed with developing the actual application QAWithContext -> Configure data_ingestion.py,model_api.py and embedding.py
15. Install the required local packages for running files of QAWithContext, by running setup.py where a package named QAApplication_LlaamaIndex_GoogleGenAI is created
    python setup.py install
    #Upon running 15, build and QAApplication_LlaamaIndex_GoogleGenAI.egg-info folders are created
    Note : check if QAApplication_LlaamaIndex_GoogleGenAI is created using pip list
16. Finally, Configure and run Streamlit.py(which runs all the necessary imports from data_ingestion.py,model_api.py and embedding.py)
    streamlit run StreamlitApp.py
    NOTE : The model used in the project is a gemini free - tier model , model code : "gemini-2.5-flash-lite-preview-06-17"

The output looks something like this : 
  input(.txt) : Refer Data -> MLDOC.txt 
  #Preview of input : 
  ![image](https://github.com/user-attachments/assets/a0372931-54e6-4092-829d-2f3d3e755e34)

  #Upload this file here ,ask your query click on "submit & process" :
  ![image](https://github.com/user-attachments/assets/8d833b34-30a6-4b1d-9cb8-eb112899a5e6)

  #Preview of output :(based on MLDOC.txt)
  ![image](https://github.com/user-attachments/assets/88fa87f7-d9df-46e5-9b47-48ceebfe8e4a)

