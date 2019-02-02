#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <time.h>
using namespace std;
#define IdxMin 0
#define IdxMax 4
char Op[IdxMax] = {'*','+','/','-'} ;/* Berisi Array Operator + - / * () */
double Num[IdxMax]; /* Berisi Array yang akan dimasukkan pada program */


double ev (char op, double a, double b) { /* Fungsi empat operasi aritmatika yang digunakan pada program utama */
  if (op == '+') return (double)a+b;
  else if (op == '-') return (double)a-b;
  else if (op == '/') {
    if (b != 0) return (double)a/b;
  }
  else if (op == '*') return (double)a*b;
}

int Conv (char op) {
  if (op == '+') return 5;
  else if (op == '-') return 4;
  else if (op == '*') return 3;
  else if (op == '/') return 2;
}

int main () {
  int score;
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  clock_t Mulai = clock(); //Waktu Dimulai
  FILE *outfile;
  outfile = fopen("EnumNumberSortFinal.csv","w");
  fprintf(outfile,"Ekspresi, Skor\n");
  int i,j,k ; int no = 0; int Hsl = 24; double EPS = 0.0000000001; // EPS digunakan untuk membandingkan double dengan 24 (Hsl), karena menyangkut presisi
  for (int Num1 = IdxMin+1 ; Num1 <= 13 ; Num1++) {
    Num[0] = Num1;
    for (int Num2 = IdxMin+1; Num2 <= 13; Num2++){
       Num[1] = Num2;
      for(int Num3 = IdxMin+1; Num3 <= 13 ; Num3++) {
        Num[2] = Num3;
        for (int Num4 = IdxMin+1 ; Num4 <= 13; Num4++) {
          Num[3] = Num4;
            for (i = IdxMin ; i < IdxMax ; i++) {// Mengenerate semua kemungkinan operator di posisi pertama
              no = 0;
              for (j = IdxMin ; j < IdxMax ; j++) { // Mengenerate semua kemungkinan operator di posisi kedua
                for (k = IdxMin; k < IdxMax ; k++) { // Mengenerate semua kemungkinan operator di posisi ketiga

                  if (fabs(ev(Op[k], (ev(Op[j], (ev(Op[i],Num[0], Num[1])), Num[2])), Num[3]) -Hsl) <= EPS) { // ((a op b) op c) op d
                    no++;
                    cout  << "((" << Num[0] << Op[i] <<  Num[1] << ")" << Op[j]  << Num[2] << ")" << Op[k] << Num[3] << endl;
                    score = Conv(Op[i]) + Conv(Op[j]) + Conv(Op[k]) -2 ;
                    fprintf(outfile,"((%.00f%c%.00f)%c%.00f)%c%.00f,%d\n",Num[0],Op[i],Num[1],Op[j],Num[2],Op[k],Num[3],score);
                  }
                  if (fabs(ev(Op[k], (ev( Op[i], Num[0], (ev(Op[j],Num[1], Num[2])) ) ) , Num[3])- Hsl) <= EPS) { // (a op (b op c)) op d
                    no++;
                    cout << "(" << Num[0] << Op[i] << "("  << Num[1]  << Op[j]  << Num[2] << "))" << Op[k] << Num[3] << endl;
                    score = Conv(Op[i]) + Conv(Op[j]) + Conv(Op[k]) -2 ;
                    fprintf(outfile,"(%.00f%c(%.00f%c%.00f))%c%.00f,%d\n",Num[0],Op[i],Num[1],Op[j],Num[2],Op[k],Num[3],score);
                  }
                  if (fabs(ev(Op[j],ev(Op[i], Num[0], Num[1]), ev(Op[k], Num[2], Num[3])) - Hsl ) <= EPS) { // (a op b) op (c op d)
                    no++;
                    cout << "(" << Num[0] << Op[i]   << Num[1]  << ")" << Op[j]  << "(" << Num[2] << Op[k] << Num[3] << ")" << endl;
                    score = Conv(Op[i]) + Conv(Op[j]) + Conv(Op[k]) -2 ;
                    fprintf(outfile,"(%.00f%c%.00f)%c(%.00f%c%.00f),%d\n",Num[0],Op[i],Num[1],Op[j],Num[2],Op[k],Num[3],score);
                  }
                  if (fabs(ev(Op[i],Num[0],ev(Op[k],ev(Op[j],Num[1],Num[2]), Num[3])) - Hsl) <= EPS) { // a op ((b op c) op d)
                    no++;
                    cout << Num[0] << Op[i] << "(("  << Num[1]  << Op[j]  << Num[2] << ")" << Op[k] << Num[3] << ")" << endl;
                    score = Conv(Op[i]) + Conv(Op[j]) + Conv(Op[k]) -2 ;
                    fprintf(outfile,"%.00f%c((%.00f%c%.00f)%c%.00f),%d\n",Num[0],Op[i],Num[1],Op[j],Num[2],Op[k],Num[3],score);
                  }
                  if (fabs(ev(Op[i],Num[0],ev(Op[j],Num[1],ev(Op[k], Num[2],Num[3]))) - Hsl) <= EPS) { // a op (b op (c op d))
                    no++;
                    cout << Num[0] << Op[i] << "("  << Num[1]  << Op[j]  << "("  <<  Num[2]  << Op[k] << Num[3] << "))" << endl;
                    score = Conv(Op[i]) + Conv(Op[j]) + Conv(Op[k]) -2 ;
                    fprintf(outfile,"%.00f%c(%.00f%c%.00f(%c%.00f)),%d\n",Num[0],Op[i],Num[1],Op[j],Num[2],Op[k],Num[3],score);
                  } // Terdapat lima buah if-condition yang berguna untuk meletakkan semua kemungkinan '(' dan ')'
                }
              }
            }
            if (no == 0) {
              fprintf(outfile,",0,%.00f %.00f %.00f %.00f,Tidak menghasilkan 24\n",Num[0],Num[1],Num[2],Num[3]);
            }
        }
      }
    }
  }
  fclose(outfile);
  printf("Waktu Berjalan : %.2fs\n", (double)(clock() - Mulai)/CLOCKS_PER_SEC); //Waktu Berjalan
  return 0;
}
