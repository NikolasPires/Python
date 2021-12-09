from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo: '))
sin = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a,sin))
cos = cos(radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos))
tan = tan(radians(a))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, tan))