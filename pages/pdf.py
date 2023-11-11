import streamlit as st
import base64

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Use JavaScript to set the height dynamically based on the content
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" style="border: none;" id="pdf_iframe"></iframe>
    <script>
        var pdfIframe = document.getElementById('pdf_iframe');
        pdfIframe.onload = function() {{
            pdfIframe.style.height = pdfIframe.contentWindow.document.body.scrollHeight + 'px';
        }};
    </script>
    """
    
    st.write(pdf_display, unsafe_allow_html=True)


show_pdf('2023-10-09-lv-tulx.pdf')


