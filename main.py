from sqlalchemy import create_engine, Column, Integer,String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

#criar a classe base do ORM 
base = declarative_base()

class usuario(base):
    #definir o nomeda tabela
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)

    nome = Column(String(100), nullable=True)

    email = Column(String(100), nullable=True, unique=True)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)
    salario = Column (Float)

    def __init__(self, nome, email, idade, salario):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.salario = salario
        


engine = create_engine("sqlite:///empresa.db")

base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

with Session() as session:
    try:
        usuario_existente = session.query(usuario).filter_by(email="Eduardo@gmail.com").first()
        if usuario_existente == None:
            #criar um objeto
            usuario1 = usuario("Eduardo","Eduardo@gmail.com", 33, 5000)
            session.add(usuario1)
            print("usuario cadastrado com sucesso")
        else:
            print("já existe um cadastro com esse e-mail")
        
    except Exception as erro:
        session.rollback()
        print(f"Ocorreu um erro {erro}")