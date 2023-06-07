import pandas as pd
import numpy as np

if __name__ == '__main__':

    data = pd.read_csv('teste2.csv', sep=',', low_memory=False)

    # print(data[['application_category_name']])

    src_ip_distintos = data.drop_duplicates(subset='src_ip')

    print(f"Quantos src_ip distintos eu tenho: {len(src_ip_distintos[['src_ip']])}")
    # print(len(ips_distintos[['src_ip']]))

    print(f"Qual a porcentagem de ips de destino distintos: {(len(src_ip_distintos[['dst_ip']]) / len(data[['src_ip']])) * 100}%")

    dst_ip_distintos = data.drop_duplicates(subset='dst_ip')
    print(f"Quantos des_ip distintos eu tenho: {len(dst_ip_distintos[['src_ip']])}")
    # print(len(ips_distintos[['src_ip']]))

    print(f"Qual a porcentagem de ips de destino distintos: {(len(dst_ip_distintos[['src_ip']]) / len(data[['src_ip']])) * 100}%")

    protocolos_distintos = data.drop_duplicates(subset='protocol')
    print(f"Quantos protocolos distintos eu tenho: {len(protocolos_distintos[['protocol']])}")
    print(protocolos_distintos[['protocol']])

    print(f"Qual a porcentagem de protocolos de destino distintos: {(len(dst_ip_distintos[['protocol']]) / len(data[['protocol']])) * 100}%")

    print(data['src_ip'].unique)

    dic_protocolos = {1:'ICMP', 17:'UDP', 6:'TCP', 58:'IPv6-ICMP', 2:'IGMP'}

    # protocols = pd.read_csv('protocol-numbers.cvs',sep=',')

    # print(protocols)

    teste = protocolos_distintos['protocol'].map(dic_protocolos)

    #print(teste[['protocol']])

    print(data.describe())

    print(data[['src_ip']].value_counts())

    print(data[['dst_ip']].value_counts())

    print(data[['protocol']].value_counts())

    print(data.groupby(['src_ip', 'dst_ip', 'protocol']))