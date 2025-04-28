# MISP Docker Ubuntu 24.04

www.linkedin.com/in/inaldo-nascimento



** MISP Project ** 

MISP ("Malware Information Sharing Platform") Open Source Threat Intelligence Platform & Open Standards For Threat Information Sharing.



## Agenda:

```
### Introdução 
    Documentação
    
### Sua instãncia
    From scratch 
    Or container

### E depois?
	eventos
        distribuição
	feeds
	taxonomias
	integração

```


---------------------------------------------------------------------------


## Introdução

O MISP (Malware Information Sharing Platform & Threat Sharing) é uma plataforma de código aberto desenvolvida para facilitar o compartilhamento de informações sobre ameaças cibernéticas entre organizações. Criado pelo CSIRT de Luxenburgo, com foco na colaboração, o MISP permite a coleta, armazenamento, análise e disseminação de indicadores de comprometimento (IOCs) e inteligência de ameaças (CTI) de forma estruturada e segura.

### Documentação vasta....

https://www.misp-project.org/documentation/

https://www.circl.lu/doc/misp/

https://www.circl.lu/doc/misp/quick-start/

https://cert.br/misp/

https://cert.br/misp/#tutoriais




---------------------------------------------------------------------------

## Instalando sua instância

#### From scratch, the hard way...

https://cert.br/misp/tutorial-ubuntu/


#### With container, the easy way...

https://github.com/ServSlack/misp_docker_ubuntu_24_04

##### Fetch files
```
$ git clone https://github.com/ServSlack/misp_docker_ubuntu_24_04
$ cd misp_docker_ubuntu_24_04
$ chmod +x *.sh web/*.sh files/*.sh
$ ./1_Install_Docker.sh
$ ./2-Build_MISP_Image.sh
$ ./3-Create_MISP_Containers.sh
```



---------------------------------------------------------------------------

## O que vem depois da instalação...

https://www.circl.lu/doc/misp/quick-start/


####    eventos

https://cert.br/misp/certbr-passo-a-passo-misp-2021-08-19.pdf#page=8

####    distribuição dos eventos

https://cert.br/misp/certbr-passo-a-passo-misp-2021-08-19.pdf#page=38

####    feeds

https://www.circl.lu/doc/misp/managing-feeds/

####     taxonomias

https://www.circl.lu/doc/misp/taxonomy/

####    integração

https://cert.br/misp/certbr-passo-a-passo-misp-2021-08-19.pdf#page=50


 
