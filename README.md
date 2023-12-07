# Metody-Statystyczne

proj1: 
Proszę zaprogramować generator zmiennych losowych z rozkładu normalnego N(0,1), 
korzystając z generatora liczb pseudolosowych rozkładu jednorodnego U(0,1).
Można korzystać z dowolnej metody (centralne twierdzenie graniczne, algorytm Boksa-Muellera, metoda odrzucania, itp.).
Proszę narysować histogram losowanych liczb (można spróbować różny "binning", czyli szerokość pudełek, ale sugeruję 
https://en.wikipedia.org/wiki/Histogram#Scott's_normal_reference_rule) i porównać dystrybuantę z dystrybuantą teoretyczną.

proj2:
Proszę zasymulować proces ruiny gracza z kapitałami początkowymi:
a = 50,  b = 50.
Z symulacji dla różnych wartości p (prawdopodobieństwo zabrania przez gracza A 1$ od gracza B) proszę narysować wykresy zależności prawdopodobieństwa ruiny gracza P(ruina A) od p.
Powinny to być co najmniej dwa wykresy uśrednione po różnych liczbach gier, małej i dużej (np. 10 i 1000).

proj3:
Proszę zasymulować proces ruiny gracza z łącznymi kapitałami początkowymi a + b = 100 i p = 1/2.
Z symulacji dla różnych wartości kapitału początkowego a proszę narysować wykresy zależności prawdopodobieństwa ruiny gracza P(ruina A) od a.

proj4:
Proszę zasymulować proces ruiny gracza z łącznymi kapitałami początkowymi a = b = 50.
Dla trzech różnych wartości p = 1/5, 1/2, 4/5 proszę wyznaczyć rozkład prawdopodobieństwa długości trwania rozgrywki (czyli ruiny dowolnego gracza) P(L).
Z tego rozkładu proszę wyznaczyć średnią i jej odchylenie standardowe.

proj5:
Proszę zasymulować N=100 procesów ruiny gracza z łącznymi kapitałami początkowymi a = b = 50.
Proszę wyznaczyć wykres prawdopodobieństwa średniego trwania rozgrywki (wartość znana z poprzedniego zadania) w zależności od prawdopodobieństwa p.

proj6:
Proszę zasymulować proces ruiny gracza z łącznymi kapitałami początkowymi a = b = 50 i p = 1/2 i 1/5.
Proszę wyznaczyć rozkład kapitału gracza A po n krokach rozgrywki w trzech przypadkach:
n = 10, L_śr/2, 0.9 L_śr
gdzie L_śr to średnia długość trwania rozgrywki wyznaczona w poprzednich zadaniach.

proj7:
Proszę dla obydwu graczy narysować trajektorie liczby wygranych (całych rozgrywek!) w funkcji liczby gier dla kilku wybranych parametrów a, b, p (przy a+b=100).
(To tzw. proces liczący. Trajektorie będą krzywymi niemalejącymi.)

proj8:
Mając daną macierz przejścia P
0.64	0.32	0.04
0.4	0.5	0.1
0.25	0.5	0.25
trzystanowego łańcucha Markowa

proszę obliczyć jego stan stacjonarny  \Pi = \Pi P  poprzez wielokrotne mnożenie macierzy P.
 lim_{n \rightarrow \infty} P^n  przyjmie wierszami wartości stanu stacjonarnego

\Pi_0	\Pi_1\Pi_2
\Pi_0\Pi_1\Pi_2
\Pi_0\Pi_1\Pi_2

Proszę znaleźć \bar{n}, od którego kolejne iteracje mnożenia są stabilne, tzn. np.  |P^n-P^{n-1}| \leq 10^{-5} . Można w tym celu patrzeć na poszczególne elementy macierzowe, np.  |P_{00}^n-P_{00}^{n-1}| albo jakąś normę macierzową.
Proszę narysować wykres zmienności danego elementu lub całej normy wraz z kolejnymi iteracjami.
