# Analisador de Dados

Autor: Leonardo Simões

Trabalho de conclusão de curso (TCC) em Engenharia de Computação pela UERJ. 

Leia também o [texto do projeto](https://github.com/leosimoes/UERJ-TCC-Analisador-Dados-Texto).

Aplicativo Web para análise de dados de forma interativa e semiautomatizada, de 
modo que, facilite o processo e possa ser realizada por uma pessoa sem conhecimentos em programação, 
e sem necessidade de instalar algum software.


## Ambiente de programação

A aplicação foi construída usando a linguagem Python 3.8 e seus módulos:

* streamlit: 1.28.0
* numpy: 1.26.1
* pandas: 2.1.2
* matplotlib: 3.3.2
* seaborn: 0.13.0
* scikit-learn: 1.3.2
* scipy: 1.11.3


## Execução 

Para executar a aplicação localmente: após baixa-lá, configurar a venv (ambiente virtual) e instalar as dependências, 
use o terminal no diretório da aplicação e use o comando `streamlit run main.py`. 

Para acessar a aplicação hospedada no Streamlit Community Cloud: 
[Link](https://leosimoes-tcc.streamlit.app/)


## Fluxo

O fluxo de análise de dados adotada neste trabalho foi definido pelas etapas de aquisição de dados, avaliação dos dados, 
limpeza dos dados, análise exploratória dos dados, visualização dos dados e regressão. 
Este fluxo geralmente é linear, mas para as etapas após a de limpeza, pode haver um retorno para uma das etapas anteriores até a de limpeza.

![fluxo da análise de dados](./imagens/FluxoAplicacao.jpg)


## Diagrama de Classes

![Diagrama de Classes](./imagens/DiagramaDeClasses.jpg)
