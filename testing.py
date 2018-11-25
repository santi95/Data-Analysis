import unittest
import consultas
from random import randint, choice
import datos
import errores

class PruebaConsultas(unittest.TestCase):

    def setUp(self):
        self.int = 0
        self.string = 'string'
        self.genoma_malo =str(5) + "lllll" + str(2) + 'll' + "".join([choice(['A', 'C', 'T', 'G']) for i in range(852)])
        self.genoma_bueno = datos.personas[0].genoma

    def tearDown(self):
        self.genoma_malo = self.genoma_bueno

    def test_ascendencia(self):
        self.assertEqual(consultas.ascendencia(0), ['Albina'])
        self.assertEqual(consultas.ascendencia(2), ['Albina'])
        #self.assertRaises(errores.NotAcceptable('Ascendencia'), consultas.ascendencia, 9)

    def test_índice_de_tamaño(self):
        self.assertEqual(consultas.índice_de_tamaño(0), 0.0)
    def test_pariente_de(self):
        self.assertEqual(consultas.pariente_de(1, consultas.id_getter("Tomas Salvadores")), ['Emilio Gabriele'])
    def test_gemelo_genético(self):
        pass
    def test_valor_característica(self):
        self.assertEqual(consultas.valor_característica('TAG', 'Fernando Florenzano'), ['Daltonismo', 'Miopía'])
    def test_min(self):
        self.assertEqual(consultas.min('GTC'), 'Verdes')
        self.assertEqual(consultas.min('GTC'), 'Verdes')
    def test_max(self):
        self.assertEqual(consultas.max('GTA'), 'Aguileña')
    def test_prom(self):
        self.assertEqual(consultas.prom('CTC'), 41.163636363636364)


if __name__ == "__main__":
    unittest.main()
