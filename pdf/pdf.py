import PyPDF2

"""
    从pdf提取文本
"""
# pdfReader = PyPDF2.PdfFileReader(open('测试用例/test.pdf', 'rb'))
# print(pdfReader.numPages)
# print(pdfReader.getPage(0).extractText()) # 提取内容可能会出错


"""
    加密pdf
"""
# pdfReader = PyPDF2.PdfFileReader(open('测试用例/test.pdf', 'rb'))
# pdfWriter = PyPDF2.PdfFileWriter()
#
# for pageNum in range(pdfReader.numPages):
#     pdfWriter.addPage(pdfReader.getPage(pageNum))
#
# pdfWriter.encrypt('123')  # 加密
#
# result = open('测试用例/encryptedtest.pdf', 'wb')
# pdfWriter.write(result)
# result.close()


"""
    解密pdf
"""
# pdfReader = PyPDF2.PdfFileReader(open('测试用例/encryptedtest.pdf', 'rb'))
# print(pdfReader.isEncrypted)  # 是否加密
# pdfReader.decrypt('123')  # 解密
# print(pdfReader.getPage(0).extractText())
