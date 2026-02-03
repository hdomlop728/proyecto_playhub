import time
import logging

logger = logging.getLogger("request_logger")

class juegos_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        inicio = time.time()
        respuesta = self.get_response(request)
        duracion = (time.time() - inicio) * 1000

        usuario = getattr(request, "user", None)
        username = usuario.username if usuario and usuario.is_authenticated else "anonymous"

        logger.info(
            "%s %s user=%s time_ms=%.2f status=%s",
            request.method,
            request.path,
            username,
            duracion,
            getattr(respuesta, "status_code", "n/a"),
        )
        return respuesta
