#with open('output.txt', 'w') as file:
#    while True:
#        user_input = input("Vvedite stroki (pustaya stroka - konets zapisi): ")
#        if not user_input:
#            break
#        file.write(user_input + '\n')
#print("Zapis' zavershena.")


#file_name = input("Vvedite imya fayla: ")

#try:
    
#    with open(file_name, 'r') as file:
        
#        line_number = 1

        
#        for line in file:
#            print(f"{line_number}: {line.strip()}")
#            line_number += 1
#except FileNotFoundError:
#    print(f"Fayl '{file_name}' ne nayden.")
#except Exception as e:
#    print(f"Proizoshla oshibka: {e}")


#with open(input_file, 'r') as file:
#        lines = file.readlines()

#    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

#    for i, chunk in enumerate(chunks):
#        output_file_name = f"part_{i + 1}.txt"
#        with open(output_file_name, 'w') as output_file:
#            output_file.writelines(chunk)

#file_name = input("Vvedite imya fayla: ")
#try:
#    chunk_size = int(input("Vvedite tseloye chislo N: "))
#    split_file(file_name, chunk_size)
#    print(f"Fayl '{file_name}' byl razdelen na chasti po {chunk_size} stroki(i).")

#except FileNotFoundError:
#    print(f"Fayl '{file_name}' ne nayden.")


#def merge_files(output_file, input_files):
#    with open(output_file, 'w') as output:
#        for file_name in input_files:
#            with open(file_name, 'r') as file:
#                output.write(file.read())


#output_file = input("Vvedite imya vykhodnogo fayla: ")
#input_files = input("Vvedite imena faylov dlya ob'yedineniya (cherez probel): ").split()

#try:
#    merge_files(output_file, input_files)
#    print(f"Fayly uspeshno ob'yedeniny v '{output_file}'.")
#except Exception as e:
#    print(f"Error: {e}"




