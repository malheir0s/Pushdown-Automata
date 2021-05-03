# pushdown-automata
this algorithm simulates a non-deterministic pushdown automata (PDA)

# Entrada
 Na primeira linha, há uma lista de estados. Na segunda linha, há o alfabeto de entrada. Na terceira linha, há o alfabeto de pilha. Na quarta linha, há o número total n de transições. Para cada uma das n linhas seguintes, há uma quíntupla <a, b, c, d, e> onde ‘a’ é o estado de origem, ‘b’ é o caractere a ser lido,  ‘c’ é o símbolo a ser desempilhado, ‘d’ é o estado de destino e, por fim, ‘e’ é a palavra a serempilhada. Em seguida, há um caractere informando o estado inicial. Na próxima linha, há uma lista de estados finais. Por fim, há uma lista de palavras de teste a ser reconhecida. Os itens da listas serão separados por espaço em branco. A palavra vazia (λ) é representada por *.

# Saída
 O algoritmo imprime para cada palavra de teste ‘S’ se o APND reconhece a palavra ou ‘N’ caso contrário.
