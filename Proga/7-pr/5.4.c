#include <stdio.h>
#include <string.h>

#define w 50

//Разделение слов
int split(char text[], char words[][w]) {
    int count = 0;
    char *word = strtok(text, " "); //разделение строки на слова

    while (word != NULL && count < w) { //пока слова не закончатся
        strcpy(words[count], word); //копирование в массив
        count++; // +1 слово
        word = strtok(NULL, " "); //переход к след слову
    }

    return count; //кол-во слов
}

//Сравнение слов
int compare(char a[], char b[]) {
    return strcmp(a,b); 
}

//Обмен слов местами
void swap(char a[], char b[]) {

    char temp[w];
    // a = 'слово', b = 'word'
    strcpy(temp, a); // temp = 'слово' 
    strcpy(a, b); // a = 'word'
    strcpy(b, temp); // b = 'слово'
}

//Обмен слов по алфавиту
void sort(char words[][w], int count) {

    for (int i = 0; i < count - 1; i++) { 
        for (int j = 0; j < count - 1 - i; j++) {
            if (compare(words[j], words[j + 1]) > 0) {
                swap(words[j], words[j + 1]);
            }
        }
    }

}

//Вывод
void printWords(char words[][w], int count) {
    printf("Words: ");

    for (int i = 0; i < count; i++) {
        printf("%s ", words[i]);
    }
    printf("\n");

    printf("Count words: %d\n", count);
}

int main() {
    char text[] = "orange apple banana kiwi";
    char words[w][w];

    int count = split(text, words);
    sort(words, count);
    printWords(words, count);

    return 0;
}
