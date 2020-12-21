# Hướng dẫn cách chạy chương trình gắn nhãn từ loại cho Tiếng Việt

## Các thư viện cần thiết

> [pycrfsuite](https://pypi.org/project/python-crfsuite/)
> 
> [underthesea](https://pypi.org/project/underthesea/)
> 
> [tkinter](https://www.codegrepper.com/code-examples/delphi/pip+install+tkinter)
> 
> re và unicodedata

## Chạy file ```CRF_GUI.py``` để hiển thị dưới dạng giao diện người dùng

* Chọn input là một ```file``` hoặc là một câu - ```sentence```
* Kết quả sẽ trả về dưới dạng chuỗi ```word/tag```

## File ```CRF_tagger.py```

* Chạy đoạn code bên dưới để **lấy ngữ liệu** từ ```vtb.txt``` và **huấn luyện**

```python
data = get_data() 
train(train_data=data, model_file=_model_file)
```

 * Để gắn nhãn chạy đoạn lệnh bên dưới

 ```python
l = [['học_sinh','học','sinh_học'],['học_sinh', 'học', 'ăn', '.']]
print(tag_sents(l))
 ```

## Thành viên:

* Trịnh Văn Minh - 1712601
* Nguyễn Long Nhật - 1712633