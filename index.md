<font size=6px>MCBM022-23 Introdução aos Processos Estocásticos </font>

[**Jair Donadelli**](http://hostel.ufabc.edu.br/~jair.donadelli/)  (sala 546, torre 2, bloco A)						**email** jair.donadelli@ufabc.edu.br



[toc]

Nessa disciplina vamos estudar os conceitos fundamentais de cadeias de Markov em tempo discreto e contínuo, martingales e teoria da renovação, com foco em suas propriedades, aplicações em modelagem e demonstrações teóricas. Calcular probabilidades de transição, retorno e limites, além de resolver e modelar situações-problema envolvendo esses temas.

**onde:** Seg. 21-23h (semanal); Qui. 19-21h (semanal) na sala 

**TPEI** 4-0-0-4 **RECOMENDAÇÃO**: Álgebra Linear; Cálculo de Probabilidade 

**EMENTA** Cadeias de Markov discretas e comportamento assintótico: passeios aleatórios, processo de ramificação. Processos de Poisson. Cadeias de Markov em tempo contínuo. Processos de renovação. Martingales. Introdução ao movimento browniano. 

**BIBLIOGRAFIA BÁSICA** 

DURRETT, Richard. Essentials of stochastic processes. New York, USA: Springer, 1999. vi, 281. (Springer texts in statistics). ISBN 9780387988368. 

HAIGH, John. Probability models. Falmer, GBR: Springer, 2002. viii, 256. (Springer undergraduate mathematics). ISBN 1852334312. 

ROSS, Sheldon M. Introduction to probability models. 10. ed. Burlington, USA: Academic Press, 2010. xv, 784 p., il. ISBN 9780123756862. 

**BIBLIOGRAFIA COMPLEMENTAR** 

BHAT, U. Narayan; MILLER, Gregory K. Elements of applied stochastic processes. 3. ed. Hoboken, USA: Wiley Publishing, 2002. xi, 461. (Wiley series in probability and statistics). ISBN 9780471414421. 

GRIMMETT, Geoffrey; STIRZAKER, David. Probability and random processes. 3. ed. Oxford, GBR; New York, USA: Oxford University Press, 2001. xii, 596 p., il. Includes bibliographical references (p. [580]-582) and index. ISBN 9780198572220. 

TAYLOR, Howard M.; KARLIN, Samuel. An introduction to stochastic modeling. 3. ed. San Diego, USA: Academic Press, 1998. xi, 631. ISBN 9780126848878. 955 

RESNICK, Sidney I. Adventures in stochastic processes. Boston, USA: Birkhäuser Science, c1992. xii, 626. ISBN 9780817635916. Outras Bibliografias ÇINLAR, Erhan. Introduction to stochastic processes. Mineola, USA: Dover, 2013. vii, 404. ISBN 9780486497976.

**MATERIAL COMPLEMENTAR** 

[Probability, Mathematical Statistics, Stochastic Processes](https://www.randomservices.org/random/)

[Finite Markov Chains and Algorithmic Applications](https://cms.dm.uba.ar/academico/materias/verano2018/probabilidades_y_estadistica_C/Haggstrom-Finite%20Markov%20chains%20and%20algorithm%20applications.pdf)

[Markov Chains and Mixing Times](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf)

[Brownian Motion](https://www.mi.uni-koeln.de/~moerters/book/book.pdf)

**Cronograma**

| Semana e Tema                                                | Objetivos                                                    | Tópicos                                                      | Referências                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------- |
| **Semana 1 – Introdução a Processos Estocásticos e Cadeias de Markov Discretas** | - Compreender o conceito de processo estocástico.<br>- Definir formalmente cadeia de Markov em tempo discreto.<br>- Representar cadeias por matrizes de transição. | - Espaço de estados, tempo discreto vs. contínuo.<br>- Propriedade de Markov e homogeneidade no tempo.<br>- Matriz de transição $P$, distribuição inicial e evolução $\pi^{(n)} = \pi^{(0)} P^n$. | Ross, Cap. 4.1–4.2.<br>G&S, Cap. 6.1–6.2. |
| **Semana 2 – Classificação de Estados e Passeios Aleatórios** | - Classificar estados: acessibilidade, comunicação, absorção.<br>- Estudar passeios aleatórios como exemplo central. | - Acessibilidade, comunicação, classes fechadas, estados absorventes.<br>- Periodicidade e aperiocidade.<br>- Passeio aleatório simples em $\mathbb{Z}$ e ciclos finitos. | Ross, Cap. 4.3.<br>G&S, Cap. 6.3–6.5.     |
| **Semana 3 – Distribuições Invariantes e Convergência**      | - Calcular distribuições estacionárias.<br>- Entender condições para existência e unicidade.<br>- Estudar convergência em cadeias finitas. | - Definição: $\pi P = \pi$.<br>- Cadeias irreducíveis e aperiódicas.<br>- Teorema ergódico (caso finito). | Ross, Cap. 4.4.<br>G&S, Cap. 6.6–6.8.     |
| **Semana 4 – Processos de Ramificação**                      | - Definir e analisar processo de Galton–Watson.<br>- Usar funções geradoras para probabilidade de extinção. | - Definição e árvore de descendência.<br>- Funções geradoras; regimes subcrítico, crítico e supercrítico. | Ross, Cap. 4.7.<br>G&S, Cap. 6.9.         |
| **Semana 5 – Processos de Poisson**                          | - Definir e caracterizar processo de Poisson.<br>- Relacionar chegadas com tempos exponenciais. | - Incrementos independentes e estacionários.<br>- Distribuição de contagem (Poisson).<br>- Distribuição de tempos (exponencial).<br>- Superposição e divisão. | Ross, Cap. 5.1–5.3.<br>G&S, Cap. 6.10.    |
| **Semana 6 – Cadeias de Markov em Tempo Contínuo**           | - Introduzir cadeias de Markov em tempo contínuo.<br>- Entender matriz geradora $Q$ e equações de Kolmogorov. | - Definição; taxas de transição.<br>- Equações de Kolmogorov (direita e esquerda).<br>- Processos de nascimento e morte. | Ross, Cap. 6.1–6.4.<br>G&S, Cap. 6.11.    |
| **Semana 7 – Martingales**                                   | - Definir martingales em tempo discreto.<br>- Estudar propriedades básicas e exemplos. | - Martingale, submartingale, supermartingale.<br>- Propriedades básicas.<br>- Teorema de parada opcional (forma simples). | Ross, Cap. 13.1–13.3.<br>G&S, Cap. 12.    |
| **Semana 8 – Introdução ao Movimento Browniano**             | - Definir movimento browniano e propriedades básicas.<br>- Relacionar com passeios aleatórios como limite difusivo. | - Incrementos independentes e gaussianos.<br>- Continuidade de trajetória.<br>- Aproximação via passeio aleatório escalonado. | Ross, Cap. 10.1–10.3.<br>G&S, Cap. 13.    |





## 







| semana                                                       | Temas                                                        | Objetivos                                                    | Material                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 01                                                           | Apresentação da disciplina e revisão de probabilidade. Definição de Cadeia de Markov |                                                              | Exercícios de revisão                                        |
| 02 - Introdução a Processos Estocásticos e Cadeias de Markov Discretas | Propriedade de Markov, homogeneidade no tempo.<br/>Matriz de transição, representação gráfica (diagramas de estados).<br/>Distribuição após $n$ passos. | Compreender o conceito geral de processo estocástico. Definir formalmente uma cadeia de Markov em tempo discreto. Introduzir representação via matriz de transição. | Leitura<br/><br/>Norris, Markov Chains, Cap. 1.<br/><br/>Grimmett & Stirzaker, Probability and Random Processes, Seção 6.1. |
| 03 - Classificação de Estados e Passeios Aleatórios          | Acessibilidade, comunicação, classes, estados absorventes.<br/>Recorrência, transiência, periodicidade.<br/>Passeios aleatórios simples .<br/>Comportamento assintótico de passeios aleatórios: tempo de retorno esperado. | Classificar estados quanto à acessibilidade, comunicação e absorção.<br/><br/>Estudar passeios aleatórios como exemplo central. | Leitura<br/><br/>Norris, Cap. 1 e 2.<br/><br/>Ross, Introduction to Probability Models, Seção 4.3. |
| 04                                                           | Prova na 5ª                                                  |                                                              |                                                              |
| 05 – Distribuições Invariantes e Convergência                | Definição: <br/>𝜋<br/>𝑃<br/>=<br/>𝜋<br/>πP=π, normalização.<br/><br/>Existência e unicidade em cadeias irreducíveis e aperiódicas.<br/><br/>Convergência para <br/>𝜋<br/>π (Teorema Ergodico). | Compreender distribuição estacionária e condições para sua existência.<br/><br/>Introduzir o Teorema Ergodico em cadeias finitas. | Leitura<br/><br/>Norris, Cap. 1.7.<br/><br/>Ross, Seção 4.4. |
| 06 – Processos de Ramificação                                | Definição do processo de ramificação.<br/><br/>Funções geradoras e propriedades.<br/><br/>Probabilidade de extinção e regimes subcrítico, crítico e supercrítico. | Entender o processo de Galton–Watson.<br/><br/>Usar funções geradoras para estudar probabilidade de extinção. | Leitura<br/><br/>Grimmett & Stirzaker, Seção 6.7.<br/><br/>Harris, The Theory of Branching Processes, Cap. 1. |
| 07– Processos de Poisson                                     | Incrementos independentes e estacionários.<br/><br/>Distribuição de Poisson para contagem de eventos.<br/><br/>Tempo até o primeiro evento, distribuição exponencial.<br/><br/>Superposição e divisão de processos de Poisson. | Definir e caracterizar o processo de Poisson.<br/><br/>Relacionar tempos de chegada com distribuição exponencial. | 27/10 é feriado, reposição em 08/12<br/>Leitura<br/><br/>Ross, Cap. 5.<br/><br/>Norris, Cap. 2. |
| 08                                                           | Prova  na 5ª                                                 |                                                              |                                                              |
| 09 – Cadeias de Markov em Tempo Contínuo                     | Definição formal, taxas de transição.<br/><br/>Equações de Kolmogorov direta e inversa.<br/><br/>Processo de nascimento e morte. | Introduzir o conceito de cadeia de Markov em tempo contínuo.<br/><br/>Compreender a matriz geradora <br/>𝑄<br/>Q e as equações de Kolmogorov. | Leitura<br/><br/>Norris, Cap. 2.<br/><br/>Ross, Seção 6.1–6.3. |
| 10 – Martingales                                             | Definição, intuição de “jogo justo”.<br/><br/>Martingale, submartingale, supermartingale.<br/><br/>Propriedades básicas, parada opcional (versão simples). | Definir martingales em tempo discreto.<br/><br/>Explorar exemplos e aplicações simples. | 20/11 é feriado, reposição em 11/12<br/>Leitura<br/><br/>Williams, Probability with Martingales, Cap. 5.<br/><br/>Grimmett & Stirzaker, Seção 12.1. |
| 11– Introdução ao Movimento Browniano                        | Definição: incrementos independentes, estacionários e gaussianos.<br/><br/>Continuidade de trajetória.<br/><br/>Limite de passeios aleatórios.<br/><br/>Aplicações introdutórias (precificação, difusão física). | Compreender propriedades básicas do movimento browniano.<br/><br/>Relacionar com passeios aleatórios como limite difusivo. |                                                              |
| 12                                                           | Prova na 5ª                                                  |                                                              |                                                              |
| 13                                                           | Prova Sub em 08/12<br/>Exame de recuperação em 11/12         |                                                              |                                                              |
|                                                              |                                                              |                                                              |                                                              |



## **Avaliação**

3 provas 

## **Atendimento**







![image-20250721155034230](./image-20250721155034230.png)
