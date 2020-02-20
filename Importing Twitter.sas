proc datasets noprint lib=work kill;
run;
quit;
proc import out=twitter datafile="C:\Users\Daniel chacreton\Documents\Coding\Social-Media-Data-Project\Twitter Results\HIV Final Search Terms_2020-02-16.txt"
dbms=csv replace;
delimiter = "~]";
run;

proc freq data = twitter;
tables location;
run;
