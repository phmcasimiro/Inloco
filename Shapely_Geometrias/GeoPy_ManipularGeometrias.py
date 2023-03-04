# Importar biblioteca shapely
# shapely - biblioteca de manipulação de geometrias (ponto, linha e polígono)
# caso a biblioteca não esteja instalada no ambiente virtual do Python, haverá um aviso e será necessário instalar com "!pip install"
import shapely

# "!pip install" usado para instalar bibliotecas
# "-q" usado para não exibir as informações de atualização da biblioteca que esta sendo instalada
!pip install shapely -q

# Importar geometrias simples, ou seja, um ponto, linha ou poligono usados para representar um objetos do mundo real
# Exemplo: cada ilha de um arquipélago é interpretado pelo computador como um único ponto
from shapely.geometry import Point, LineString, Polygon

# Importar geometrias múltiplas, ou seja, vários pontos, linhas ou polígonos para representar um conjunto de objetos do mundo real com o mesmo nome
# Exemplo: Estado do Rio de Janeiro é representando por uma geometria multipolygon porque o territorio continental e as ilhas fazem parte do mesmo objeto 
from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon, box 

# Criar variáveis do tipo ponto e atribuindo coordenadas
p1 = Point(5.4,3.0)
p2 = Point(10,-7)
p3 = Point(80,25)
p3D = Point(5.4,3.0,0.25) # Variável do tipo ponto com coordenadas X, Y e Z