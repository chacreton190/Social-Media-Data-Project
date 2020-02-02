*FILENAME TEMP "C:\Users\Daniel chacreton\Documents\Coding\Social-Media-Data-Project\Twitter Results\HIV Key Words_2020-02-01.txt" encoding="utf-8";
PROC IMPORT OUT = TET DATAFILE = "C:\Users\Daniel chacreton\Documents\Coding\Social-Media-Data-Project\Twitter Results\HIV Key Words_2020-02-01.txt"
DBMS= dlm replace;
DELIMITER="~]";
RUN;
