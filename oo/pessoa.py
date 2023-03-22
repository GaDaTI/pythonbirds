class Pessoa:
    def __init__(self, nome= None):
        """
        Atributo de instaância :  Atributos usados para criação de um objeto.
        """
        self.nome = nome
    def cumprimentar(self):
        return  f'Como vai você?{id(self)}'

if __name__ == '__main__':
       p = Pessoa('Vascaino')
       print(Pessoa.cumprimentar(p))
       print("-"*100)
       print(id(p))
       print("-" * 100)
       print( p.cumprimentar())
       print("-" * 100)
       print("ATRIBUTO DE INSTÂNCIA")
       print(f"p.nome :  {p.nome}")
       print("-" * 100)
       p.nome = 'Gabriel Santana'
       print(f"p.nome :  {p.nome}")



