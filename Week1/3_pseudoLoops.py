Het algoritme zorgt ervoor dat de sum wordt uitgerekend door steeds het 1ste tot laatste cijfer op te tellen en dat dit steeds met 1 plekje verschuifd, 
als de sum groter is dan max, dan krijgt de sum waarde van max, uiteindelijk returnd het een array results, met daarin de sum waarden.


Maak array result
for loop i van 0 tot en met lengte array a gedeeld door 2
j is de lengte van array a min 1 en min i
maak sum met  int 0
for loop van  k in range i tot j
sum krijgt sum + a[k] ex 0 = 0 + 10; 10 = 10 + 20; sum = 30
eind for
als sum groter is dan max dan wordt het max in sum gezet
sum wordt append in result
return result
 1 2 3 4 5 6
0 - 5 1+2+3+4+5+6 21
1-4 2+3+4+5 14
2-3	3+4 7
3-3 4
