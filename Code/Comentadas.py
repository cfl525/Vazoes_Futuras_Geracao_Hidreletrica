# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:47:40 2022

@author: E805511


DESCARTADAS...
"""

#%% FILTRANDO AS DATAS

# def filtro_datas():
#     """Filtragem por um intervalo de anos."""
#     #serie1 = df_end.query('ANOS==2020'&'POSTO==74')
#     #serie2 = df_end[(df_end['ANOS']=='2020')]
#     serie3 = df_end.query('ANOS=="2020"')
#     return serie3

# a = filtro_datas()

# def selecao_datas():
#     """Selecionando as datas."""
#     #filtro = (df_end['ANOS']>'2020') & (df_end['ANOS']<='2021')
#     #selecao = teste_usinas.loc[2002:2003]
#     #selecao1 = df_end["ANOS"].isin(pd.date_range(start='2020', end='2021'))
#     selecao2 = teste_usinas[teste_usinas.columns[3:12]]
#     #teste_usinas.loc[1:3, selecao2]
#     return selecao2


# a1 = selecao_datas()

#%% PLOT



# #Definir x e y
#sns.scatterplot(data = df_end, x='name1', y='name2')



#%% MANEIRAS DE ORGANIZAR AS INFORMAÇÃO
#Para separar por período do ano como abr/2022 a mar/2023
#E poder calcular o coeficiente de Pearson com as colunas geradas

# def reshape(inf, sup, data):
#     """Criando a própria função."""
#     return [float(i) for i in data.iloc[inf:sup,:].values]

# pd.DataFrame({'A': reshape(0,10, obs) ,'B': reshape(10,20, obs), 
#               'C': reshape(20,30, obs), 'D': reshape(30,40, obs)}, index = range(10))


# #Refatoração da função acima
# pd.DataFrame(obs.values.reshape(-1, 10).T, columns=['A','B', 'C', 'D'])


#teste_usinas2 = df_end.groupby("POSTO").indices('POSTO' -> '74', '275')


# %% Fabiano

# df_end_1.set_index('ANO_INI', append=True, inplace=True)
# df_end_2.set_index('ANO_FIM', append=True, inplace=True)



# df_final = pd.concat([df_end_1, df_end_2], axis="columns")
#df_final['ANO_INI'].astype(str)


#%% main

# if __name__ == '__main__':
#     def main():
#         """Parâmentros por linha de comando.
#         1 - código da usina
#         2 - Caminho do arquivo vazoes.dat
#         3 - Quantos meses a serem preenchidos
#         """
#         pass



#%% CÁLCULO

# nova linha: 2022-2023 com os dados do comparativo da correlação
# para todas as usinas



#Interando entre linhas

#Percorrendo pelas colunas
#iteritems - key=colunas
# for i, values_geracao in b.iterrows():
#     ultimo_ano = values_geracao
#     #inserir a correlação
    


r_pearson = []
#r_pearson.append()

# r_series = pd.Series(r_pearson, 
#                      name='Correlação',
#                      index=None)

#Organizando
# r_series.sort_values()

#Pegar o primeiro índice da série e relacionar com índice do DataFrame auxiliar.



# for i in b.itertuples():
#     print(i)


#------------------------------------------------------------------------------

# def selecionar_multi_usinas(usinas: list):
#     """
#     Digite o código das usinas em uma lista.
    
#     Exemplo:
#        iusi = selecionar_multi_usinas([6, 74, 169, 275])
#     """
#     lista_usinas = usinas
#     usinas_selec = df_final[df_final.index.isin(lista_usinas)]
#     return usinas_selec


# c = selecionar_multi_usinas([6, 74, 169, 275])

# %% PLOT

# sns.heatmap(correlacao,
#             #cmap='ocean',
#             annot=True,
#             linewidths=0.5)

# sns.heatmap(correlacao1,
#             cmap='GnBu_r',
#             annot=True,
#             linewidths=0.5)


#%% CORRELAÇÃO DE PEARSON E MANIPULAÇÃO DE DADOS
# =============================================================================
# pivot2 = df_end.pivot_table(index = ['ANOS', 'POSTO'],
#                             )
# correlacao = df_end.corr(method='pearson')

# teste_usinas = df_final.groupby("POSTO").get_group(74)
# correlacao1 = b.corr(method='pearson')
