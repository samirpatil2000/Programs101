[X, Y] = meshgrid(-50:.2:50, -50:.2:50);
V = 1.8 ^(1.5 * sqrt(X^2+Y^2)).*cos(0.5*Y).