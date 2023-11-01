#Autor: Leonardo Simões

import streamlit as st
import pandas as pd

class LimpadorDados:

    def __init__(self, df):
        self.df = df.copy()

    #@st.cache(allow_output_mutation=True)
    def get_dataframe_limpo(self):
        return self.df

    def dropar_colunas(self):
        st.markdown('#### Exclusão de colunas')
        colunas_drop = st.multiselect('Colunas a serem excluídas: ', self.df.columns, default=None, key='cols_drop')
        if colunas_drop:
            self.df.drop(columns=colunas_drop, inplace=True)

    def dropar_linhas(self):
        st.markdown('#### Exclusão de linhas com valores ausentes')
        valores_na = self.df.isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values(ascending=False)
        colunas_na = valores_na.index.values
        colunas_linhas_drop = st.multiselect('Linhas a serem excluídas das colunas: ', colunas_na, default=None, key='cols_linhas_drop')
        if colunas_linhas_drop:
            self.df.dropna(subset=colunas_linhas_drop, inplace=True)

    def dropar_linhas_duplicadas(self):
        st.markdown('#### Exclusão de linhas duplicadas')
        if self.df.duplicated().sum() > 0:
            self.df.drop_duplicates(keep='first', inplace=True)
            st.write('As linhas duplicadas foram removidas.')
        else:
            st.write('Não há linhas duplicadas.')

    def preencher_colunas_media(self):
        st.markdown('#### Preenchimento de valores usando média da coluna')

        valores_na = self.df.select_dtypes(include=['number']).isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values(ascending=False)
        colunas_na = valores_na.index.values
        colunas_preencher_media = st.multiselect('Colunas numéricas a serem preenchidas com a média: ', colunas_na, default=None, key='cols_media')

        if colunas_preencher_media:
            for coluna in colunas_preencher_media:
                self.df[coluna].fillna(self.df[coluna].mean(), inplace=True)

    def preencher_colunas_mediana(self):
        st.markdown('#### Preenchimento de valores usando mediana da coluna')

        valores_na = self.df.select_dtypes(include=['number']).isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values(ascending=False)
        colunas_na = valores_na.index.values
        colunas_preencher_mediana = st.multiselect('Colunas numéricas a serem preenchidas com a mediana: ', colunas_na, default=None, key='cols_mediana')

        if colunas_preencher_mediana:
            for coluna in colunas_preencher_mediana:
                self.df[coluna].fillna(self.df[coluna].median(), inplace=True)

    def preencher_colunas_zero(self):
        st.markdown('#### Preenchimento de colunas com usando valor zero')

        valores_na = self.df.select_dtypes(include=['number']).isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values(ascending=False)
        colunas_na = valores_na.index.values
        colunas_preencher_zero = st.multiselect('Colunas numéricas a serem preenchidas com zero: ', colunas_na, default=None, key='cols_zero')

        if colunas_preencher_zero:
            for coluna in colunas_preencher_zero:
                self.df[coluna].fillna(0, inplace=True)

    def preencher_colunas_minimo(self):
        st.markdown('#### Preenchimento de colunas com seu menor valor')

        valores_na = self.df.select_dtypes(include=['number']).isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values(ascending=False)
        colunas_na = valores_na.index.values
        colunas_preencher_min = st.multiselect('Colunas numéricas a serem preenchidas com o mínimo: ', colunas_na, default=None, key='cols_min')

        if colunas_preencher_min:
            for coluna in colunas_preencher_min:
                self.df[coluna].fillna(self.df[coluna].min(), inplace=True)

    def preencher_colunas_maximo(self):
        st.markdown('#### Preenchimento de colunas com seu maior valor')

        valores_na = self.df.select_dtypes(include=['number']).isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values(ascending=False)
        colunas_na = valores_na.index.values
        colunas_preencher_max = st.multiselect('Colunas numéricas a serem preenchidas com o máximo: ', colunas_na, default=None, key='cols_max')

        if colunas_preencher_max:
            for coluna in colunas_preencher_max:
                self.df[coluna].fillna(self.df[coluna].max(), inplace=True)