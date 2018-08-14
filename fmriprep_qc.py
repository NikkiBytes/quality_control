import glob
import os

path="/projects/niblab/bids_projects/Experiments/BBx"
outfile=os.path.join(path, "BBx_ses-1_QC_fmriprep.html")
os.remove(outfile)
f = open(outfile, 'w')
subjects = glob.glob(os.path.join(path, 'fmriprep', 'ses-1', 'sub-*'))
for sub in subjects:
        print("SUBJECT ---------------------------> ", sub)
        f.write("SUBJECT ID: %s"%sub)
        svg_path = os.path.join(sub, 'fmriprep', 'sub-*', 'figures', '*svg')
        svgs = glob.glob(svg_path)
        #print(svgs)
        for svg in svgs:
            #print(svg)
            if "T1w" in svg:
                print("WRITING ANATOMICAL FILES TO HTML >>>>>>>>> ", svg.split("/")[-1])
                f.write("ANATOMICAL \n")
                f.write("<IMG SRC=\"%s\">"%svg)
f.close()
