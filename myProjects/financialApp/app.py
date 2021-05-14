from utils import database


def prompt_add_investment():
    ativo = input('Nome do ativo: ').upper()
    numero_cotas = int(input('Número de cotas compradas: '))
    valor_cota = float(input('Valor pago por cota: '))
    data = input('Data da compra (DIA-MÊS-ANO): ')
    database.add_investment(ativo, numero_cotas, valor_cota, data)


def list_all_investments():
    investments = database.get_all_investments()
    for invest in investments:
        print(f"ID: {invest['id']}, Ativo: {invest['ativo']}, N° Cotas: {invest['numero_cotas']}, Valor/Cota: {invest['valor_cota']}, Data: {invest['data']}")


def prompt_delete_investment():
    id = input('ID da transação que deseja exlcuir: ')
    database.delete_investment(id)


def organize_by_value_invested():
    investments = database.get_all_investments()
    # Dictonary with name and value invested
    name_value_dict = [{'ativo': invest['ativo'],
                        'valor_investido': round(invest['numero_cotas']*invest['valor_cota'], 2)}
                       for invest in investments]
    # Sorting in descending way
    name_value_dict.sort(reverse=True, key=lambda x: x.get(
        'valor_investido'))
    # Geting the total invested
    values = [invest['valor_investido'] for invest in name_value_dict]
    total_invested = sum(values)
    # Printing
    for invest in name_value_dict:
        print(
            f"{invest['ativo']} possui R$ {str(invest['valor_investido']).replace('.', ',')} investido e representa {round(invest['valor_investido']/total_invested*100, 2) }% da carteira")
    print(total_invested)
    # print(name_value_dict)


database.create_investment_table()
# prompt_add_investment()
# list_all_investments()
organize_by_value_invested()

'''
user_date = input('Enter date in YYYY-mm-dd format: ')
data = user_date.strftime('%d-%m-%Y')

print(user_date)
print(data)
'''
