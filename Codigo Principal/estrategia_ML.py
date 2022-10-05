modelo = None

def queryModel(game_state):
    global modelo
    # dado o modelo e o game_state, retorna a estimativa de acao para TODOS os jogadores
    return modelo.predict(game_state)