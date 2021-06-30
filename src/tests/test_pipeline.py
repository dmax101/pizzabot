import pytest

from controller.pipeline import Pipeline


class TestClass:
    def test_mock_of_pipeline(self):
        pipeline = Pipeline()
        pipeline.on_start = False
        pipeline.on_greeting = False
        pipeline.on_choosing_products = False
        pipeline.on_transation_db = False
        pipeline.on_canceling_operation = True
        pipeline.on_end_operation = True
        pipeline.pedidos = []

        expected_message = "Finalizando sessão! Obrigado pela preferência!"

        message = ""
        while True:
            message = pipeline.start("test")["message"]
            if (
                message == "Operação cancelada pelo usuário"
                or message == "Finalizando sessão! Obrigado pela preferência!"
            ):
                break

        assert expected_message == message
