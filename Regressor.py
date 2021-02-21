#Autor: Leonardo Simões

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

class Regressor:

    def __init__(self, df):
        self.df = df.select_dtypes(include=['number']).dropna()
        self.colunas = self.df.columns.values

    def linear(self):
        X = st.multiselect('X', self.colunas, default=None, key='x_reglinear')
        y = st.selectbox('y', self.colunas, key='y_reglinear')
        if st.button('Treinar Regressão Linear'):
            if X:
                if y:
                    #Treinando o modelo de regressão
                    reg = LinearRegression()
                    reg.fit(self.df[X], self.df[[y]])
                    st.write('Score do treinamento: ' + str(round(reg.score(self.df[X], self.df[[y]]),3)))
                    #Formatando coeficientes para impressao
                    coeficientes_valores = np.append(reg.coef_, reg.intercept_)
                    coeficientes_df = pd.DataFrame(coeficientes_valores).T
                    coeficientes_nomes = X.copy()
                    coeficientes_nomes.append('constante')
                    coeficientes_df.columns = coeficientes_nomes
                    coeficientes_df.index = ['Coeficientes']
                    st.table(coeficientes_df)


    def logistica(self):
        colunas_binarias = [c for c in self.df if sorted(list(self.df[c].value_counts().index)) == ([0, 1])]

        X = st.multiselect('X', self.colunas, default=None, key='x_reglogistica')
        y = st.selectbox('y', colunas_binarias, key='y_reglogistica')
        if st.button('Treinar Regressão Logística'):
            if X:
                if y:
                    # Treinando o modelo de regressão
                    clf = LogisticRegression(random_state=0)
                    clf.fit(self.df[X], self.df[[y]])
                    st.write('Score do treinamento: ' + str(round(clf.score(self.df[X], self.df[[y]]),3)))
                    #Formatando coeficientes para impressao
                    coeficientes_valores = np.append(clf.coef_, clf.intercept_)
                    coeficientes_df = pd.DataFrame(coeficientes_valores).T
                    coeficientes_nomes = X.copy()
                    coeficientes_nomes.append('constante')
                    coeficientes_df.columns = coeficientes_nomes
                    coeficientes_df.index = ['Coeficientes']
                    st.table(coeficientes_df)