
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programnonassocIFXnonassocELSEnonassocSMALLERLARGERSMALLEREQLARGEREQNOTEQEQleftADDSUBDOTADDDOTSUBleftMULDIVDOTMULDOTDIVleftUMINUSleftTRANSPOSEADD ADDASSIGN ASSIGN BREAK COLON COMMA CONTINUE DIV DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR ID IF INT LARGER LARGEREQ LCURLBRACK LPARENT LSQBRACK MUL MULASSIGN NOTEQ ONES PRINT RCURLBRACK RETURN RPARENT RSQBRACK SEMICOLON SMALLER SMALLEREQ STRING SUB SUBASSIGN TRANSPOSE WHILE ZEROSprogram : instructionsinstructions : instructions instruction\n                    | instructioninstruction : assignment SEMICOLON\n                   | call SEMICOLON\n                   | loop\n                   | branch\n                   | LCURLBRACK instructions RCURLBRACKassignment : ID assignment_operator expression\n                  | ID matrix assignment_operator expressionassignment_operator : ASSIGN\n                           | ADDASSIGN\n                           | SUBASSIGN\n                           | MULASSIGN\n                           | DIVASSIGNexpression : term\n                  | LPARENT expression RPARENTexpression : expression ADD expression\n                  | expression SUB expression\n                  | expression MUL expression\n                  | expression DIV expression\n                  | expression DOTADD expression\n                  | expression DOTSUB expression\n                  | expression DOTMUL expression\n                  | expression DOTDIV expressionexpression : SUB expression %prec UMINUSexpression : expression TRANSPOSEcomparison : expression comparison_operator expressioncomparison_operator : SMALLER\n                          | LARGER\n                          | SMALLEREQ\n                          | LARGEREQ\n                          | NOTEQ\n                          | EQcall : BREAK\n            | CONTINUE\n            | RETURN expression\n            | PRINT print_inputsprint_inputs : print_inputs COMMA print_input\n                    | print_inputprint_input : STRING\n                   | IDmatrix_fun : fun_name LPARENT expression RPARENTfun_name : EYE\n                | ZEROS\n                | ONESloop : for\n            | whilefor : FOR for_expression instructionfor_expression : ID ASSIGN rangewhile : WHILE LPARENT comparison RPARENT instructionbranch : IF LPARENT comparison RPARENT instruction %prec IFX\n              | IF LPARENT comparison RPARENT instruction ELSE instructionrange : num_term COLON num_termterm : ID\n            | number\n            | matrix\n            | stringnum_term : ID\n                | numbermatrix_term : ID\n                   | matrix\n                   | numbernumber : INT\n              | FLOATstring : STRINGmatrix : LSQBRACK matrix_contents RSQBRACK\n              | matrix_funmatrix_contents : matrix_contents COMMA matrix_content\n                       | matrix_contentmatrix_content : matrix_term'
    
