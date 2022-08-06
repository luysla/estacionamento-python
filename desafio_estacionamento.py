class Estacionamento:
    def __init__(self, carro_para_vaga, moto_para_vaga):
        self.vagas_de_carro = 0;
        self.vagas_de_moto = 0;
        self.carro_para_vaga = carro_para_vaga;
        self.moto_para_vaga = moto_para_vaga;
        self.total_vagas_livres_carro = 5;
        self.total_vagas_livres_moto = 5;
    
    def estacionar_carro(self):
        if self.vagas_de_carro == 0:
            print('Estacionamento sem vagas disponíveis')
        else:
            self.vagas_de_carro -= 1;

    def estacionar_moto(self):
        if self.vagas_de_moto == 0:
            print('Estacionamento sem vagas disponíveis')
            if self.vagas_de_carro > 0:
                self.vagas_de_carro -= 1;
        else:
            self.vagas_de_moto -= 1;
    
    def remover_carro(self):
        self.vagas_de_carro += 1;
    
    def remover_moto(self):
        self.vagas_de_moto += 1;
    
    def estado_do_estacionamento(self):
        print(f'Estado do estacionamento \n Vagas livres para carros: {self.total_vagas_livres_carro} \n Vagas livres para motos: {self.total_vagas_livres_moto}')

    def __str__(self) -> str:
        return f'Informações - Estacionamento \n Vagas livres para carros: {self.total_vagas_livres_carro} \n Vagas livres para motos: {self.total_vagas_livres_moto}'

class Vaga:
    def __init__(self, idVaga, tipo, placa):
        self.idVaga = idVaga;
        self.tipo = tipo;
        self.livre = True;
        self._placa = placa;
    
    def ocuparVaga(self):
        self.livre = False;
        print(f'A vaga {self.id} está ocupada')
    
    def desocuparVaga(self):
        self.livre = True;
        print(f'A vaga {self.id} está livre')
    
class TipoVeiculo:
    def __init__(self, tipo, placa):
        self.tipo = tipo
        self._placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True
        print(f'{self.tipo} está estacionado')
    
    def sair_da_vaga(self):
        self.estacionado = False
        print(f'{self.tipo} saiu da vaga')
    
    def __str__(self) -> str:
        return f'Informações - Tipo de Veículo \nTipo: {self.tipo} \nPlaca: {self._placa} \nEstacionado: {self.estacionado}'

class Carro(TipoVeiculo):
    def __init__(self, tipo, placa):
        super().__init__(tipo, placa)
    
    def __str__(self) -> str:
        return f'Informações - Carro \nTipo: {self.tipo} \nPlaca: {self._placa} \nEstacionado: {self.estacionado}'

class Moto(TipoVeiculo):
    def __init__(self, tipo, placa):
        super().__init__(tipo, placa)
    
    def __str__(self) -> str:
        return f'Informações - Moto \nTipo: {self.tipo} \nPlaca: {self._placa} \nEstacionado: {self.estacionado}'

carro1 = Carro('Carro', '6F5FXM')
carro2 = Carro('Carro', 'MDRO4O')

moto1 = Moto('Moto', '58J9ND')
moto2 = Moto('Moto', 'JCE29L') 

vagas = [];





    
    


