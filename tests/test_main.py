import sys
from io import StringIO
from paquete_ejemplo.__main__ import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hola desde paquete_ejemplo" in captured.out

