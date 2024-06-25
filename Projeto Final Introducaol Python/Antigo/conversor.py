class Conversor:
  def __init__(self):
    self.unidade_medida = None
    self.unidade_para = None
    self.valor = 0

  def mudar_medidas(self, medida_1, medida_2):
      self.unidade_medida = medida_1
      self.unidade_medida = medida_2
                       
  def cm_m_km(self):
    match (self.unidade_medida, self.unidade_para):
        case ('cm', 'm'):
            return self.valor / 100
        case ('cm', 'km'):
            return self.valor / 100000
        case ('m', 'cm'):
            return self.valor * 100
        case ('m', 'km'):
            return self.valor / 1000
        case ('km', 'cm'):
            return self.valor * 100000
        case ('km', 'm'):
            return self.valor * 1000
        case _:
            print("Erro, conversão não suportada entre as medidas fornecidas!")
            return None
        
  def configurar_valor(self, valor):
        self.valor = valor      
 
  """            
  def mg_g_kg(self):
       match (self.unidade_medida, self.unidade_para):
            case ('kg', 'g'):
                return self.valor * 1000
            case ('kg', 'mg'):
                return self.valor * 1000000
            case ('g', 'kg'):
                return self.valor / 1000
            case ('g', 'mg'):
                return self.valor * 1000
            case ('mg', 'kg'):
                return self.valor / 1000000
            case ('mg', 'g'):
                return self.valor / 1000
            case _:
                print("Erro, conversão não suportada entre as medidas fornecidas!")
                return None
           
  def conversor_segundos(self,unidade_medida , valor):
        match unidade_medida:
            case 'segundos' | 'segundo':
                return valor
            case 'minutos' | 'minuto':
                return valor * 60
            case 'horas' | 'hora':
                return valor * 3600
            case 'dias' | 'dia':    
                return valor * 86400
            case 'semanas' | 'semana':    
                return valor * 604800
            case 'meses' | 'mes':
                return valor * 2629746 
            case 'anos' | 'ano':
                return valor * 31556952  
            case _:
                return None"""




     