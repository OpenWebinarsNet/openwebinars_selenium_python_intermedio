Feature: Comprobar la direccion web
Descripcion de la feature actual

    Scenario: La URL es correcta
        Given Nos encontramos en google
        When Buscamos la cadena "wikipedia"
        Then La URL del primer resultado es "https://es.wikipedia.org/wiki/Wikipedia:Portada"


    Scenario: La URL es incorrecta
        Given Nos encontramos en google
        When Buscamos la cadena "facebook"
        Then La URL del primer resultado es "https://youtube.com"
