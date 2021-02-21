#Autor: Leonardo Simões

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AvaliadorDados:
    
    def __init__(self, df):
        self.df = df

    def exibir_head(self):
        # Exibindo o cabeçalho e as primeiras linhas do dataframe
        st.write('O cabeçalho e as primeiras linhas do dataset são: ')
        st.dataframe(self.df.head(10))

    def exibir_dimensoes(self):
        # Exibindo as dimensões do dataframe
        dimensoes = 'As dimensões do dataset são ' + str(self.df.shape[0]) + ' linhas e ' + str(self.df.shape[1]) + ' colunas.'
        st.write(dimensoes)

    def exibir_colunas(self):
        # Exibindo nomes das colunas
        colunas_originais = ', '.join(list(self.df.columns))
        st.write('As colunas são: ' + colunas_originais + '.')

    def exibir_linhas_duplicadas(self):
        # Verificando linhas duplicadas
        duplicadas = self.df.duplicated().sum()
        st.write('A quantidade de linhas duplicadas é ' + str(duplicadas) + '.')

    def exibir_informacoes_gerais(self):
        # Exibindo informações gerais do dataframe
        valores_na = self.df.isna().sum()
        informacoes = pd.DataFrame({'Coluna': self.df.columns,
                                    'Tipo': self.df.dtypes,
                                    'Valores Ausentes': valores_na,
                                    'Percentual Faltante': valores_na / self.df.shape[0]
                                    })
        informacoes.reset_index(drop=True, inplace=True)
        informacoes['Percentual Faltante'] = informacoes['Percentual Faltante'].round(3)
        st.subheader("Informações gerais das colunas")
        st.table(informacoes)
        del informacoes

    def exibir_colunas_valores_ausentes(self):
        # Verificando colunas com valores ausentes
        valores_na = self.df.isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values(ascending=False)

        if not valores_na.empty:
            colunas_na = ', '.join(valores_na.index.values)
            st.write('As colunas com valores ausentes são: ' + colunas_na + '.')
        else:
            st.write('Não há colunas com valores ausentes')

    def plotar_colunas_valores_ausentes(self):
        # Verificando colunas com valores ausentes
        valores_na = self.df.isna().sum()
        valores_na = valores_na[valores_na > 0].sort_values()

        if not valores_na.empty:
            # Plotando gráfico de barras para valores ausentes
            #st.markdown('### Valores ausentes por coluna')
            na_fig, na_plot = plt.subplots(figsize=(12, 8))
            na_plot.barh(valores_na.index, valores_na.values)
            na_plot.set_title('Valores ausentes por coluna')
            na_plot.set_xlabel('Quantidade de valores ausentes')
            na_plot.set_ylabel('Colunas')
            st.pyplot(na_fig)