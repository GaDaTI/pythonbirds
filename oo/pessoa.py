class Pessoa:
    def cumprimentar(self):
        return  f'Como vai você?{id(self)}'

if __name__ == '__main__':
       p = Pessoa()
       print(Pessoa.cumprimentar(p))
       print("-"*100)
       print(id(p))
       print("-" * 100)
       print( p.cumprimentar())
       print("-" * 100)


