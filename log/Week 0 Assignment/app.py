import hashlib

def main():
    with open("INPUT.txt", "r") as infile:
        data = infile.read().strip().split("\n") 
    user_data = data[0].split(" - ")
    user_data[1] = hashlib.sha256(user_data[1].encode()).hexdigest()

    year_seq = 0
    month_seq = 0
    current_year = ""
    sks_count = 0
    
    with open("{} - {}.txt".format(user_data[0],user_data[1]),"w") as outfile:
        for row in data:
            if "Tahun Ajaran" in row and row.split()[2] != current_year:
                year_seq += 1
                month_seq = 1
                current_year = row.split()[2]
                sks_count = 0
            elif "Tahun Ajaran" in row and row.split()[2] == current_year:
                month_seq += 1
                sks_count = 0
            elif "Disetujui" in row:
                course_data = row.split("\t")
                sks_count += int(course_data[5])
                outfile.write("{}{} {} {} {:2} {:2}\n".format(year_seq,
                                                          month_seq,
                                                          course_data[1].strip(),
                                                          course_data[5].strip(),
                                                          course_data[8].strip(),
                                                          sks_count
                                                            ))



if __name__ == "__main__":
    main()
