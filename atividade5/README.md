## Lista de Exercícios 5

### Utilizando o Apache Spark e demais ferramentas correlatas, implemente os seguintes passos:

1. Selecione um estado brasileiro e dez de suas cidades. Crie um CSV para
armazenar as cidades, com id (nome da cidade), latitude, longitude e
população. Crie outro CSV para armazenar a distância entre essas cidades,
com src, dst e relationship como campos (adicione pelo menos 30 registros
nesse arquivo).
2. Utilizando as bibliotecas do Spark, crie um objeto GraphFrame a partir
desses dois CSVs.
3. Utilizando o método bfs (Breadth First Search), execute 5 filtragens a sua
escolha.
4. Execute 2 consultas utilizando o método find.
5. Execute 2 consultas utilizando o método filterVertices.
6. Implemente uma rotina que, recebendo como entrada um objeto
GraphFrame, percorra todos os vértices do grafo com o algoritmo da busca
em profundidade.

Referências:

<https://realpython.com/pyspark-intro/>

<https://graphframes.github.io/graphframes/docs/_site/user-guide.html>