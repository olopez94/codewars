int basicOp(char op, int val1, int val2) {
  // Your code here
  if (op == '+'){
    return val1 + val2;
  } else if (op == '-'){
    return val1 - val2;
  } else if (op == '*'){
    return val1 * val2;
  } else if (op == '/'){
    return val1 / val2;
  }
}

/*
int basicOp(char op, int val1, int val2) {
  switch (op) {
    case '+': return val1 + val2;
              break;
    case '-': return val1 - val2;
              break;
    case '*': return val1 * val2;
              break;
    case '/': return val1 / val2;
              break;
    
  }
  return 0;
}
*/
