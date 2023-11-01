#Autor: Leonardo Simões

import streamlit as st
import pandas as pd
import base64

class ColetorDados:
    def __init__(self):
        self.sem_rotulos = False
        self.separador = ','

    def verificar_rotulo(self):
        if st.checkbox('O arquivo não possui rótulos para colunas na primeira linha'):
            self.sem_rotulos = True

    def verificar_separador(self):
        sep_dict = {'vírgula': ',', 'ponto e vírgula': ';', 'um espaço': ' ','tabulação':'\t'}
        sep = st.selectbox('Selecione o separador usado no arquivo', list(sep_dict.keys()))
        if sep:
            self.separador = sep_dict[sep]

    def carregar_arquivo(self):
        return st.file_uploader('Upload de arquivo csv, tsv ou txt:', type=['csv','tsv','txt'])

    @st.cache_data
    def carregar_dados(_self, arquivo):
        if _self.sem_rotulos:
            df = pd.read_csv(arquivo, sep=_self.separador, header=None)
            df.columns = ['x' + str(i) for i in range(1, df.shape[1] + 1)]
            return df
        else:
            df = pd.read_csv(arquivo, sep=_self.separador)
            lowercase = lambda x: str(x).lower()
            df.rename(lowercase, axis='columns', inplace=True)
            return df

    def download_df_link(self, df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(
            csv.encode()
        ).decode()
        return f'<a href="data:file/csv;base64,{b64}" download="dados_limpos.csv">Download do dataset limpo</a>'

