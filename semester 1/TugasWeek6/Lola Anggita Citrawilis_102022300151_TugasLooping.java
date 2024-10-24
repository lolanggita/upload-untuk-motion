public class TugasLooping {
    public static void main(String[] args) {
        int n = 2;
        int count = 0;
        int jumlah = 0;
        int Maximum = Integer.MIN_VALUE;
        int Minimum = Integer.MAX_VALUE;

        while (n <= 15) {
            int angka = n;
            jumlah += angka;
            count++;
            n++;

            if (angka > Maximum) {
                Maximum = angka; 
            }

            if (angka < Minimum) {
                Minimum = angka; 
            }

        }

        double rataRata = (double) jumlah / count; // Hitung rata-rata (menggunakan pembagian floating point)

        System.out.println("Nilai Maksimum: " + Maximum);
        System.out.println("Nilai Minimum: " + Minimum);
        System.out.println("Rata-rata: " + rataRata);
    }
}
