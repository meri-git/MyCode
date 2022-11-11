################# Add a column to a file #################################################
awk 'BEGIN {IGNORECASE=1} END {print r} r && !/^[a-z]/ {print r; r = ""} {r r ? r $0: $0}' file1.dat > file1.dat.new

################# delete a particular single line with its line number. ##################
################# This will delete the 33rd line and save the updated file. ##############
sed -i '33d' file.dat

################# Unix Calculator (numberA numberB operation) ############################
echo '1135423480 568 / p' | dc

################# This will give you the unique items that exist in A but not in B: ######
cat A perl -ne '$z=$_; chomp ($z); $y=`grep $z B`; if ($y== "") {print "\n$z";}' | sort -u file

################# This will give you the list of common items in both A and B: ###########
cat A xargs -i grep {} B|sort -u

################# Add single quotes around a column in unix file #########################
sed -e s/^/\'/ -e s/$/\'/ input.txt > output.txt

################# grep gz file ###########################################################
zgrep -Ec "$" file.dat.gz

################# grep and count empty lines in a file ###################################
grep -c "^$" file.dat

################# grep gz file ###########################################################
zgrep -Ec "$" file.dat.gz

################# ADD A COLUMN TO END OF REC LAYOUT ######################################
awk 'BEGIN { OFS = "," } {print $0, ""}' abc.csv > abc_new.csv

################# GROUP BY IN DATA FILE ##################################################
cut -d $'\004' -f1 abc.dat | sort | uniq -c | sort -rh | head -1

################# REMOVE LOAD EVENT ID FROM FILE NAME ####################################
find . -depth name "DAT*" -exec sh-C 'f=" {}"; mv -- "$f" "${f%DAT* }DAT"' \;

################# SORT FILE LIST BASED ON DATES IN FILE NAME #############################
ls | awk -F'[_]' '{print $7, $0}' | sort | sed -e 's/^[0-9]* //'.

################# ZIP FILES THAT ARE NO ZIPPED YET #######################################
gzip *[!.gz]

################# Check length of fixed width file #######################################
awk '{ print (length($0))}' ABC.DAT | sort | uniq -c || sort -rh head -20

################## Delete a row in file ##################################################
sed -i '66d' abc.dat;

################## Grep many items in a single command ###################################
egrep -ins "7442040035404744709780026820132526743004728|025125178140019510931145065003461984" abc.dat

################## Find a file in directory tree #########################################
find . -name file_name* -print | egrep '100229136100229135|100229133100229097|10022 9062|100229057100229059'

################# Find a file in directory ###############################################
find /vol/path -name "file_name_pattern*" -print

################# show unique records ####################################################
sort {file} | uniq -d | wc -1

################# Count of files in directory ############################################
find .//. ! -name . -print | grep -c

################# replace a string in a file (using sed ##################################
sed -i 's/20160511/20160505/g' sbc.dat

################# Update a string in file (update  data_as_of_dt in file #################
sed ""s@^$PRD_END_DT^D@ $PRD_END_DT_1^D@q"" file1.d.SPRD_END_DT_1.dat.prod > file1.d.SPRD_END_DT_1.dat

################# convert Dos file to Unix formatiing ####################################
dos2unix <filename.dat>

################# convert Unicode characters to ASCII ####################################
iconv -f unicode -t ascii oldfile > newfile

################# Convert UTF characters to ASCII ########################################
iconv -f utf8 -t ascii oldfile > newfile

################# Check space consumed system ############################################
df -kht /vol/path/

################# Disk usage in a particular diectory ####################################
du -sh

################# untar a file ###########################################################
tar --strip-components=3 -xvf <TAR file name>

################# tar multiple files #####################################################
tar cf 2015_XTCI_files.tar *2015*

################# view files contained in tarball ########################################
tar tf 2013_XTCI_files.tar

################# top 10 directories occupying most space; cd into the directory #########
du -hsx* | sort -rh | head -10

################# To check no. of columns of a file in Linux #############################
gawk -F "delimeter" '{print NF;exit}' FILE NAME

################# SCP a file from Prod to dev server  ####################################
scp user@serverprod:/home/prod/file_name.TAR user@serverdev:/home/dev/data/

################# Count number of delimiters (^D) in each row of file ####################
awk -F ^D '{print NF-1}' filename.dat

################# Get byte length of each record in a file ###############################
awk '{print length+1}' filename.dat

################# Extract 100th row from a file into another file ########################
awk 'NR ==100' /dev/data/filename.dat >> ~/filenamel.dat

################# Extract 100th from a file into another file to 105th row ###############
awk 'NR >= 100 && NR <= 105' /dev/data/filename.dat >> ~/filenamel.dat

################# Count number of fields in each row of file #############################
awk -F '^D' '{print NF}' file1.dat

################# scp files from a list file #############################################
xargs -a /home/gupta2/tables.list | xargs -i scp {} server_name:/vol/path/file1

################# grep special characters in Unix file ###################################
grep --color='auto' -P -n "[^\x00-\x7F]" filel.dat

######## ######## Cut and combine columns from fixed width file ##########################
awk '{OFS="~"}; {print substr($1,1,2), substr($1,3,4), substr($1,8,2), s ubstr($1,10,4), substr($1,15,8), substr($1,30,2)}' file.DAT | sort | uniq -c sort -rh > ~/file.DAT.uniq_keys

################# Sort delimited file based on a column ##################################
sort -t"|" -k17,17 file1.dat

################# Grep the last non-empty line of multiple files #########################
for file in abc*20200807*.log; do awk '/./{line=$0} END {print FILENAME, line}' "$file"; done | grep "DataBaseConnect" 
for file in /vol/path/abc*`date '+%Y%m%d'`*.log; do awk '/./{line=$0} END{print FILENAME, line}' "$file"; done | grep "DataBaseConnect"

################# Pad fixed width file to desired length #################################
awk '{printf "%-400s\n", $0}' oldfile.txt > newfile.txt

################# Sum up column in a delimited file ######################################
gawk -F'|' { sum += $39 } END{ print s }' file.dat

