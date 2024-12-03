#IMPORTING PACKAGES
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
# from PIL import Image
import subprocess
import os
import base64
import pickle
import csv
import wget
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors


# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href


# Model Prediction(s)
def model(input_data):
    # Reads in saved regression model
    load_model = pickle.load(open('KNeighborsRegressor.m', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='IC50(nM)')
    molecule_name = pd.Series(load["Smiles"], name='molecule_name / SMILES')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

#CREATING MULTIPLE PAGES
selected = option_menu(
    menu_title=None,
    options=["Home", "Predictions", "Directions", "FAQs", "About us"],
    icons=["house", "list", "pencil", "question mark", "people"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#F0F2F6", "secondary-color": "3383FF"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "5px",
            "--hover-color": "C7FF33",
        },
        "nav-link-selected": {"background-color": "brown"},
        "options-selected": {"background-color": "brown"},
    },

)
if selected == "Home":
     #Logo image
     #image = Image.open('receptor.jpg')
     #image = img.resize((600, 400))
     #st.image(image, use_column_width=True)
     #st.image(image)
    st.title("CancerML")
    st.write(
        "CancerML predicts IC50 values of compounds against vascular endothelial growth factor receptor-2 (VEGFR-2). "
        "VEGFR-2 is a drug target implicated in many cancer forms like breast cancer, cervical cancer, colon cancer, oral cancer,"
        "ovarian cancer, pancreatic cancer, and prostate cancer. "
        "CancerML uses a deep neural regression model to predict Half maximal Inhihibtory concentrations with a mean absolute error"
        " of 0.0086 nM and a root mean squared error of 0.0254 nM using molecular fingerprints to facilitate selection of lead candidates"
        " towards experimental validation. "
        ".")
if selected == "FAQs":
    if st.button("what is CancerML?"):
        st.write("CancerML is a predictive app for predicting IC50s of compounds against VEGFR2")
    if st.button("How does CancerML work?"):
        st.write("CancerML makes use  of a deep neural network regression algorithm to make predictions")
    if st.button("How reliable are the predictions made by CancerML?"):
        st.write("Values of IC50s of compounds against VEGFR2 are reliable with a mean absolute error of 0.00867 nM")
    if st.button("What are the limitations of CancerML?"):
        st.write(
            "Like other ML algorithms, predictions on compounds not very similar to the training set are not very reliable")
    if st.button("who developed CancerML?"):
        st.write("CancerML is a product of the department of Biomedical engineering, University of Ghana.")

if selected == "Predictions":
    # im = Image.open('drug1.jpg')
    # image = image.resize(200, 100)
    #st.image(im, use_column_width=True)
    choice = st.sidebar.selectbox("Input Type", ["single compound", "multiple compounds"])
    # Sidebar
    # with st.sidebar.header('1. Upload your CSV data'):
    # uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['csv'])

    #CREATING INPUTS FOR SINGLE COMPOUNDS
    if choice == "single compound":
        # with st.header('Input SMILES'):
        with open('uploaded_file.csv', 'w+') as uploaded_file:
            file = csv.writer(uploaded_file)
            file.writerow(['Smiles', '1'])
            desc = st.sidebar.text_input("paste your compound's smiles and press Enter: ")
            file.writerow([desc, desc])
        # if st.sidebar.button("Example"):


    #CREATING INPUTS FOR MULTIPLE COMPOUNDS. INPUTS SHOULD BE IN CSV FORMAT
    elif choice == "multiple compounds":
        with st.sidebar.header('1. Upload your CSV data'):
            # uploaded_file = st.sidebar.file_uploader("Upload your input file", accept_multiple_files=True)
            uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['csv'])

    if st.sidebar.button('Predict'):
        try:

            # with open('uploaded_file.csv', 'r') as uploaded_file:
            # open(uploaded_file, 'r')
            load_data = pd.read_table(uploaded_file)
            load_data.to_csv('molecule.csv', sep='\t', header=True, index=False)
            load = pd.read_csv('molecule.csv')
            # load.to_csv('molecule.smi', sep='\t', header=False, index=False)
            # load_data.to_csv('molecule.smi', index=False)
            # molecule = pd.read_csv('molecule.smi')
        except:
            with open('uploaded_file.csv', 'r') as uploaded_file:
                load_data = pd.read_table(uploaded_file)
                load_data.to_csv('molecule.csv', sep='\t', index=False)
                load = pd.read_csv('molecule.csv')
                # load.to_csv('molecule.smi', sep='\t', header=False, index=False)
                # load_data.to_csv('molecule.smi', index=False)
                # molecule = pd.read_csv('molecule.smi')
        #COMPUTING MORGAN FINGERPRINTS
        with st.spinner("Calculating descriptors..."):
                def canonical_smiles(smiles):
                    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
                    smiles = [Chem.MolToSmiles(mol) for mol in mols]
                    return smiles
                Canon_SMILES = canonical_smiles(load.Smiles)
                def morgan_fpts(data):
                    Morgan_fpts = []
                    for i in data:
                        mol = Chem.MolFromSmiles(i)
                        fpts = AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048)
                        mfpts = np.array(fpts)
                        Morgan_fpts.append(mfpts)
                    return np.array(Morgan_fpts)
                Morgan_fpts = morgan_fpts(load['Smiles'])
                Morgan_fingerprints = pd.DataFrame(Morgan_fpts,
                                                   columns=['Col_{}'.format(i) for i in range(Morgan_fpts.shape[1])])
                Morgan_fingerprints.to_csv("mfprints.csv", index=False)

                descriptors = Morgan_fingerprints

                # st.write(desc)
                # st.write(desc.shape)

                # Read descriptor list used in previously built model
                st.header('**Molecular Fingerprints**')
                from sklearn.feature_selection import VarianceThreshold

               # try:

                    #def remove_low_variance(input_data, threshold=0.1):
                       # selection = VarianceThreshold(threshold)
                        #selection.fit(input_data)
                        #return input_data[input_data.columns[selection.get_support(indices=True)]]


                    #desc_subset = remove_low_variance(descriptors, threshold=0.1)
                    #desc_subset = desc_subset.iloc[:, 0:260]
                    #desc_subset.to_csv(index=False)
                #except:
                    #desc_subset = desc.iloc[:, 1:177]
                desc_subset = descriptors.iloc[:, 1:177]

        st.write(desc_subset)
        st.write(desc_subset.shape)

            # Apply trained model to make prediction on query compounds

        model(desc_subset)

    else:
        st.info('Upload input data in the sidebar to start!')
if selected == "Directions":
    st.title('**How to use this application**')
    st.write("1. Go to the 'Make Predictions' page and upload your input data in a csv format using the side bar.\n"
             "2. Press the 'predict' button on the side bar.\n "
             "3. The app will convert your input data into an smi file format, compute molecular descriptors and make"
             "predictions. \n"
             "4. The output file is in a csv format containing the compounds' names and corresponding IC50 values.\n "
             "5. You may now download the output file using the 'download' button. \n")
if selected == "About us":
    st.write(
        "This web application is the product of the department of Biomedical engineering, School of Engineering Sciences,"
        "College of Basic and Applied Sciences, University of Ghana. It was built under the supervision of Dr Samuel Kwofie.")
