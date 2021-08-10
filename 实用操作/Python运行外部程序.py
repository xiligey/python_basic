"""Python运行外部程序的四种方法
1. os.system(command)
2. ShellExecute
3. CreateProcess
4. call
"""

if __name__ == '__main__':
    # 1.使用os.system函数运行其他程序或脚本
    import os

    command = 'code 1.txt'  # 使用vscode打开1.txt文件
    os.system(command)

    # 2.使用ShellExecute函数运行其他程序(只支持Windows系统)
    # from win32api import ShellExecute
    # ShellExecute(hwnd,op,file,params,dir,bShow)
    #   - hwnd:父窗口的句柄，若没有则为0
    #   - op：要进行的操作，为open，print or 空
    #   - file：要运行的程序或脚本
    #   - params 要向程序传递的参数，如果打开的是文件则为空
    #   - dir：程序初始化的目录
    #   - bShow：是否显示窗口
    # 示例
    #   1. ShellExecute(0,'open','notepad.exe','python.txt','',1)
    #   2. ShellExecute(0,'open','http://www.baidu.com','','',1)
    #   3. ShellExecute(0,'open','F:\\Love\\Lady Antebellum - Need You Now.ape','','',1)

    # 3.使用CreateProcess函数(只支持Windows系统)
    # import win32process
    # from win32process import CreateProcess
    #
    # CreateProcess('c:\\windows\\notepad.exe',
    #               '',
    #               None,
    #               None,
    #               0,
    #               win32process.CREATE_NO_WINDOW,
    #               None,
    #               None,
    #               win32process.STARTUPINFO())

    # 4. call
    from subprocess import call

    call("pip install --upgrade pip", shell=True)
