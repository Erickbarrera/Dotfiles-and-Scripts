++ Template
    By Erick Barrera
 */



#include <stdio.h>
#include <getopt.h>


void printFilename();
void getopt();
char  *filename;

int main(int argc, char *argv[]){

    int opt;
    int cflag = 0;
    int oflag = 0;

    while ((opt = getopt (argc, argv, "co")) != -1) {
        switch (opt) {
            case 'c':
                cflag = 1;
                printf("Option c On\n");
                break;
            case 'o':
                oflag = 1;
                printf("Option o on\n");
                break;
            default:
                //Default action for unknown option
                printf("Option not recognized\n");
                break;
        }

        //if argument is not an option, it is the filename
        //so set the filename to the non-option argument
        if (optind < argc) {
            int i;
            for (i = 0; i < argc; i++){
                filename = argv[optind];
            }
        }
    }
    if(cflag == 1){
        //c flag stuff here
    }

    if(oflag == 1 ){
      printFilename(); /
    }
}



//this will be your write to file function
void printFilename(){
    printf("%s",filename);
    printf("\n");
}

