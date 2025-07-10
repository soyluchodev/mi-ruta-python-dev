
# Manipulación de Series en pandas

## Conceptos clave

1. Acceso a elementos

```markdown
| Método | Tipo acceso      | Negativos | Ejemplo                      | Output   |
|--------|------------------|-----------|------------------------------|----------|
| iloc   | Posición (int)   | Sí        | `serie.iloc[-1]`             | Último   |
| loc    | Etiqueta (str)   | No        | `serie.loc["índice"]`        | Valor    |
```



## Notas importantes

- .iloc es estrictamente posicional (solo enteros)
- .loc usa las etiquetas del índice
- Los índices negativos solo funcionan con .iloc