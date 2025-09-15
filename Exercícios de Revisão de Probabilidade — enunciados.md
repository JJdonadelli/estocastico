# Exercícios de Revisão de Probabilidade 

------

## 1. Esperança condicional

Seja $(X, Y)$ um vetor aleatório com densidade conjunta

$f_{X,Y}(x,y) = \frac{1}{8}, \quad 0 < x < 2,\ 0 < y < 4,$

e $f_{X,Y}(x,y) = 0$ caso contrário.

(a) Calcule $E[X \mid Y = y]$.

(b) Calcule $E[E[X\mid Y]]$ e verifique a propriedade da torre $E[E[X\mid Y]] = E[X]$.

------

## 2. Distribuição em um processo de Poisson

Uma fila de atendimento segue um processo de Poisson (o número de chegadas em intervalo de comprimento $t$ tem distribuição de Poisson com parâmetro $\lambda t$)  com taxa de $\lambda = 3$ clientes por minuto.

(a) Qual a probabilidade de que **nenhum cliente** chegue em um intervalo de 30 segundos?

(b) O tempo até o próximo evento em um Poisson($\lambda$)  tem distribuição exponencial Exp($\lambda$). Qual a probabilidade de que o **tempo até o próximo cliente** seja maior que 1 minuto?

(c) Justifique a propriedade de *falta de memória* da distribuição exponencial neste contexto, ou seja, prove que $\mathbb P(T>s+t\mid T>s) = \mathbb P(T>t).$

------

## 3. Cálculo de probabilidades em um passeio aleatório

Considere um passeio aleatório $(S_n)_{n\ge0}$ em $\mathbb{Z}$ com $S_0=0$ e passos independentes e com a esma lei:

$\mathbb P(X_i=+1)=p,\qquad \mathbb P(X_i=-1)=1-p.$

Então $S_n=\sum_{i=1}^n X_i$.

(a) Para $p=\tfrac12$, calcule $P(S_2=0)$ e $P(S_4=0)$.

(b) Para $p=0.6$, calcule $E[S_5]$ e $\mathrm{Var}(S_5)$.

------

## 4. Covariância e correlação em vetores aleatórios

Sejam $X\sim N(0,1)$ e $Y = 2X + \varepsilon$, onde $\varepsilon\sim N(0,4)$ é independente de $X$.

(a) Calcule $\mathrm{Cov}(X,Y)$ e $\mathrm{Corr}(X,Y)$.

(b) Discuta como a correlação se relaciona com dependência e independência.

------

## 5. Teorema Central do Limite

Sejam \(X_i\) variáveis aleatórias independentes com distribuição Bernoulli(\(p\)). Defina \(S_n=\sum_{i=1}^n X_i\).

(1) Verifique que a esperança e a variância \(S_n\) são $np$ e $np(1-p)$, respectivamente.

(2) Pelo TCL – Teorema Central do Limite – vale que, para \(n\) grande,
$$
\mathbb P\Big(\frac{S_n-np}{\sqrt{np(1-p)}}\le z\Big)\approx\Phi(z),
$$
onde \(\Phi\) é a função distribuição da normal padrão.

Estime \(\mathbb P(S_{100}\ge 60)\) para \(p=0.55\) conhecido que $\Phi(0.9045)\approx 0.816$​.5. .

------

## 6. Quem vai pagar o pastel?

------

Dois amigos foram passear na feira. Quando chegaram na barraca de pastel, decidiram fazer uma [aposta](aposta.html) para ver quem iria pagar a conta. Cada um escolheu, de antemão, uma sequência de três resultados possíveis nos lançamentos de uma moeda – cara (c) e coroa (k). Em seguida, começaram a lançar a moeda repetidamente, combinando que o vencedor seria aquele cuja sequência aparecesse primeiro.

Supondo que quem escolheu primeiro escolheu ckc, quais são as probabilidades do segundo a escolher ganhar o jogo considerando cada uma dois 7 possíveis outras sequências?