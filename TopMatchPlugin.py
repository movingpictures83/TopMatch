import os
class TopMatchPlugin:
    def input(self, filename):
       infile = open(filename, 'r')
       self.genescores = set()
       for line in infile:
           contents = line.strip().split('\t')
           #if ((float(contents[2]), contents[1]) not in self.genescores):
           self.genescores.add((float(contents[2]), contents[1]))

    def run(self):
       self.genescorelist = list(self.genescores)
       self.genescorelist.sort()
       self.genescorelist.reverse()

    def output(self, filename):
       #outfile = open(filename, 'w')
       # Top ten, future make flexible
       maxscore = self.genescorelist[0][0]
       maxgene = self.genescorelist[0][1]
       #gi|998213302|gb|CP014343.1|
       #gbname = maxgene.split("|")
       #print("Maxgene: "+gbname[3])
       #os.system("esearch -db nucleotide -query \""+gbname[3]+"\" | efetch -format fasta > "+filename)

       #outfile.write("Gene\tScore\n")
       i = 0
       while (self.genescorelist[i][0] == maxscore):
               gbname = self.genescorelist[i][1].split("|")
               print("Gene: "+gbname[3])
               os.system("esearch -db nucleotide -query \""+gbname[3]+"\" | efetch -format fasta > "+filename+"/"+gbname[3]+".fasta")
               i += 1
#       outfile.write(self.genescorelist[i][1]+"\t"+str(self.genescorelist[i][0])+"\n")
