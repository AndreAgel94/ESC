import os

commandDict = {
    "add" : "C_ARITHMETIC",
    "sub" : "C_ARITHMETIC",
    "neg" : "C_ARITHMETIC",
    "eq" : "C_ARITHMETIC",
    "gt" : "C_ARITHMETIC",
    "lt" : "C_ARITHMETIC",
    "and" : "C_ARITHMETIC",
    "or" : "C_ARITHMETIC",
    "not" : "C_ARITHMETIC",
    "push" : "C_PUSH",
    "pop" : "C_POP"
}

segmentPointers = {
    "constant" : "SP",
    "local" : "LCL",
    "argument" : "ARG",
    "this" : "THIS",
    "that" : "THAT",
    "temp" : "5",
    "pointer" : "SP"
}

jumpDict = {
    "TRUE" : 0,
    "CONTINUE" : 0
}


def main():

    file_name = input("Informelocal e arquivo: ")

    if os.path.exists(file_name):
        
        try:
            
            file = open(file_name, 'r')
            lines = file.readlines()
            file.close()

            output_file = file_name.replace(".vm", ".asm")
            output_file = output_file.replace(".VM", ".asm")
            
            output_name = output_file.split("\\")
            segmentPointers["static"] = output_name[len(output_name) - 1].replace(".asm", "") + "."

            file = open(output_file, 'w')
            file.close()
            
            for line in lines:
                
                result = parse(line)

                if result == -1:
                    
                    print("O arquivo não pode ser traduzido! " +
                          "Por favor, verifique se não existem erros de sintaxe.")
                    return -1


                elif result != 0:

                    writed = codeWriter(output_file, result)

                    if  writed == -1:

                        return -1

            print("o arquivo foi traduzido")

        except IOError:
            
            print("erro no acesso ao arquivo")

    else:

        print ("o arquivo nao existe")

def parse(line):

    if line.find("//") != -1:

        line = line.split("//")[0]

    elements = line.replace("\n", "").split(' ')

    if elements[0] != '': #and elements[0] != "\n":

        if len(elements) != 1 and len(elements) != 3:

            return -1
        
        if elements[0] in commandDict:
            
            commandType = commandDict[elements[0]]
            result = [commandType]

        else:

            return -1
                
        if commandType != "C_RETURN":

            if commandType == "C_ARITHMETIC":

                arg1 = elements[0]

            else:

                arg1 = elements[1]

            result.append(arg1)
            arg2CallList = ["C_PUSH", "C_POP"]

            if commandType in arg2CallList:

                arg2 = elements[2]
                result.append(arg2)

            return result
    else:

        return 0

def codeWriter(output_file, arguments):
    
    if arguments[0] == "C_ARITHMETIC":

        output = writeArithmetic(arguments[1])

    elif arguments[0] ==  "C_PUSH" or arguments[0] ==  "C_POP":

        output = writePushPop(arguments[0], arguments[1], arguments[2])

    if output == -1:

        return -1

    try:
        
        file = open(output_file, 'a')

        for line in output:

            file.writelines(line)

        file.close()

        return 0
    
    except IOError:
        
        print ("nao foi possivel traduzir o arquivo")
        return -1

