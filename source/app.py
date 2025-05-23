'''
Home page for the Anasys Python Tools Streamlit app.

Run this file using `python -m streamlit run ./streamlit_app/app.py`
'''

import streamlit as st
from utils import setup_page, SessionStateSingleton   # pylint: disable=E0401

setup_page(streamlit_layout='centered')

if error := SessionStateSingleton().get_error_message():
    st.error(error, icon=':material/warning:')

st.title('AXZ File Viewer')

if SessionStateSingleton().get_anasys_doc() is not None:
    st.info('Click on a page in the sidebar to view the uploaded document', icon=':material/keyboard_double_arrow_left:')

st.write(
    '''
    This application is designed to view and analyse ruker/Anasys .axz files 
    (.axd and .irb files are also supported), without using Anasys Studio software. 
    This enables everyone to view and analyse the data, even without access to a 
    nanoIR microscope.

    The app is divided into several pages, accessible via the sidebar on the left. 
    The pages are as follows:

    1. **Optical Images.** View all optical images in the document, and correlate
    these with measurement locations of maps and spectra.  
    2. **Map Overview.** Quickly view all maps in the document and access all 
    metadata associated with each map.
    3. **Map QC.** Offers a quality control report for all maps in the document, 
    grouped by time of acquisition. This is useful for checking the quality of the 
    raw map data. The app performs some automatic checks of data quality and will 
    warn the user if it finds any possible issues. It is possible to generate a 
    PDF report of the QC data. 
    4. **Spectra.** View all spectra in the document, and access metadata 
    associated with each spectrum. Like maps, a QC report can be generated and 
    possible issues with data quality are highlighted. Spectra can also be exported
    as a CSV file for further processing.
    '''
)
