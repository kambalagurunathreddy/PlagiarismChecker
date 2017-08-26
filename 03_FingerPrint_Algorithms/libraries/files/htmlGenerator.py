import os
def htmlGenerator(matrix,absfilepath,title="Plagiarism Checker"):
    f=open(absfilepath,"w")
    hCode1=r'<style type="text/css">.tg  {border-collapse:collapse;border-spacing:0;border-color:#aaa;margin:0px auto;}.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aaa;color:#333;background-color:#fff;}.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aaa;color:#fff;background-color:#f38630;}.tg .tg-j2zy{background-color:#FCFBE3;vertical-align:top}.tg .tg-e3zv{font-weight:bold}.tg .tg-9hbo{font-weight:bold;vertical-align:top}.tg .tg-3jhu{background-color:#FCFBE3;font-weight:bold}.tg .tg-z2zr{background-color:#FCFBE3;text-align:right}.tg .tg-yw4l{vertical-align:top}.tg .tg-vvaf{background-color:#FCFBE3;font-weight:bold;vertical-align:top}@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style><div class="tg-wrap"><table class="tg">'
    f.write(hCode1)
    f.write("<h2 style='color:#4285F4;' align='center'>"+title+"</h2>")
    for i in range(len(matrix)):
        f.write("<tr>")
        for j in range(len(matrix[i])):
            if i==0 or j==0:
                f.write('<th class="tg-031e">'+str(matrix[i][j])+'</th>')
            else:
                f.write('<td class="tg-z2zr">'+str(matrix[i][j])+'</td>')
        f.write("</tr>")    
    
    hCode2="</table></div>"
    f.write(hCode2)
    f.close()


if __name__=="__main__":
        currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
        htmlGenerator([["","File1","File2"],["File1",40,50],["File2",60,70]],currentDirABSPath+os.sep+"a.html")
    