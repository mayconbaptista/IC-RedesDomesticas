"""
qua 16 nov 2022 # colete 5 min dedados salve em uma arq pcap entenda as features,
gere um arquivo csv crie um data framim e faça analizes estatisticas sobre os dados extraidos,
monte um histograma.
*  o que é um fulho e o que representa esse fluxo?
* conteudo do pacote, o nfstream não olha o conteudo mais sim o cabeçalho.
"""

import nfstream
import pandas as PD
import csv
import matplotlib

# df = nfstream.NFStreamer(source="first.pcapng", statistical_analysis=True).to_pandas()


if __name__ == '__main__':


    try:
        # nfstream.NFStreamer(source="pcaps/in1.pcap",statistical_analysis=True).to_csv()
        df = nfstream.NFStreamer(source="pcaps/in1.pcap",statistical_analysis=True).to_pandas()

        pcap_csv = df.to_csv()

        # arg = open('pcap.csv','w')
        # arg.write(pcap_csv)
    except:
        print("error!")
        exit()

    print(df.head(10)) # mostrando as 10 primeiras linhas

    print(df.columns)

    print(df.loc[3]) # mostrar os dados da coluna 3

    print(df[['src_ip']]) # mostrar todos os dados da coluna src_ip 

    print(df[df['src_ip'] == '192.168.0.1']) # filtrar somente os end que o ip de origem seja igual a 192.168.0.1


    print(df[['protocol']])

    index = PD.read_csv('protocol-numbers.csv')

    print(index.head(10))

    