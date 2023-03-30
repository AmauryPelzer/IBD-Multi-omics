
#1- Get pathways based on all ECs we have, while querying try to use all ECs or one by one
#2- Enrichment and Testing  from https://pypi.org/project/keggtools/ will be done 
#3- See the results
#optional see how to get metabolites from KEGG

from Bio.KEGG import REST
from Bio.KEGG import Enzyme
request = REST.kegg_get("ec:5.4.2.2")
open("ec_5.4.2.2.txt", "w").write(request.read())
records = Enzyme.parse(open("ec_5.4.2.2.txt"))
record = list(records)[0]
#print (record)
#print (record.classname)
#print (record.entry)
print (record.pathway)


#human_pathways = REST.kegg_list("pathway", "eco").read()
#print(human_pathways)


from keggtools import Enrichment

# Add pathway object to list
pathway_list = []

# Init analysis with organism code
analysis = Enrichment(pathways=pathway_list)

# Study genes as list of entrez gene id's
study_genes = []
analysis.run_analysis(gene_list=study_genes)

# to_dataframe method requires pandas installation
result = analysis.to_dataframe()
print(result.head())