from tqdm import tqdm
from glob import glob
import json

associates = """Jonathan Abbatt (University of Toronto), Igor Adameyko (Medical University of Vienna/ Karolinska Institutet), Laura Airoldi (University of Padova), Kwasi Appeaning Addo (University of Ghana), Lisa Ainsworth (USDA ARS), Julia Baum (University of Victoria), Peter Bijl (Utrecht University), Barbara Block (Stanford University), Gabriel Bowen (University of Utah), Jérôme Chave (CNRS), John C. H. Chiang (University of California, Berkeley), Peter U. Clark (Oregon State University), Julia Clarke (University of Texas at Austin), Henk A. Dijkstra (Utrecht University), Philip Donoghue (University of Bristol), Robert Dunbar (Stanford University), Noah Fierer (University of Colorado), Erich Fischer (ETH Zurich), Baylor Fox-Kemper (Brown University), Kevin Furlong (Pennsylvania State University), Glenn Gaetani (Woods Hole Oceanographic Institution), Jim Gaherty (University of Northern Arizona), Paul A. Garber (University of Illinois at Urbana-Champaign), Alessandra Giannini (Ecole normale supérieure, Paris), Darryl Granger (Purdue University), Mark Hay (Georgia Institute of Technology), Michael Hochberg (Institute of Evolutionary Sciences, University of Montpellier), Fumio Inagaki (Japan Agency for Marine-Earth Science and Technology), Jennifer Jacquet (University of Miami), Rachel Klima (Johns Hopkins University), Raphael Kudela (UC Santa Cruz), Paul Kushner (University of Toronto), Yonglong Lu (Chinese Academy of Science), Dario Lupiáñez (Max Delbrück Center for Molecular Medicine), Pablo Marquet (Pontificia Universidad Catolica de Chile), Douglas McCauley (University of California, Santa Barbara), Monica Medina (Pennsylvania State University), Jack Middelburg (Utrecht University, The Netherlands), Anne Hélène Monsoro-Burq (Institut Curie), Sarah O’Connor (Max Planck Institute), Stephanie Pierce (Harvard University), Thorsten Reusch (GEOMAR Helmholtz Center for Ocean Research Kiel), Dustin Rubenstein (Columbia University), Roberta L. Rudnick (University of California, Santa Barbara), Lynn M. Russell (Scripps Institution of Oceanography, UCSD), Evan Scannapieco (Arizona State University), Blair Schoene (Princeton University), Arnau Sebé-Pedrós (Centre for Genomic Regulation/CRG), Bertrand Servin (INRA), Tiffany Shaw (University of Chicago), Neil Shubin (University of Chicago), Robert Steneck (University of Maine), Rashid Sumaila (Institute for the Oceans and Fisheries & School for Policy and Global Affairs, University of British Columbia), Pierre Taberlet (LECA, Grenoble), Cedric Tan (University of Oxford), Susannah Tringe (The U.S. Department of Energy Joint Genome Institute), Andreas Wagner (University of Zurich, IEU), Ellen Wohl (Colorado State University), Rachel Wood (University of Edinburgh), Shang-Ping Xie (University of California, San Diego), Yi Yin (New York University), Feifei Zhang (Nanjing University), Jin Zhang (Texas A&M University), Xin Zhou (China Agricultural University), Zhonghe Zhou (Institute of Vertebrate Paleontology and Paleoanthropology)"""


def splitter(x):
    return [f"{r.strip()})" for r in x.split("),")]


if __name__ == "__main__":
    table = str.maketrans("() /", "[]__")
    with open("README.md", "w") as output:
        for editor in tqdm(splitter(associates)):
            file = f"res/{editor.translate(table)}.json"
            with open(file, "r") as js:
                res = json.load(js)

            fname = file.removesuffix(".json").removeprefix("res/").translate(table)
            output.write(f"## {editor}\n")

            for r in res["organic_results"][:3]:
                t = r["title"]
                blurb = r["snippet"]
                l = r["link"]
                output.write(f" - [{t}]({l}) : {blurb}  \n")

            output.write("\n\n")
