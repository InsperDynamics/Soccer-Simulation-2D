
class SoccerServerError(Exception):
    """
    Mensagem de erro retornada pelo servidor
    """

class SoccerServerWarning(Exception):
    """
    Mensagem de warning retornada pelo servidor
    """

class MessageTypeError(Exception):
    """
    Tipo de mensagem desconhecido recebido do servidor
    """

class AgentAlreadyPlayingError(Exception):
    """
    Usuário chamou o método play de um agente depois que ele já foi iniciado jogando
    """

class ObjectTypeError(Exception):
    """
    Tipo de objeto desconhecido é encontrado em uma mensagem de sense
    """

class AgentConnectionStateError(Exception):
    """
    Métodos foram chamados em um momento inadequado em relação ao estado de conexão do objeto do agente
    """

