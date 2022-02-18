using System.Diagnostics;

namespace App {

    struct Carrinho {
        public double preco { get; }
        public int quantidade { get; }

        public Carrinho(double preco, int quantidade) {
            this.preco = preco;
            this.quantidade = quantidade;
        }
    }

    class App {
        static public void Main(String[] args) {
            String? linha;
            List<Carrinho> carrinhos = new List<Carrinho>();
            
            while ((linha = Console.ReadLine()) != null) {
                var dados = linha.Split("\t");
                double preco;
                int quantidade;

                double.TryParse(dados[0], out preco);
                int.TryParse(dados[1], out quantidade);

                carrinhos.Add(new Carrinho(preco, quantidade));
            }

            Stopwatch sw = Stopwatch.StartNew();
            double media = CalculoLoop(carrinhos);
            sw.Stop();

            Console.WriteLine($"Tempo Calculo: {sw.ElapsedMilliseconds/1000.0}");
            Console.WriteLine(media);
        }

        static public double CalculoLoop(List<Carrinho> carrinhos) {
            double total = 0;
            foreach (var carrinho in carrinhos) {
                total += carrinho.preco * carrinho.quantidade;
            }
            return total/carrinhos.Count;
        }
    }
    
}


