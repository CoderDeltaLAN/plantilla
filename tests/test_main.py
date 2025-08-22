from paquete_ejemplo.__main__ import main

def test_main_output(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hola desde paquete_ejemplo" in captured.out
