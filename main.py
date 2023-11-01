#Autor: Leonardo Simões

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels
import base64

#import das classes criadas para analise dos dados
from ProcessamentoDados.ColetorDados import ColetorDados
from ProcessamentoDados.AvaliadorDados import AvaliadorDados
from ProcessamentoDados.LimpadorDados import LimpadorDados
from ProcessamentoDados.ExploradorDados import ExploradorDados
from ProcessamentoDados.GeradorGrafico import GeradorGrafico
from ProcessamentoDados.Regressor import Regressor

#Para executar o app: streamlit run main.py
if __name__ == '__main__':
    st.title('Aplicativo Web para exploração de dados')
    #st.info('Aplicação construída com Streamlit e Python.')
    st.markdown('*Autor: Leonardo Simões*')
    info1 = 'As etapas consideradas para a análise de dados são Aquisição, Avaliação, Limpeza, Análise Exporatória, Visualizações e Regressões. '
    info2 = 'Após o carregamento dos dados, as opções de visualizações e regressões desejadas devem ser marcadas na barra lateral. '
    st.markdown(info1 + info2)
    st.markdown('<hr/>', unsafe_allow_html=True)

    st.header('Aquisição dos dados')
    coletorDados = ColetorDados()
    coletorDados.verificar_rotulo()
    coletorDados.verificar_separador()
    arquivo = coletorDados.carregar_arquivo()

    if arquivo is not None:

        #DataFrame gerado a partir do arquivo do upload
        df = coletorDados.carregar_dados(arquivo)
        st.markdown('<hr/>', unsafe_allow_html=True)

        #Avaliação dos dados
        st.header('Avaliação dos dados')
        avaliadorDados = AvaliadorDados(df)
        avaliadorDados.exibir_head()
        avaliadorDados.exibir_dimensoes()
        avaliadorDados.exibir_colunas()
        avaliadorDados.exibir_linhas_duplicadas()
        avaliadorDados.exibir_colunas_valores_ausentes()
        avaliadorDados.exibir_informacoes_gerais()
        avaliadorDados.plotar_colunas_valores_ausentes()
        st.markdown('<hr/>', unsafe_allow_html=True)

        #Limpeza dos dados
        st.header('Limpeza dos dados')
        limpadorDados = LimpadorDados(df)
        limpadorDados.dropar_linhas_duplicadas()
        limpadorDados.dropar_colunas()
        limpadorDados.dropar_linhas()
        limpadorDados.preencher_colunas_media()
        limpadorDados.preencher_colunas_mediana()
        limpadorDados.preencher_colunas_zero()
        limpadorDados.preencher_colunas_minimo()
        limpadorDados.preencher_colunas_maximo()
        df_limpo = limpadorDados.get_dataframe_limpo()
        st.markdown(coletorDados.download_df_link(df_limpo), unsafe_allow_html=True)
        st.markdown('<hr/>', unsafe_allow_html=True)

        #Análise Exploratória dos dados
        st.header('Análise Exploratória dos dados')
        exploradorDados = ExploradorDados(df_limpo)
        exploradorDados.descrever_colunas_qualitativas()
        exploradorDados.descrever_colunas_quantitativas()
        exploradorDados.contar_valores()
        exploradorDados.agrupar()
        exploradorDados.realizar_query()
        st.markdown('<hr/>', unsafe_allow_html=True)

        #Visualização gráfica dos dados
        geradorGrafico = GeradorGrafico(df_limpo)

        st.sidebar.write('Gráficos')
        if st.sidebar.checkbox('Histogramas'):
            geradorGrafico.plotar_histogramas()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Barras'):
            geradorGrafico.plotar_barras()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Caixa (BoxPlot)'):
            geradorGrafico.plotar_boxplot()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Dispersão (pontos)'):
            geradorGrafico.plotar_dispersao()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Regressão Linear'):
            geradorGrafico.plotar_regressao_linear()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Regressão Logística'):
            geradorGrafico.plotar_regressao_logistica()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Pizza'):
            geradorGrafico.plotar_pizza()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Violino'):
            geradorGrafico.plotar_violino()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Barras Agrupadas 2 variáveis'):
            geradorGrafico.plotar_grafico_barras_agrupadas_2D()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Barras Agrupadas 3 variáveis'):
            geradorGrafico.plotar_grafico_barras_agrupadas_3D()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Pairplot'):
            geradorGrafico.plotar_pairplot()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Correlação'):
            geradorGrafico.plotar_correlacao()
            st.markdown('<hr/>', unsafe_allow_html=True)

        #Regressões Lineares e Logísticas
        regressor = Regressor(df_limpo)

        st.sidebar.write('Regressões')
        if st.sidebar.checkbox('Linear'):
            st.header('Regressão Linear')
            regressor.linear()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if st.sidebar.checkbox('Logística'):
            st.header('Regressão Logística')
            regressor.logistica()
            st.markdown('<hr/>', unsafe_allow_html=True)
