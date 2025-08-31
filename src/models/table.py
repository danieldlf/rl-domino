import networkx as nx # Lib de Grafos

from pydantic import BaseModel, ConfigDict

from .dorme import Dorme
from .stone import Stone

class Table(BaseModel):
    dorme: Dorme
    played_stones: nx.MultiGraph # Representação do jogo no formato de um grafo

    model_config = ConfigDict(arbitrary_types_allowed=True)