import warnings
import erp.http


def application(environ, start_response):

    warnings.warn("The WSGI application entrypoint moved from "
                  "erp.service.wsgi_server.application to erp.http.root "
                  "in 15.3.",
                  DeprecationWarning, stacklevel=1)
    return erp.http.root(environ, start_response)
