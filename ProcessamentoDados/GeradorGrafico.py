#Autor: Leonardo Simões

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels

class GeradorGrafico:

    def __init__(self, df):
        self.df = df
        self.colunas_numericas = df.select_dtypes(include=['number']).columns.values
        self.colunas_float = df.select_dtypes(include=['float64']).columns.values
        self.colunas_nao_float = df.select_dtypes(exclude=['float64']).columns.values
        self.colunas_binarias = [c for c in self.df[self.colunas_numericas] if
                            sorted(list(self.df[c].value_counts().index)) == ([0, 1])]

    def plotar_histogramas(self):
        st.markdown('### Histogramas')
        colunas_histogramas = st.multiselect('Colunas númericas decimais: ', self.colunas_float, default=None, key='x_histograma')

        if colunas_histogramas:
            for coluna in colunas_histogramas:
                fig = plt.figure(figsize=(13, 9))
                ax = sns.histplot(x=self.df[coluna], kde=True)
                ax.set_title('Distribuição de ' + coluna)
                ax.set_ylabel('Quantidade')
                ax.set_xlabel(coluna.capitalize())
                st.pyplot(fig)

    def plotar_barras(self):
        st.markdown('### Gráficos de Barras')
        colunas_barras = st.multiselect('Colunas qualitativas ou discretas:', self.colunas_nao_float, default=None, key='x_barras_1D')

        if colunas_barras:
            for coluna in colunas_barras:
                color = sns.color_palette("Blues_d")
                fig = plt.figure(figsize=(13, 9))
                ax = sns.countplot(x=self.df[coluna], palette=color)
                ax.set_title('Distribuição de ' + coluna)
                ax.set_ylabel('Quantidade')
                ax.set_xlabel(coluna.capitalize())
                st.pyplot(fig)

    def plotar_boxplot(self):
        st.markdown('### Diagramas de Caixa (Boxplots)')
        colunas_boxplot = st.multiselect('Colunas numéricas:', self.colunas_numericas, default=None, key='x_boxplot')

        if colunas_boxplot:
            for coluna in colunas_boxplot:
                fig = plt.figure(figsize=(13, 9))
                ax = sns.boxplot(x=self.df[coluna])
                ax.set_title('Distribuição de ' + coluna)
                ax.set_xlabel(coluna.capitalize())
                st.pyplot(fig)

    def plotar_dispersao(self):
        st.markdown('### Gráficos de Dispersão')
        colunas_scatter_x = st.multiselect('Colunas para o eixo X:', self.colunas_numericas, default=None, key='x_dispersao')
        colunas_scatter_y = st.multiselect('Colunas para o eixo Y:', self.colunas_numericas, default=None, key='y_dispersao')

        if colunas_scatter_x:
            if colunas_scatter_y:
                for eixo_x in colunas_scatter_x:
                    for eixo_y in colunas_scatter_y:
                        fig = plt.figure(figsize=(13, 9))
                        ax = sns.scatterplot(x=self.df[eixo_x], y=self.df[eixo_y])
                        ax.set_title(eixo_x.capitalize() + ' X ' + eixo_y.capitalize())
                        ax.set_ylabel(eixo_y.capitalize())
                        ax.set_xlabel(eixo_x.capitalize())
                        st.pyplot(fig)

    def plotar_regressao_linear(self):
        st.markdown('### Gráficos de Regressão Linear')
        colunas_regressao_x = st.multiselect('Colunas para o eixo X:', self.colunas_numericas, default=None, key='x_reg_linear')
        colunas_regressao_y = st.multiselect('Colunas para o eixo Y:', self.colunas_numericas, default=None, key='y_reg_linear')

        if colunas_regressao_x:
            if colunas_regressao_y:
                for eixo_x in colunas_regressao_x:
                    for eixo_y in colunas_regressao_y:
                        fig = plt.figure(figsize=(13, 9))
                        ax = sns.regplot(x=self.df[eixo_x], y=self.df[eixo_y], ci=0, line_kws={"color": "red"})
                        ax.set_title(eixo_x.capitalize() + ' X ' + eixo_y.capitalize())
                        ax.set_ylabel(eixo_y.capitalize())
                        ax.set_xlabel(eixo_x.capitalize())
                        st.pyplot(fig)

    def plotar_regressao_logistica(self):
        st.markdown('### Gráficos de Regressão Logística')
        colunas_regressao_x = st.multiselect('Colunas para o eixo X:', self.colunas_numericas, default=None, key='x_reg_log')
        colunas_regressao_y = st.multiselect('Colunas para o eixo Y:', self.colunas_binarias, default=None, key='y_reg_log')

        if colunas_regressao_x:
            if colunas_regressao_y:
                for eixo_x in colunas_regressao_x:
                    for eixo_y in colunas_regressao_y:
                        fig = plt.figure(figsize=(13, 9))
                        ax = sns.regplot(x=self.df[eixo_x], y=self.df[eixo_y], logistic=True, ci=0, line_kws={"color": "red"})
                        ax.set_title(eixo_x.capitalize() + ' X ' + eixo_y.capitalize())
                        ax.set_ylabel(eixo_y.capitalize())
                        ax.set_xlabel(eixo_x.capitalize())
                        st.pyplot(fig)

    def plotar_pizza(self):
        st.markdown('### Gráficos de Pizza')
        colunas_chart = st.multiselect('Colunas não decimais:', self.colunas_nao_float, default=None, key='p_pizza')

        if colunas_chart:
            for coluna in colunas_chart:
                counts = self.df[coluna].value_counts()
                fig, ax = plt.subplots(figsize=[13, 9])
                ax.pie(counts, labels=counts.index,
                       startangle=90, counterclock=False, autopct='%1.2f%%')
                ax.set_title('Distribuição de ' + coluna.capitalize())
                st.pyplot(fig)

    def plotar_violino(self):
        st.markdown('### Gráficos de Violino')
        colunas_violino_x = st.multiselect('Colunas para o eixo X:', self.colunas_nao_float, default=None, key='x_violino')
        colunas_violino_y = st.multiselect('Colunas para o eixo Y:', self.colunas_float, default=None, key='y_violino')

        if colunas_violino_x:
            if colunas_violino_y:
                for eixo_x in colunas_violino_x:
                    for eixo_y in colunas_violino_y:
                        fig = plt.figure(figsize=(13, 9))
                        ax = sns.violinplot(x=self.df[eixo_x], y=self.df[eixo_y], inner='quartile')
                        ax.set_title(eixo_x.capitalize() + ' X ' + eixo_y.capitalize())
                        ax.set_ylabel(eixo_y.capitalize())
                        ax.set_xlabel(eixo_x.capitalize())
                        st.pyplot(fig)

    def plotar_pairplot(self):
        st.markdown('### Pairplot')
        colunas_pairplot = st.multiselect('Colunas númericas: ', self.colunas_numericas, default=None, key='xy_pairplot')

        if colunas_pairplot:
            pairplot = sns.pairplot(self.df[colunas_pairplot])
            st.pyplot(pairplot)

    def plotar_correlacao(self):
        st.markdown('### Mapa de calor das correlações')
        corrMatrix = self.df.corr()
        fig = plt.figure(figsize=(13, 9))
        ax = sns.heatmap(corrMatrix, annot=True)
        ax.set_title('Gráfico de calor de correlações das variáveis')
        st.pyplot(fig)

    def plotar_grafico_barras_agrupadas_2D(self):
        st.markdown('### Gráficos de Barras Agrupadas com 2 variáveis')
        colunas_barras_x = st.multiselect('Colunas para o eixo X', self.colunas_nao_float, default=None, key='x_barras_2D')
        colunas_barras_z = st.multiselect('Colunas para legenda', self.colunas_nao_float, default=None, key='z_barras_2D')

        if colunas_barras_x:
            if colunas_barras_z:
                for eixo_x in colunas_barras_x:
                    for eixo_z in colunas_barras_z:
                        fig = plt.figure(figsize=(13, 9))
                        ax = sns.countplot(x=self.df[eixo_x], hue=self.df[eixo_z])
                        ax.legend(loc=8, ncol=3, framealpha=1, title=eixo_z)
                        ax.set_title('Quantidade de ' + eixo_x.capitalize() + ' e ' + eixo_z.capitalize())
                        ax.set_ylabel('Quantidade')
                        ax.set_xlabel(eixo_x.capitalize())
                        st.pyplot(fig)

    def plotar_grafico_barras_agrupadas_3D(self):
        st.markdown('### Gráficos de Barras Agrupadas com 3 variáveis')
        colunas_barras_y = st.multiselect('Colunas para o eixo Y', self.colunas_float, default=None, key='y_barras_3D')
        colunas_barras_x = st.multiselect('Colunas para o eixo X', self.colunas_nao_float, default=None, key='x_barras_3D')
        colunas_barras_z = st.multiselect('Colunas para legenda', self.colunas_nao_float, default=None, key='z_barras_3D')

        if colunas_barras_x:
            if colunas_barras_z:
                if colunas_barras_y:
                    for eixo_x in colunas_barras_x:
                        for eixo_z in colunas_barras_z:
                            for eixo_y in colunas_barras_y:
                                fig = plt.figure(figsize=(13, 9))
                                ax = sns.barplot(x=self.df[eixo_x], y=self.df[eixo_y], hue=self.df[eixo_z])
                                ax.legend(loc=8, ncol=3, framealpha=1, title=eixo_z)
                                ax.set_title(eixo_y.capitalize() + ' por ' + eixo_x.capitalize() + ' e ' + eixo_z.capitalize())
                                ax.set_ylabel(eixo_y.capitalize())
                                ax.set_xlabel(eixo_x.capitalize())
                                st.pyplot(fig)