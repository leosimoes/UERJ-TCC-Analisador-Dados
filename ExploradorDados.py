#Autor: Leonardo Simões

import streamlit as st
import pandas as pd
import base64

class ExploradorDados:

    def __init__(self, df):
        self.df = df
        self.colunas_nao_float = df.select_dtypes(exclude=['float64']).columns.values
        self.colunas_qualitativas = df.select_dtypes(exclude=['number']).columns.values

    def descrever_colunas_qualitativas(self):
        # Descrevendo colunas qualitativas
        df_qualitativo = self.df[self.colunas_qualitativas]
        if len(df_qualitativo.columns) > 0:
            descricao_qualitativa = pd.DataFrame({'Coluna': df_qualitativo.columns,
                                                  'Tipo': df_qualitativo.dtypes,
                                                  'Valores Únicos': df_qualitativo.nunique(),
                                                  })
            descricao_qualitativa.reset_index(drop=True, inplace=True)
            st.subheader("Descrição das colunas não numéricas")
            st.table(descricao_qualitativa)
        else:
            st.write("O dataset não possui colunas qualitativas, todas são numéricas.")

    def descrever_colunas_quantitativas(self):
        # Descrevendo colunas numéricas (quantitativas)
        descricao_df = self.df.describe()
        descricao_df.index = ['quantidade', 'média', 'desvio padrao', 'mínimo', 'quartil 1 (25%)',
                              'mediana - quartil 2 (50%)', 'quartil 3 (75%)', 'máximo']
        st.subheader("Descrição de colunas numéricas")
        st.table(descricao_df)

    def contar_valores(self):
        st.markdown('### Contagem de valores por coluna')
        colunas_contagem = st.multiselect('Colunas para contagem de valores:', self.colunas_nao_float, default=None, key='cols_contagem')

        if colunas_contagem:
            for coluna in colunas_contagem:
                contagem = self.df[coluna].value_counts()
                contagem = contagem.to_frame().T
                contagem.index = ['Quantidade']
                st.markdown('#### Valores de ' + coluna)
                st.write(contagem)

    def realizar_query(self):
        st.markdown('### Consulta')
        st.markdown('A consulta deve ser feita comparando valores das colunas com algum valor constante. '
                    'Por exemplo: `A >= 1 & B == "outros"`. '
                    'Operadores relacionais são <, >, <=, >=, ==, <>. '
                    'Operadores lógicos são &, |.')
        query = st.text_input('Digite uma query para o dataframe', key='input_query')
        if query:
            try:
                df_query = self.df.query(query)
                st.dataframe(df_query)
                st.markdown(self.download_df_link(df_query), unsafe_allow_html=True)
            except:
                st.write('Query inválida')

    def agrupar(self):
        st.markdown('### Agrupamento')
        colunas_agrupamento = st.multiselect('Colunas para o agrupamento', self.colunas_nao_float, default=None, key='cols_agrumentp')
        if colunas_agrupamento:
            df_agrupado = self.df.groupby(colunas_agrupamento)
            descricao_df = df_agrupado.describe()
            colunas_descricao_1 = ['quantidade', 'média', 'desvio padrao', 'mínimo', 'quartil 1 (25%)',
                                   'mediana - quartil 2 (50%)', 'quartil 3 (75%)', 'máximo']
            descricao_df.columns.set_levels(colunas_descricao_1, level=1, inplace=True)
            st.subheader("Descrição de colunas numéricas")
            st.dataframe(descricao_df)

    def download_df_link(self, df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(
            csv.encode()
        ).decode()
        return f'<a href="data:file/csv;base64,{b64}" download="dataset_query.csv">Download do dataset resultante da consulta</a>'