def writeArithmetic(command):
    output = ["//" + command + "\n"]
    if command == "neg" or command == "not":
        output.append("@SP\n")
        output.append("A=M-1\n")

        if command == "neg":   
            output.append("M=-M\n")
        else:
            output.append("M=!M\n")

        return output

    else:
        output.append("@SP\n")
        output.append("M=M-1\n")
        #output.append("@SP\n")
        output.append("A=M-1\n")
        output.append("D=M\n")
        output.append("@SP\n")
        output.append("A=M\n")

        if command == "add":

            output.append("D=D+M\n")

        elif command == "sub":

            output.append("D=D-M\n")

        elif command == "and":

            output.append("D=D&M\n")

        elif command == "or":

            output.append("D=D|M\n")

        else:
            
            if command == "eq":

                output.append("D=D-M\n")
                output.append("@TRUE_" + str(jumpDict["TRUE"]) + "\n")
                output.append("D; JEQ\n")
            
            elif command == "gt":

                output.append("D=D-M\n")
                output.append("@TRUE_" + str(jumpDict["TRUE"]) + "\n")
                output.append("D; JGT\n")

            elif command == "lt":

                output.append("D=D-M\n")
                output.append("@TRUE_" + str(jumpDict["TRUE"]) + "\n")
                output.append("D; JLT\n")

            else:

                return -1

            output.append("D=0\n")
            output.append("@CONTINUE_" + str(jumpDict["CONTINUE"]) + "\n") 
            output.append("0; JMP\n")
            output.append("(TRUE_" + str(jumpDict["TRUE"]) + ")\n")
            output.append("D=-1\n")
            output.append("(CONTINUE_" + str(jumpDict["CONTINUE"]) + ")\n")

            jumpDict["TRUE"] = jumpDict["TRUE"] + 1
            jumpDict["CONTINUE"] = jumpDict["CONTINUE"] + 1
        
        output.append("@SP\n")
        output.append("A=M-1\n")
        output.append("M=D\n")

        return output
    
def writePushPop(command, segment, index):

    output = ["//" + command + " " + segment + " " + index + "\n"]

    if command == "C_PUSH":
                
        if segment == "constant" or segment == "pointer":

            if segment == "pointer":

                if index == '0':

                    output.append("@THIS\n")

                elif index == '1':

                    output.append("@THAT\n")

                else:

                    print("Erro de sintaxe")
                    return -1
                
                output.append("D=M\n")

            else:
                
                output.append("@" + str(index) + "\n")
                output.append("D=A\n")


        else:

            if segment == "temp":

                output.append("@" + str(int(segmentPointers[segment]) + int(index)) + "\n")
                output.append("D=M\n")

            elif segment == "static":
            
                output.append("@" + segmentPointers[segment] + str(index) + "\n")
                output.append("D=M\n")
                
            else:

                output.append("@" + str(index) + "\n")
                output.append("D=A\n")
                output.append("@" + segmentPointers[segment] + "\n")
                output.append("A=D+M\n")
                output.append("D=M\n")


            
        output.append("@SP\n")
        output.append("A=M\n")
        output.append("M=D\n")
        output.append("@SP\n")
        output.append("M=M+1\n")

        return output

    else:

        if segment == "static":

            output.append("@SP\n")
            output.append("M=M-1\n")
            output.append("@SP\n")
            output.append("A=M\n")
            output.append("D=M\n")
            output.append("@" + segmentPointers[segment] + str(index) + "\n")
            output.append("M=D\n")

            return output
        elif segment == "pointer":
            if index == '0':
                i = "THIS"

            elif index == '1':
                i = "THAT"
            else:

                print("Erro de sintaxe")
                return -1

            output.append("@SP\n")
            output.append("M=M-1\n")
            output.append("A=M\n")
            output.append("D=M\n")
            output.append("@" + i + "\n")
            output.append("M=D\n")

            return output
        
        elif segment == "temp":

            output.append("@" + str(int(segmentPointers[segment]) + int(index)) + "\n")
            output.append("D=A\n")
            output.append("@tempVariable\n")
            output.append("M=D\n")
            output.append("@SP\n")
            output.append("M=M-1\n")
            output.append("A=M\n")
            output.append("D=M\n")      
            output.append("@tempVariable\n")
            output.append("A=M\n")
            output.append("M=D\n")
            output.append("@tempVariable\n")
            output.append("M=0\n")

            return output

        else:
            
            output.append("@" + str(index) + "\n")
            output.append("D=A\n")
            output.append("@" + segmentPointers[segment] + "\n")
            output.append("D=D+M\n")
            output.append("@tempVariable\n")
            output.append("M=D\n")
            output.append("@SP\n")
            output.append("M=M-1\n")
            output.append("A=M\n")
            output.append("D=M\n")      
            output.append("@tempVariable\n")
            output.append("A=M\n")
            output.append("M=D\n")
            output.append("@tempVariable\n")
            output.append("M=0\n")

            return output
main()