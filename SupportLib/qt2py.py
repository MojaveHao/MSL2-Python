"""
qt2py_release_v_1.3.py ui文件转Python代码
兼容PySide2 5.14.0及以下版本
"""

import os
import tkinter as tk
import traceback
from tkinter import filedialog, messagebox, ttk

import PySide2


class Qt2Py:
    """A class to convert ui file to Python codes."""

    def __init__(self, src):
        """Full directories of a ui file."""
        self.src = src
        self.error_dir = os.path.join(os.path.dirname(__file__), "errors.txt")

    def _handle_exception(self):
        """Save Exception infos to an file."""
        with open(self.error_dir, 'a', encoding='utf-8') as f:
            traceback.print_exc(file=f)
            f.write('\n')

    def _is_lower_version(self) -> bool:
        """
        Check if current PySide2 version is lower than 5.14.0.

            :return: comparsion result
        """
        ps2_v, std_v = PySide2.__version__.split('.'), '5.14.0'.split('.')
        len_ps2, len_std = len(ps2_v), len(std_v)
        if len_ps2 > len_std:
            std_v += ['0'] * (len_ps2 - len_std)
        else:
            ps2_v += ['0'] * (len_std - len_ps2)
        for i in range(len(ps2_v)):
            if int(ps2_v[i]) < int(std_v[i]):
                return True
        return False

    def _generate_dst(self) -> str:
        """
        Return a Python file name according to ui file.

            :return: python file name
        """
        src_dir, src_name = os.path.split(self.src)
        return os.path.join(src_dir, f"ui_{os.path.splitext(src_name)[0]}.py")

    def _qt2py_version_higher(self) -> bool:
        """
        Convert higher version ui file to Python codes. Return bool.

            :return: True for successful conversion False for failure.
        """
        # 找到并切换到PySide2所在目录
        os.chdir(os.path.dirname(PySide2.__file__))

        # 生成python文件名
        dst = self._generate_dst()

        # 开始转换
        if os.system(f'.{os.sep}uic {self.src} -g python -o {dst}'):
            return False
        else:
            try:
                with open(dst, encoding='utf-8') as f:
                    codes = f.read().replace('QString()', '""')
                with open(dst, 'w', encoding='utf-8') as f:
                    f.write(codes)
                return True
            except Exception:
                self._handle_exception()
                return False

    def _qt2py_version_lower(self) -> bool:
        """
        Convert lower version ui file to Python codes. Return bool.

            :return: True for successful conversion False for failure.
        """
        # 生成python文件名
        dst = self._generate_dst()

        import pyside2uic

        # 开始转换
        try:
            with open(dst, 'w', encoding='utf-8') as f:
                pyside2uic.compileUi(self.src, f)
        except Exception:
            self._handle_exception()
            return False
        else:
            return True

    def qt2py(self) -> bool:
        """
        Convert ui file to Python file according PySide2 version.

            :return: True for successful conversion False for failure.
        """
        if self._is_lower_version():
            return self._qt2py_version_lower()
        else:
            return self._qt2py_version_higher()


class Ui_Qt2Py:
    """A class to create a GUI for file conversion."""

    def __init__(self, master):
        """Set up attributes and GUI widgets."""
        self.master = master

        self.setup_Master()
        self.setup_Ui()
        self.bind_Method()

    def setup_Master(self):
        """Adjustments to root window."""
        self.master.resizable(False, False)
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry(f'340x240+{(width-340)//2}+{(height-240)//2}')
        self.master.title('Qt Creator转换器')

    def setup_Ui(self):
        """Add all widgets to root window."""
        ttk.Label(
            self.master, text='Qt Creator转换器', font=('Calibri', 20)
        ).place(anchor='center', relx=0.5, rely=0.15)

        ttk.Label(
            self.master, font=('Arial', 12),
            text=f'PySide2 版本：{PySide2.__version__}'
        ).place(anchor='center', relx=0.5, rely=0.35)

        self.btn_choose_file = ttk.Button(self.master, text='选择ui文件')
        self.btn_choose_file.place(anchor='center', relx=0.275, rely=0.55,
                                   relwidth=0.35, relheight=0.15)

        self.btn_convert = ttk.Button(self.master, text='开始转换')
        self.btn_convert.place(anchor='center', relx=0.725, rely=0.55,
                               relwidth=0.35, relheight=0.15)

        self.file_path = ttk.Label(
            self.master, text='请选择需要转换的ui文件……',
            font=('Arial', 16), wraplength=320, anchor='center')
        self.file_path.place(anchor='center', relx=0.5, rely=0.8, relwidth=1)

    def _select_file(self, event=None):
        """Using file-selecting dialog to get ui file path."""
        file_path = filedialog.askopenfilename(
            title='打开文件', filetypes=[('Qt', '*.ui')])
        if file_path:
            self.file_path['text'] = file_path

    def _convert_file(self, event=None):
        """Method to convert a ui file to Python codes."""
        if not os.path.isfile(self.file_path['text']):
            messagebox.showerror('文件错误', '请至少选择一个ui文件')
        else:
            q = Qt2Py(self.file_path['text'])
            if q.qt2py():
                messagebox.showinfo('转换结果', '转换成功')
            else:
                messagebox.showinfo('转换结果', '转换出错')

    def _add_to_clipboard(self, event=None):
        """Add file path to clipboard."""
        path = self.file_path['text']
        if os.path.isfile(path):
            self.master.clipboard_append(path)
            messagebox.showinfo('操作结果', '路径已复制到剪贴板')
        else:
            messagebox.showinfo('操作结果', '未检测到有效文件路径')

    def bind_Method(self):
        """Bind methods to GUI buttons."""
        self.btn_choose_file['command'] = lambda: self._select_file()
        self.btn_convert['command'] = lambda: self._convert_file()

        self.master.bind_all('<Control-KeyPress-o>', self._select_file)
        self.master.bind_all('<Control-KeyPress-e>', self._convert_file)
        self.file_path.bind('<Double-Button-1>', self._add_to_clipboard)


def main():
    """Main entrance."""
    root = tk.Tk()
    Ui_Qt2Py(root)
    root.mainloop()


if __name__ == "__main__":
    main()