_lr_action_items = {'LCURLBRACK':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[8,8,-3,-6,-7,8,-47,-48,-2,-4,-5,8,-64,-65,8,-8,-49,8,-59,-50,-60,8,-52,-51,8,-54,-53,]),'ID':([0,2,3,6,7,8,12,13,14,15,17,19,20,21,22,23,25,26,27,28,29,30,38,39,44,45,51,52,54,55,57,64,65,66,67,68,69,70,71,72,76,79,80,84,96,97,98,99,100,101,102,103,104,105,107,108,111,113,114,115,116,117,],[9,9,-3,-6,-7,9,40,50,-47,-48,53,-2,-4,-5,9,40,-11,-12,-13,-14,-15,61,40,40,-64,-65,40,9,40,-8,40,40,40,40,40,40,40,40,40,40,50,-49,104,61,9,40,-29,-30,-31,-32,-33,-34,-59,-50,-60,9,-52,104,-51,9,-54,-53,]),'BREAK':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[10,10,-3,-6,-7,10,-47,-48,-2,-4,-5,10,-64,-65,10,-8,-49,10,-59,-50,-60,10,-52,-51,10,-54,-53,]),'CONTINUE':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[11,11,-3,-6,-7,11,-47,-48,-2,-4,-5,11,-64,-65,11,-8,-49,11,-59,-50,-60,11,-52,-51,11,-54,-53,]),'RETURN':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[12,12,-3,-6,-7,12,-47,-48,-2,-4,-5,12,-64,-65,12,-8,-49,12,-59,-50,-60,12,-52,-51,12,-54,-53,]),'PRINT':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[13,13,-3,-6,-7,13,-47,-48,-2,-4,-5,13,-64,-65,13,-8,-49,13,-59,-50,-60,13,-52,-51,13,-54,-53,]),'IF':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[16,16,-3,-6,-7,16,-47,-48,-2,-4,-5,16,-64,-65,16,-8,-49,16,-59,-50,-60,16,-52,-51,16,-54,-53,]),'FOR':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[17,17,-3,-6,-7,17,-47,-48,-2,-4,-5,17,-64,-65,17,-8,-49,17,-59,-50,-60,17,-52,-51,17,-54,-53,]),'WHILE':([0,2,3,6,7,8,14,15,19,20,21,22,44,45,52,55,79,96,104,105,107,108,111,114,115,116,117,],[18,18,-3,-6,-7,18,-47,-48,-2,-4,-5,18,-64,-65,18,-8,-49,18,-59,-50,-60,18,-52,-51,18,-54,-53,]),'$end':([1,2,3,6,7,14,15,19,20,21,55,79,111,114,117,],[0,-1,-3,-6,-7,-47,-48,-2,-4,-5,-8,-49,-52,-51,-53,]),'RCURLBRACK':([3,6,7,14,15,19,20,21,22,55,79,111,114,117,],[-3,-6,-7,-47,-48,-2,-4,-5,55,-8,-49,-52,-51,-53,]),'SEMICOLON':([4,5,10,11,31,36,37,40,41,42,43,44,45,46,47,48,49,50,56,73,75,82,83,86,87,88,89,90,91,92,93,94,95,110,],[20,21,-35,-36,-68,-37,-16,-55,-56,-57,-58,-64,-65,-66,-38,-40,-41,-42,-9,-27,-26,-10,-67,-18,-19,-20,-21,-22,-23,-24,-25,-17,-39,-43,]),'ELSE':([6,7,14,15,20,21,55,79,111,114,117,],[-6,-7,-47,-48,-4,-5,-8,-49,115,-51,-53,]),'ASSIGN':([9,24,31,53,83,110,],[25,25,-68,80,-67,-43,]),'ADDASSIGN':([9,24,31,83,110,],[26,26,-68,-67,-43,]),'SUBASSIGN':([9,24,31,83,110,],[27,27,-68,-67,-43,]),'MULASSIGN':([9,24,31,83,110,],[28,28,-68,-67,-43,]),'DIVASSIGN':([9,24,31,83,110,],[29,29,-68,-67,-43,]),'LSQBRACK':([9,12,23,25,26,27,28,29,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,84,97,98,99,100,101,102,103,],[30,30,30,-11,-12,-13,-14,-15,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-29,-30,-31,-32,-33,-34,]),'EYE':([9,12,23,25,26,27,28,29,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,84,97,98,99,100,101,102,103,],[33,33,33,-11,-12,-13,-14,-15,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-29,-30,-31,-32,-33,-34,]),'ZEROS':([9,12,23,25,26,27,28,29,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,84,97,98,99,100,101,102,103,],[34,34,34,-11,-12,-13,-14,-15,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-29,-30,-31,-32,-33,-34,]),'ONES':([9,12,23,25,26,27,28,29,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,84,97,98,99,100,101,102,103,],[35,35,35,-11,-12,-13,-14,-15,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-29,-30,-31,-32,-33,-34,]),'LPARENT':([12,16,18,23,25,26,27,28,29,32,33,34,35,38,39,51,54,57,64,65,66,67,68,69,70,71,72,97,98,99,100,101,102,103,],[38,51,54,38,-11,-12,-13,-14,-15,64,-44,-45,-46,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-29,-30,-31,-32,-33,-34,]),'SUB':([12,23,25,26,27,28,29,31,36,37,38,39,40,41,42,43,44,45,46,51,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,97,98,99,100,101,102,103,110,112,],[39,39,-11,-12,-13,-14,-15,-68,66,-16,39,39,-55,-56,-57,-58,-64,-65,-66,39,39,66,39,39,39,39,39,39,39,39,39,39,-27,66,-26,66,66,-67,66,-18,-19,-20,-21,-22,-23,-24,-25,-17,39,-29,-30,-31,-32,-33,-34,-43,66,]),'INT':([12,23,25,26,27,28,29,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,80,84,97,98,99,100,101,102,103,113,],[44,44,-11,-12,-13,-14,-15,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-29,-30,-31,-32,-33,-34,44,]),'FLOAT':([12,23,25,26,27,28,29,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,80,84,97,98,99,100,101,102,103,113,],[45,45,-11,-12,-13,-14,-15,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-29,-30,-31,-32,-33,-34,45,]),'STRING':([12,13,23,25,26,27,28,29,38,39,51,54,57,64,65,66,67,68,69,70,71,72,76,97,98,99,100,101,102,103,],[46,49,46,-11,-12,-13,-14,-15,46,46,46,46,46,46,46,46,46,46,46,46,46,46,49,46,-29,-30,-31,-32,-33,-34,]),'ADD':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,65,-16,-55,-56,-57,-58,-64,-65,-66,65,-27,65,-26,65,65,-67,65,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,65,]),'MUL':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,67,-16,-55,-56,-57,-58,-64,-65,-66,67,-27,67,-26,67,67,-67,67,67,67,-20,-21,67,67,-24,-25,-17,-43,67,]),'DIV':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,68,-16,-55,-56,-57,-58,-64,-65,-66,68,-27,68,-26,68,68,-67,68,68,68,-20,-21,68,68,-24,-25,-17,-43,68,]),'DOTADD':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,69,-16,-55,-56,-57,-58,-64,-65,-66,69,-27,69,-26,69,69,-67,69,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,69,]),'DOTSUB':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,70,-16,-55,-56,-57,-58,-64,-65,-66,70,-27,70,-26,70,70,-67,70,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,70,]),'DOTMUL':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,71,-16,-55,-56,-57,-58,-64,-65,-66,71,-27,71,-26,71,71,-67,71,71,71,-20,-21,71,71,-24,-25,-17,-43,71,]),'DOTDIV':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,72,-16,-55,-56,-57,-58,-64,-65,-66,72,-27,72,-26,72,72,-67,72,72,72,-20,-21,72,72,-24,-25,-17,-43,72,]),'TRANSPOSE':([31,36,37,40,41,42,43,44,45,46,56,73,74,75,78,82,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,73,-16,-55,-56,-57,-58,-64,-65,-66,73,-27,73,73,73,73,-67,73,73,73,73,73,73,73,73,73,-17,-43,73,]),'RSQBRACK':([31,44,45,58,59,60,61,62,63,83,109,110,],[-68,-64,-65,83,-70,-71,-61,-62,-63,-67,-69,-43,]),'COMMA':([31,44,45,47,48,49,50,58,59,60,61,62,63,83,95,109,110,],[-68,-64,-65,76,-40,-41,-42,84,-70,-71,-61,-62,-63,-67,-39,-69,-43,]),'RPARENT':([31,37,40,41,42,43,44,45,46,73,74,75,77,81,83,85,86,87,88,89,90,91,92,93,94,110,112,],[-68,-16,-55,-56,-57,-58,-64,-65,-66,-27,94,-26,96,108,-67,110,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,-28,]),'SMALLER':([31,37,40,41,42,43,44,45,46,73,75,78,83,86,87,88,89,90,91,92,93,94,110,],[-68,-16,-55,-56,-57,-58,-64,-65,-66,-27,-26,98,-67,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,]),'LARGER':([31,37,40,41,42,43,44,45,46,73,75,78,83,86,87,88,89,90,91,92,93,94,110,],[-68,-16,-55,-56,-57,-58,-64,-65,-66,-27,-26,99,-67,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,]),'SMALLEREQ':([31,37,40,41,42,43,44,45,46,73,75,78,83,86,87,88,89,90,91,92,93,94,110,],[-68,-16,-55,-56,-57,-58,-64,-65,-66,-27,-26,100,-67,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,]),'LARGEREQ':([31,37,40,41,42,43,44,45,46,73,75,78,83,86,87,88,89,90,91,92,93,94,110,],[-68,-16,-55,-56,-57,-58,-64,-65,-66,-27,-26,101,-67,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,]),'NOTEQ':([31,37,40,41,42,43,44,45,46,73,75,78,83,86,87,88,89,90,91,92,93,94,110,],[-68,-16,-55,-56,-57,-58,-64,-65,-66,-27,-26,102,-67,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,]),'EQ':([31,37,40,41,42,43,44,45,46,73,75,78,83,86,87,88,89,90,91,92,93,94,110,],[-68,-16,-55,-56,-57,-58,-64,-65,-66,-27,-26,103,-67,-18,-19,-20,-21,-22,-23,-24,-25,-17,-43,]),'COLON':([44,45,104,106,107,],[-64,-65,-59,113,-60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions':([0,8,],[2,22,]),'instruction':([0,2,8,22,52,96,108,115,],[3,19,3,19,79,111,114,117,]),'assignment':([0,2,8,22,52,96,108,115,],[4,4,4,4,4,4,4,4,]),'call':([0,2,8,22,52,96,108,115,],[5,5,5,5,5,5,5,5,]),'loop':([0,2,8,22,52,96,108,115,],[6,6,6,6,6,6,6,6,]),'branch':([0,2,8,22,52,96,108,115,],[7,7,7,7,7,7,7,7,]),'for':([0,2,8,22,52,96,108,115,],[14,14,14,14,14,14,14,14,]),'while':([0,2,8,22,52,96,108,115,],[15,15,15,15,15,15,15,15,]),'assignment_operator':([9,24,],[23,57,]),'matrix':([9,12,23,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,84,97,],[24,42,42,62,42,42,42,42,42,42,42,42,42,42,42,42,42,42,62,42,]),'matrix_fun':([9,12,23,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,84,97,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'fun_name':([9,12,23,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,84,97,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'expression':([12,23,38,39,51,54,57,64,65,66,67,68,69,70,71,72,97,],[36,56,74,75,78,78,82,85,86,87,88,89,90,91,92,93,112,]),'term':([12,23,38,39,51,54,57,64,65,66,67,68,69,70,71,72,97,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'number':([12,23,30,38,39,51,54,57,64,65,66,67,68,69,70,71,72,80,84,97,113,],[41,41,63,41,41,41,41,41,41,41,41,41,41,41,41,41,41,107,63,41,107,]),'string':([12,23,38,39,51,54,57,64,65,66,67,68,69,70,71,72,97,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'print_inputs':([13,],[47,]),'print_input':([13,76,],[48,95,]),'for_expression':([17,],[52,]),'matrix_contents':([30,],[58,]),'matrix_content':([30,84,],[59,109,]),'matrix_term':([30,84,],[60,60,]),'comparison':([51,54,],[77,81,]),'comparison_operator':([78,],[97,]),'range':([80,],[105,]),'num_term':([80,113,],[106,116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','Mparser.py',30),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Mparser.py',34),
  ('instructions -> instruction','instructions',1,'p_instructions','Mparser.py',35),
  ('instruction -> assignment SEMICOLON','instruction',2,'p_instruction','Mparser.py',39),
  ('instruction -> call SEMICOLON','instruction',2,'p_instruction','Mparser.py',40),
  ('instruction -> loop','instruction',1,'p_instruction','Mparser.py',41),
  ('instruction -> branch','instruction',1,'p_instruction','Mparser.py',42),
  ('instruction -> LCURLBRACK instructions RCURLBRACK','instruction',3,'p_instruction','Mparser.py',43),
  ('assignment -> ID assignment_operator expression','assignment',3,'p_assignment','Mparser.py',47),
  ('assignment -> ID matrix assignment_operator expression','assignment',4,'p_assignment','Mparser.py',48),
  ('assignment_operator -> ASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',52),
  ('assignment_operator -> ADDASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',53),
  ('assignment_operator -> SUBASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',54),
  ('assignment_operator -> MULASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',55),
  ('assignment_operator -> DIVASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',56),
  ('expression -> term','expression',1,'p_expression','Mparser.py',60),
  ('expression -> LPARENT expression RPARENT','expression',3,'p_expression','Mparser.py',61),
  ('expression -> expression ADD expression','expression',3,'p_num_expression_binary','Mparser.py',65),
  ('expression -> expression SUB expression','expression',3,'p_num_expression_binary','Mparser.py',66),
  ('expression -> expression MUL expression','expression',3,'p_num_expression_binary','Mparser.py',67),
  ('expression -> expression DIV expression','expression',3,'p_num_expression_binary','Mparser.py',68),
  ('expression -> expression DOTADD expression','expression',3,'p_num_expression_binary','Mparser.py',69),
  ('expression -> expression DOTSUB expression','expression',3,'p_num_expression_binary','Mparser.py',70),
  ('expression -> expression DOTMUL expression','expression',3,'p_num_expression_binary','Mparser.py',71),
  ('expression -> expression DOTDIV expression','expression',3,'p_num_expression_binary','Mparser.py',72),
  ('expression -> SUB expression','expression',2,'p_expression_negation','Mparser.py',76),
  ('expression -> expression TRANSPOSE','expression',2,'p_expression_transpose','Mparser.py',80),
  ('comparison -> expression comparison_operator expression','comparison',3,'p_comparison','Mparser.py',85),
  ('comparison_operator -> SMALLER','comparison_operator',1,'p_comparison_operator','Mparser.py',89),
  ('comparison_operator -> LARGER','comparison_operator',1,'p_comparison_operator','Mparser.py',90),
  ('comparison_operator -> SMALLEREQ','comparison_operator',1,'p_comparison_operator','Mparser.py',91),
  ('comparison_operator -> LARGEREQ','comparison_operator',1,'p_comparison_operator','Mparser.py',92),
  ('comparison_operator -> NOTEQ','comparison_operator',1,'p_comparison_operator','Mparser.py',93),
  ('comparison_operator -> EQ','comparison_operator',1,'p_comparison_operator','Mparser.py',94),
  ('call -> BREAK','call',1,'p_call','Mparser.py',98),
  ('call -> CONTINUE','call',1,'p_call','Mparser.py',99),
  ('call -> RETURN expression','call',2,'p_call','Mparser.py',100),
  ('call -> PRINT print_inputs','call',2,'p_call','Mparser.py',101),
  ('print_inputs -> print_inputs COMMA print_input','print_inputs',3,'p_print_inputs','Mparser.py',105),
  ('print_inputs -> print_input','print_inputs',1,'p_print_inputs','Mparser.py',106),
  ('print_input -> STRING','print_input',1,'p_print_input','Mparser.py',110),
  ('print_input -> ID','print_input',1,'p_print_input','Mparser.py',111),
  ('matrix_fun -> fun_name LPARENT expression RPARENT','matrix_fun',4,'p_matrix_fun','Mparser.py',115),
  ('fun_name -> EYE','fun_name',1,'p_fun_name','Mparser.py',119),
  ('fun_name -> ZEROS','fun_name',1,'p_fun_name','Mparser.py',120),
  ('fun_name -> ONES','fun_name',1,'p_fun_name','Mparser.py',121),
  ('loop -> for','loop',1,'p_loop','Mparser.py',125),
  ('loop -> while','loop',1,'p_loop','Mparser.py',126),
  ('for -> FOR for_expression instruction','for',3,'p_for','Mparser.py',130),
  ('for_expression -> ID ASSIGN range','for_expression',3,'p_for_expression','Mparser.py',134),
  ('while -> WHILE LPARENT comparison RPARENT instruction','while',5,'p_while','Mparser.py',138),
  ('branch -> IF LPARENT comparison RPARENT instruction','branch',5,'p_branch','Mparser.py',142),
  ('branch -> IF LPARENT comparison RPARENT instruction ELSE instruction','branch',7,'p_branch','Mparser.py',143),
  ('range -> num_term COLON num_term','range',3,'p_range','Mparser.py',147),
  ('term -> ID','term',1,'p_term','Mparser.py',151),
  ('term -> number','term',1,'p_term','Mparser.py',152),
  ('term -> matrix','term',1,'p_term','Mparser.py',153),
  ('term -> string','term',1,'p_term','Mparser.py',154),
  ('num_term -> ID','num_term',1,'p_num_term','Mparser.py',158),
  ('num_term -> number','num_term',1,'p_num_term','Mparser.py',159),
  ('matrix_term -> ID','matrix_term',1,'p_matrix_term','Mparser.py',163),
  ('matrix_term -> matrix','matrix_term',1,'p_matrix_term','Mparser.py',164),
  ('matrix_term -> number','matrix_term',1,'p_matrix_term','Mparser.py',165),
  ('number -> INT','number',1,'p_number','Mparser.py',169),
  ('number -> FLOAT','number',1,'p_number','Mparser.py',170),
  ('string -> STRING','string',1,'p_string','Mparser.py',174),
  ('matrix -> LSQBRACK matrix_contents RSQBRACK','matrix',3,'p_matrix','Mparser.py',178),
  ('matrix -> matrix_fun','matrix',1,'p_matrix','Mparser.py',179),
  ('matrix_contents -> matrix_contents COMMA matrix_content','matrix_contents',3,'p_matrix_contents','Mparser.py',183),
  ('matrix_contents -> matrix_content','matrix_contents',1,'p_matrix_contents','Mparser.py',184),
  ('matrix_content -> matrix_term','matrix_content',1,'p_matrix_content','Mparser.py',188),
]
