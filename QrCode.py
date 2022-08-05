import os
import fitz
import qrcode

pdf_dir=[]
def get_pdffile():
	docunames = os.listdir()
	for docuname in docunames:
		if os.path.splitext(docuname)[1]=='.pdf': #目录下包含.pdf的文件
			pdf_dir.append(docuname)

def conver_img():
	for file in pdf_dir:
		#pdfz转长图片
		command = "python3 pdf-to-long-image.py --pdf_path "+file+""
		os.system(command)

pngpath = []
def get_pngfile():
	filePath = os.getcwd()
	for root, dirs, files in os.walk(filePath):
	    for file in files:
	        if os.path.splitext(file)[1] == '.jpg':
	            pngpath.append(os.path.join(file))
	print("开始生成二维码")
	print("图片数量为："+str(len(pngpath)))
	for file in pngpath:
		context = 'http://172.16.20.94/'+file
		print(context)
		img = qrcode.make(context)
		save_path='./erweima/'
		imgname = file.split(".")[0]
		img.save(save_path+imgname+'.jpg')
	filePath = os.getcwd() + "/erweima/"
	erweimapath = []
	for root, dirs, files in os.walk(filePath):
	    for file in files:
	        if os.path.splitext(file)[1] == '.jpg':
	            erweimapath.append(os.path.join(file))
	print("二维码数量："+str(len(pngpath)))

if __name__=='__main__':
	get_pdffile()
	conver_img()
	get_pngfile()
