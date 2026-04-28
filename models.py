
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(150))
    
    produtos = relationship("Produto", back_populates="categoria")

    def __repr__(self):
        return f"Categoria| ID: {self.id} | Nome: {self.nome} | Descrição: {self.descricao}"
    

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    
    categoria = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto| ID: {self.id} | Nome: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque}"